"""
HelpDesk Info - Application de diagnostic PC professionnel
Auteur: Michael - LM-Code (https://lm-code.be)
Contact: contact@lm-code.be
GitHub: https://github.com/LM-Code-Be/helpdesk-info
Version: 1.0.0
Description: Outil web de diagnostic système pour techniciens IT permettant
             la collecte d'informations système, gestion des programmes,
             services et processus Windows.
"""

from flask import Flask, render_template, request, send_file, jsonify
import platform
import socket
import psutil
import uuid
import requests
import datetime
import os
import subprocess
import winreg
import logging
from io import BytesIO

# Configuration de l'application Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['JSON_AS_ASCII'] = False

# Configuration du système de logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('helpdesk.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def get_size(bytes_value, suffix="B"):
    """
    Convertit une taille en octets vers un format lisible par l'humain.

    Args:
        bytes_value: Nombre d'octets à convertir
        suffix: Suffixe à ajouter (par défaut "B" pour Bytes)

    Returns:
        String formaté avec l'unité appropriée (Ko, Mo, Go, To)

    Exemple:
        >>> get_size(1536)
        '1.50 KB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T"]:
        if bytes_value < factor:
            return f"{bytes_value:.2f} {unit}{suffix}"
        bytes_value /= factor
    return f"{bytes_value:.2f} P{suffix}"

def get_installed_programs():
    """
    Récupère la liste complète des programmes installés via le registre Windows.

    Cette fonction parcourt les clés de registre HKLM et HKCU pour identifier
    tous les programmes installés sur le système. Elle extrait le nom et la
    date d'installation lorsque disponible.

    Returns:
        list: Liste de dictionnaires contenant 'name' et 'install_date' pour chaque programme

    Note:
        Certains programmes peuvent ne pas avoir de date d'installation enregistrée
    """
    programs = []

    # Chemins de registre où Windows stocke les infos des programmes installés
    reg_paths = [
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
        (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
    ]

    for root, path in reg_paths:
        try:
            with winreg.OpenKey(root, path) as key:
                # Parcourir toutes les sous-clés (chaque programme)
                for i in range(winreg.QueryInfoKey(key)[0]):
                    try:
                        subkey_name = winreg.EnumKey(key, i)
                        with winreg.OpenKey(key, subkey_name) as subkey:
                            name = None
                            install_date = None

                            # Tenter de récupérer le nom du programme
                            try:
                                name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                            except FileNotFoundError:
                                # Certaines entrées n'ont pas de DisplayName
                                pass

                            # Tenter de récupérer la date d'installation
                            try:
                                install_date = winreg.QueryValueEx(subkey, "InstallDate")[0]
                            except FileNotFoundError:
                                # La date n'est pas toujours renseignée
                                pass

                            # Ajouter seulement si on a au moins un nom
                            if name:
                                programs.append({
                                    "name": name,
                                    "install_date": install_date if install_date else "Non disponible"
                                })
                    except Exception as e:
                        # Ignorer les sous-clés inaccessibles ou corrompues
                        logger.debug(f"Impossible de lire la sous-clé: {e}")
                        continue
        except Exception as e:
            logger.error(f"Erreur lors de l'accès au registre {path}: {e}")
            continue

    # Supprimer les doublons potentiels et trier par nom
    seen = set()
    unique_programs = []
    for prog in programs:
        if prog['name'] not in seen:
            seen.add(prog['name'])
            unique_programs.append(prog)

    return sorted(unique_programs, key=lambda x: x['name'].lower())

def get_services():
    """
    Récupère la liste complète des services Windows via PowerShell.

    Utilise Get-Service pour obtenir tous les services système avec leur
    nom, nom d'affichage et statut actuel.

    Returns:
        list: Liste de dictionnaires contenant les infos de chaque service

    Note:
        Requiert l'exécution de PowerShell. En cas d'échec, retourne une liste vide.
    """
    services = []
    try:
        # Exécution de la commande PowerShell pour lister les services
        result = subprocess.check_output(
            "powershell -Command \"Get-Service | Select-Object Name, DisplayName, Status\"",
            shell=True,
            text=True,
            timeout=10  # Timeout de sécurité
        )

        lines = result.strip().split('\n')

        # Les 3 premières lignes sont les en-têtes, on les ignore
        for line in lines[3:]:
            parts = line.strip().split(None, 2)
            if len(parts) == 3:
                services.append({
                    "name": parts[0],
                    "display_name": parts[1],
                    "status": parts[2]
                })

        logger.info(f"Récupération de {len(services)} services Windows réussie")

    except subprocess.TimeoutExpired:
        logger.error("Timeout lors de la récupération des services")
    except subprocess.CalledProcessError as e:
        logger.error(f"Erreur PowerShell lors de la récupération des services: {e}")
    except Exception as e:
        logger.error(f"Erreur inattendue lors de la récupération des services: {e}")

    return services

def get_processes():
    """
    Récupère la liste des processus actifs sur le système.

    Collecte pour chaque processus: PID, nom, utilisation CPU et mémoire.
    Les processus inaccessibles (permissions) sont automatiquement ignorés.

    Returns:
        list: Liste de dictionnaires avec les informations de chaque processus

    Note:
        L'utilisation CPU est un snapshot instantané et peut varier
    """
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            info = proc.info
            # Conversion de la mémoire en format lisible
            info['memory'] = get_size(info['memory_info'].rss)
            # Suppression de l'objet memory_info pour alléger le JSON
            del info['memory_info']
            processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Processus terminé pendant l'itération ou accès refusé
            continue
        except Exception as e:
            logger.debug(f"Erreur lors de la lecture d'un processus: {e}")
            continue

    return processes

def get_system_info():
    """
    Collecte complète des informations système.

    Récupère toutes les données pertinentes pour le diagnostic:
    - Informations matérielles (CPU, RAM, Disques)
    - Informations réseau (IP locale, publique, MAC)
    - Informations système (OS, utilisateur, uptime)

    Returns:
        dict: Dictionnaire contenant toutes les informations système

    Note:
        La récupération de l'IP publique nécessite une connexion Internet
    """
    # Récupération de l'IP publique via service externe
    try:
        public_ip = requests.get("https://api.ipify.org", timeout=5).text
        logger.info(f"IP publique récupérée: {public_ip}")
    except requests.RequestException as e:
        logger.warning(f"Impossible de récupérer l'IP publique: {e}")
        public_ip = "Non disponible"
    except Exception as e:
        logger.error(f"Erreur inattendue lors de la récupération de l'IP: {e}")
        public_ip = "Erreur"

    # Calcul du temps de démarrage et uptime
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time

    # === Informations des disques ===
    disk_info = []
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            disk_info.append({
                "device": part.device,
                "mountpoint": part.mountpoint,
                "fstype": part.fstype,
                "total": get_size(usage.total),
                "used": get_size(usage.used),
                "free": get_size(usage.free),
                "percent": usage.percent
            })
        except PermissionError:
            # Certains lecteurs peuvent ne pas être accessibles
            logger.debug(f"Accès refusé au disque {part.mountpoint}")
            continue
        except Exception as e:
            logger.debug(f"Erreur lors de la lecture du disque {part.device}: {e}")
            continue

    # === Informations réseau ===
    net_info = []
    mac_address = "Non disponible"
    addrs = psutil.net_if_addrs()

    for interface_name, interface_addresses in addrs.items():
        for address in interface_addresses:
            # Adresses IPv4
            if str(address.family) == 'AddressFamily.AF_INET':
                net_info.append({
                    "interface": interface_name,
                    "ip": address.address,
                    "netmask": address.netmask if address.netmask else "N/A",
                    "broadcast": address.broadcast if address.broadcast else "N/A"
                })
            # Adresse MAC (souvent sur la première interface physique)
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                if mac_address == "Non disponible":
                    mac_address = address.address

    # Construction du dictionnaire de retour
    system_data = {
        "hostname": socket.gethostname(),
        "username": os.getlogin(),
        "os": f"{platform.system()} {platform.release()} ({platform.version()})",
        "architecture": platform.machine(),
        "cpu": platform.processor(),
        "cores_physical": psutil.cpu_count(logical=False),
        "cores_total": psutil.cpu_count(logical=True),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "ram_total": get_size(psutil.virtual_memory().total),
        "ram_used": get_size(psutil.virtual_memory().used),
        "ram_available": get_size(psutil.virtual_memory().available),
        "boot_time": boot_time.strftime("%Y-%m-%d %H:%M:%S"),
        "uptime": str(uptime).split('.')[0],
        "ip_public": public_ip,
        "mac_address": mac_address,
        "disks": disk_info,
        "network": net_info
    }

    logger.info("Informations système collectées avec succès")
    return system_data

@app.route("/uninstall_program", methods=["POST"])
def uninstall_program():
    """
    Endpoint de désinstallation de programme via WMI/PowerShell.

    Cette opération peut prendre plusieurs minutes selon le programme.
    Requiert des privilèges administrateur.

    Returns:
        JSON avec success (bool) et message (str)
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({
                "success": False,
                "message": "Nom du programme manquant"
            }), 400

        program_name = data.get("name")
        logger.info(f"Tentative de désinstallation: {program_name}")

        # Sécurisation: échappement des guillemets pour éviter l'injection
        safe_name = program_name.replace("'", "''")

        # Exécution de la désinstallation via WMI
        result = subprocess.run([
            "powershell",
            "-Command",
            f"Get-WmiObject -Class Win32_Product | Where-Object {{$_.Name -eq '{safe_name}'}} | ForEach-Object {{$_.Uninstall()}}"
        ], capture_output=True, text=True, shell=True, timeout=300)

        if result.returncode == 0:
            logger.info(f"Désinstallation réussie: {program_name}")
            return jsonify({
                "success": True,
                "message": f"'{program_name}' a été désinstallé avec succès"
            })
        else:
            logger.error(f"Échec de désinstallation: {program_name} - {result.stderr}")
            return jsonify({
                "success": False,
                "message": f"Erreur lors de la désinstallation: {result.stderr}"
            })

    except subprocess.TimeoutExpired:
        logger.error(f"Timeout lors de la désinstallation de {program_name}")
        return jsonify({
            "success": False,
            "message": "La désinstallation a pris trop de temps (timeout)"
        }), 408
    except Exception as e:
        logger.error(f"Erreur lors de la désinstallation: {e}")
        return jsonify({
            "success": False,
            "message": f"Erreur inattendue: {str(e)}"
        }), 500

@app.route("/service_action", methods=["POST"])
def service_action():
    """
    Endpoint de gestion des services Windows (démarrer/arrêter/redémarrer).

    Actions supportées: start, stop, restart
    Requiert des privilèges administrateur.

    Returns:
        JSON avec success (bool) et message (str)
    """
    try:
        data = request.get_json()

        if not data or 'name' not in data or 'action' not in data:
            return jsonify({
                "success": False,
                "message": "Paramètres manquants (name ou action)"
            }), 400

        service_name = data.get("name")
        action = data.get("action").lower()

        # Validation de l'action
        valid_actions = ['start', 'stop', 'restart']
        if action not in valid_actions:
            return jsonify({
                "success": False,
                "message": f"Action invalide. Utilisez: {', '.join(valid_actions)}"
            }), 400

        logger.info(f"Action '{action}' sur le service: {service_name}")

        # Sécurisation du nom de service
        safe_name = service_name.replace("'", "''")

        # Mapping des actions vers les commandes PowerShell
        commands = {
            'start': f"Start-Service -Name '{safe_name}'",
            'stop': f"Stop-Service -Name '{safe_name}'",
            'restart': f"Restart-Service -Name '{safe_name}'"
        }

        # Exécution de la commande
        result = subprocess.run(
            ["powershell", "-Command", commands[action]],
            capture_output=True,
            text=True,
            shell=True,
            timeout=30
        )

        if result.returncode == 0:
            action_labels = {
                'start': 'démarré',
                'stop': 'arrêté',
                'restart': 'redémarré'
            }
            logger.info(f"Service {service_name} {action_labels[action]} avec succès")
            return jsonify({
                "success": True,
                "message": f"Le service '{service_name}' a été {action_labels[action]} avec succès"
            })
        else:
            logger.error(f"Échec de l'action {action} sur {service_name}: {result.stderr}")
            return jsonify({
                "success": False,
                "message": f"Erreur: {result.stderr.strip()}"
            })

    except subprocess.TimeoutExpired:
        logger.error(f"Timeout lors de l'action sur le service {service_name}")
        return jsonify({
            "success": False,
            "message": "L'opération a pris trop de temps"
        }), 408
    except Exception as e:
        logger.error(f"Erreur lors de l'action sur le service: {e}")
        return jsonify({
            "success": False,
            "message": f"Erreur inattendue: {str(e)}"
        }), 500

@app.route("/kill_process", methods=["POST"])
def kill_process():
    """
    Endpoint pour terminer un processus via son PID.

    Attention: Terminer certains processus système peut causer une instabilité.

    Returns:
        JSON avec success (bool) et message (str)
    """
    try:
        data = request.get_json()

        if not data or 'pid' not in data:
            return jsonify({
                "success": False,
                "message": "PID manquant"
            }), 400

        pid = int(data.get("pid"))

        # Vérification que le processus existe
        if not psutil.pid_exists(pid):
            return jsonify({
                "success": False,
                "message": f"Le processus avec le PID {pid} n'existe pas"
            }), 404

        logger.info(f"Tentative de terminaison du processus PID: {pid}")

        # Récupération du processus
        process = psutil.Process(pid)
        process_name = process.name()

        # Terminaison du processus
        process.terminate()

        # Attendre que le processus se termine (max 5 secondes)
        try:
            process.wait(timeout=5)
            logger.info(f"Processus {pid} ({process_name}) terminé avec succès")
            return jsonify({
                "success": True,
                "message": f"Le processus '{process_name}' (PID: {pid}) a été terminé"
            })
        except psutil.TimeoutExpired:
            # Si le processus ne se termine pas proprement, on force
            process.kill()
            logger.warning(f"Processus {pid} tué de force")
            return jsonify({
                "success": True,
                "message": f"Le processus '{process_name}' a été forcé à se terminer"
            })

    except psutil.NoSuchProcess:
        return jsonify({
            "success": False,
            "message": "Le processus n'existe plus"
        }), 404
    except psutil.AccessDenied:
        logger.error(f"Accès refusé pour terminer le processus {pid}")
        return jsonify({
            "success": False,
            "message": "Accès refusé. Privilèges administrateur requis."
        }), 403
    except ValueError:
        return jsonify({
            "success": False,
            "message": "PID invalide"
        }), 400
    except Exception as e:
        logger.error(f"Erreur lors de la terminaison du processus: {e}")
        return jsonify({
            "success": False,
            "message": f"Erreur inattendue: {str(e)}"
        }), 500

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Page d'accueil principale de l'application.

    Affiche les informations système et permet la soumission de problèmes.

    Methods:
        GET: Affichage de la page
        POST: Réception de la description du problème

    Returns:
        Template HTML avec les informations système
    """
    try:
        system_info = get_system_info()
        problem = ""

        if request.method == "POST":
            problem = request.form.get("problem", "")
            if problem:
                logger.info(f"Problème signalé par {system_info.get('username')}: {problem[:100]}...")
                # Ici, vous pourriez envoyer le problème par email ou le sauvegarder dans une base

        return render_template("index.html", info=system_info, problem=problem)

    except Exception as e:
        logger.error(f"Erreur lors du chargement de la page d'accueil: {e}")
        return render_template("error.html", error=str(e)), 500


@app.route("/export")
def export():
    """
    Génère et télécharge un rapport texte complet du système.

    Le rapport inclut toutes les informations système collectées dans un
    format texte lisible et structuré.

    Returns:
        Fichier texte téléchargeable
    """
    try:
        system_info = get_system_info()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Construction du rapport
        output = [
            "=" * 60,
            "RAPPORT DE DIAGNOSTIC SYSTÈME",
            f"Généré le: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Machine: {system_info.get('hostname')}",
            f"Utilisateur: {system_info.get('username')}",
            "=" * 60,
            ""
        ]

        # Ajout des informations
        for key, value in system_info.items():
            if isinstance(value, list):
                output.append(f"\n{key.upper().replace('_', ' ')}:")
                output.append("-" * 40)
                for item in value:
                    for subkey, subvalue in item.items():
                        output.append(f"  {subkey}: {subvalue}")
                    output.append("")
            else:
                output.append(f"{key.replace('_', ' ').title()}: {value}")

        output.append("\n" + "=" * 60)
        output.append("Fin du rapport")
        output.append("=" * 60)

        report = "\n".join(output)

        # Création du fichier en mémoire
        file_buffer = BytesIO()
        file_buffer.write(report.encode('utf-8'))
        file_buffer.seek(0)

        filename = f"rapport_diagnostic_{timestamp}.txt"
        logger.info(f"Export du rapport système: {filename}")

        return send_file(
            file_buffer,
            as_attachment=True,
            download_name=filename,
            mimetype='text/plain'
        )

    except Exception as e:
        logger.error(f"Erreur lors de l'export: {e}")
        return jsonify({
            "success": False,
            "message": "Erreur lors de la génération du rapport"
        }), 500


@app.route("/programs")
def programs():
    """
    Endpoint API retournant la liste des programmes installés.

    Returns:
        JSON array des programmes avec nom et date d'installation
    """
    try:
        programs_list = get_installed_programs()
        logger.info(f"Liste de {len(programs_list)} programmes récupérée")
        return jsonify(programs_list)
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des programmes: {e}")
        return jsonify([]), 500


@app.route("/services")
def services():
    """
    Endpoint API retournant la liste des services Windows.

    Returns:
        JSON array des services avec nom, nom affiché et statut
    """
    try:
        services_list = get_services()
        return jsonify(services_list)
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des services: {e}")
        return jsonify([]), 500


@app.route("/processes")
def processes():
    """
    Endpoint API retournant la liste des processus actifs.

    Returns:
        JSON array des processus avec PID, nom, CPU et mémoire
    """
    try:
        processes_list = get_processes()
        return jsonify(processes_list)
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des processus: {e}")
        return jsonify([]), 500

@app.errorhandler(404)
def not_found(error):
    """Gestionnaire d'erreur 404 - Page non trouvée."""
    return jsonify({"error": "Ressource non trouvée"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Gestionnaire d'erreur 500 - Erreur serveur."""
    logger.error(f"Erreur serveur: {error}")
    return jsonify({"error": "Erreur interne du serveur"}), 500


if __name__ == "__main__":
    try:
        import webbrowser

        # Configuration du serveur
        HOST = "127.0.0.1"
        PORT = 5000
        DEBUG = True  # Mettre False en production

        logger.info("=" * 60)
        logger.info("HelpDesk Info - Application de Diagnostic PC")
        logger.info("=" * 60)
        logger.info(f"Démarrage du serveur sur http://{HOST}:{PORT}")
        logger.info("Appuyez sur Ctrl+C pour arrêter le serveur")
        logger.info("=" * 60)

        # Ouverture automatique du navigateur
        webbrowser.open(f"http://{HOST}:{PORT}")

        # Lancement du serveur Flask
        app.run(
            host=HOST,
            port=PORT,
            debug=DEBUG,
            threaded=True  # Support des requêtes simultanées
        )

    except KeyboardInterrupt:
        logger.info("\nArrêt du serveur demandé par l'utilisateur")
    except Exception as e:
        logger.error(f"Erreur fatale lors du démarrage: {e}")
        input("Appuyez sur Entrée pour fermer...")
