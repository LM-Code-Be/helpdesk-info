---
# Métadonnées SEO pour l'article de blog
title: "Créer une Application Web de Diagnostic PC avec Flask et Python - Tutoriel Complet"
slug: "application-diagnostic-pc-flask-python-tutoriel"
meta_description: "Tutoriel pas à pas pour créer une application web professionnelle de diagnostic système Windows avec Flask, Python et Bootstrap. Idéal pour techniciens IT et administrateurs helpdesk."
keywords:
  - Flask Python
  - Application diagnostic PC
  - Monitoring système Windows
  - Python psutil
  - Interface web helpdesk
  - Gestion services Windows
  - PowerShell automation
  - Application IT professionnelle
  - Bootstrap DataTables
  - Tutoriel Flask avancé
author: "Michael - LM-Code"
date_published: "2025-01-29"
last_updated: "2025-01-29"
category: "Développement Web"
tags:
  - Python
  - Flask
  - Windows
  - Système
  - IT
  - HelpDesk
reading_time: "45 minutes"
difficulty: "Intermédiaire"
og_image: "/images/tutoriels/helpdesk-info-preview.jpg"
twitter_card: "summary_large_image"
canonical_url: "https://lm-code.be/tutoriels/application-diagnostic-pc-flask-python-tutoriel"
---

# 🖥️ Créer une Application Web de Diagnostic PC avec Flask et Python - Tutoriel Complet

> **Par Michael - LM-Code | Développeur Full Stack & Expert IT**
>
> Dans ce tutoriel, je vous guide pas à pas dans la création d'une application web professionnelle de diagnostic système pour techniciens IT. Vous apprendrez à créer une interface moderne permettant de monitorer, gérer et diagnostiquer des PC Windows à distance.

![Image principale - Dashboard de l'application](images/dashboard-principal.png)
*Emplacement: `/images/tutoriels/helpdesk-info/dashboard-principal.png`*

---

## 📋 Table des matières

1. [Introduction et présentation du projet](#introduction)
2. [Ce que vous allez apprendre](#ce-que-vous-allez-apprendre)
3. [Prérequis techniques](#prérequis-techniques)
4. [Architecture et technologies utilisées](#architecture-et-technologies)
5. [Étape 1 : Mise en place de l'environnement](#étape-1-environnement)
6. [Étape 2 : Structure du projet](#étape-2-structure)
7. [Étape 3 : Backend Flask et collecte système](#étape-3-backend)
8. [Étape 4 : Interface utilisateur moderne](#étape-4-frontend)
9. [Étape 5 : Design CSS professionnel](#étape-5-design)
10. [Étape 6 : Gestion des programmes](#étape-6-programmes)
11. [Étape 7 : Contrôle des services Windows](#étape-7-services)
12. [Étape 8 : Monitoring des processus](#étape-8-processus)
13. [Étape 9 : Export de rapports](#étape-9-export)
14. [Étape 10 : Sécurité et production](#étape-10-production)
15. [Compilation en exécutable](#compilation)
16. [Conclusion et prochaines étapes](#conclusion)

---

## 🎯 Introduction {#introduction}

En tant que développeur et technicien IT depuis plusieurs années, j'ai souvent eu besoin d'outils pour diagnostiquer rapidement les problèmes sur les postes de travail Windows. Les solutions existantes sont soit trop complexes, soit payantes, soit ne répondent pas exactement aux besoins.

C'est pourquoi j'ai décidé de créer **HelpDesk Info**, une application web légère et moderne qui permet de:

- ✅ Collecter toutes les informations système en un clin d'œil
- ✅ Gérer les programmes installés (avec désinstallation à distance)
- ✅ Contrôler les services Windows
- ✅ Monitorer les processus en temps réel
- ✅ Exporter des rapports de diagnostic

![Fonctionnalités de l'application](images/features-overview.png)
*Emplacement: `/images/tutoriels/helpdesk-info/features-overview.png`*

---

## 📚 Ce que vous allez apprendre {#ce-que-vous-allez-apprendre}

À la fin de ce tutoriel, vous saurez:

### Côté Backend (Python/Flask)
- 🐍 Créer une application Flask structurée et professionnelle
- 📊 Utiliser `psutil` pour collecter des informations système
- 🔧 Interagir avec le registre Windows via `winreg`
- ⚡ Exécuter des commandes PowerShell depuis Python
- 🛡️ Implémenter une gestion d'erreurs robuste
- 📝 Configurer un système de logging professionnel

### Côté Frontend (HTML/CSS/JavaScript)
- 🎨 Créer une interface moderne avec Bootstrap 5
- ✨ Implémenter des animations et transitions CSS
- 📱 Rendre l'interface responsive
- 📊 Utiliser DataTables pour des tableaux interactifs
- 🔔 Créer un système de notifications toast personnalisé
- 🎯 Gérer les requêtes AJAX avec Fetch API

### Bonnes pratiques
- ✅ Architecture MVC pour applications Flask
- ✅ Sécurisation des entrées utilisateur
- ✅ Documentation et commentaires professionnels
- ✅ Gestion des erreurs et exceptions
- ✅ Optimisation SEO et performances

---

## 🔧 Prérequis techniques {#prérequis-techniques}

### Connaissances requises
- **Python** : Niveau intermédiaire (fonctions, classes, modules)
- **HTML/CSS** : Bases solides
- **JavaScript** : Niveau débutant/intermédiaire
- **Windows** : Compréhension du système (services, processus, registre)

### Logiciels nécessaires
- **Python 3.8+** - [Télécharger](https://www.python.org/downloads/)
- **Visual Studio Code** (ou votre éditeur préféré) - [Télécharger](https://code.visualstudio.com/)
- **Git** (optionnel mais recommandé) - [Télécharger](https://git-scm.com/)
- **Windows 10/11** avec PowerShell 5.0+

### Temps estimé
⏱️ **45 minutes à 1h30** selon votre niveau

---

## 🏗️ Architecture et technologies utilisées {#architecture-et-technologies}

### Stack technique

```
Frontend (Client)
├── Bootstrap 5.3.2      → Framework CSS responsive
├── Bootstrap Icons      → Bibliothèque d'icônes moderne
├── DataTables 1.13.6    → Tables interactives
├── jQuery 3.7.1         → Manipulation DOM
└── CSS personnalisé     → Design moderne avec animations

Backend (Serveur)
├── Flask 3.0+           → Framework web Python
├── psutil 5.9+          → Monitoring système
├── requests 2.31+       → Requêtes HTTP
└── Modules Python natifs
    ├── winreg           → Accès registre Windows
    ├── subprocess       → Exécution PowerShell
    ├── platform         → Infos système
    └── socket           → Infos réseau
```

![Architecture de l'application](images/architecture-diagram.png)
*Emplacement: `/images/tutoriels/helpdesk-info/architecture-diagram.png`*

### Flux de données

```
Navigateur Web → Flask (Routes) → Fonctions Python → Système Windows
      ↑                                                      ↓
      └──────────────── JSON Response ─────────────────────┘
```

---

## 🚀 Étape 1 : Mise en place de l'environnement {#étape-1-environnement}

### 1.1 Création du dossier projet

Ouvrez un terminal et créez le dossier principal:

```bash
mkdir helpdesk-info
cd helpdesk-info
```

### 1.2 Environnement virtuel Python

Un environnement virtuel isole les dépendances de votre projet:

```bash
# Création de l'environnement virtuel
python -m venv venv

# Activation (Windows)
venv\Scripts\activate

# Vous devriez voir (venv) devant votre prompt
```

![Terminal avec environnement virtuel actif](images/venv-activation.png)
*Emplacement: `/images/tutoriels/helpdesk-info/venv-activation.png`*

### 1.3 Installation des dépendances

Créez le fichier `requirements.txt`:

```txt
Flask>=3.0.0
psutil>=5.9.0
requests>=2.31.0
```

Puis installez:

```bash
pip install -r requirements.txt
```

**💡 Astuce:** Utilisez `pip list` pour vérifier que tout est installé.

---

## 📂 Étape 2 : Structure du projet {#étape-2-structure}

### 2.1 Arborescence complète

Créez cette structure de fichiers:

```
helpdesk-info/
│
├── venv/                    # Environnement virtuel (généré)
├── static/                  # Fichiers statiques (CSS, JS, images)
│   └── style.css           # Notre CSS personnalisé
├── templates/              # Templates HTML (Jinja2)
│   └── index.html          # Page principale
├── main.py                 # Application Flask principale
├── requirements.txt        # Dépendances Python
└── README.md              # Documentation
```

### 2.2 Création des dossiers

```bash
# Création des dossiers nécessaires
mkdir static templates

# Création des fichiers vides
type nul > main.py
type nul > static\style.css
type nul > templates\index.html
```

![Structure du projet dans VS Code](images/project-structure.png)
*Emplacement: `/images/tutoriels/helpdesk-info/project-structure.png`*

---

## 🐍 Étape 3 : Backend Flask et collecte système {#étape-3-backend}

### 3.1 Configuration de base de Flask

Ouvrez `main.py` et commençons par les imports et la configuration:

```python
"""
HelpDesk Info - Application de diagnostic PC professionnel
Auteur: Michael - LM-Code (https://lm-code.be)
"""

from flask import Flask, render_template, request, send_file, jsonify
import platform
import socket
import psutil
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
```

**🔍 Explication:**
- `SECRET_KEY`: Sécurise les sessions Flask
- `JSON_AS_ASCII=False`: Permet les caractères accentués dans le JSON
- `logging`: Crée un fichier de log pour tracer les actions

### 3.2 Fonction de conversion de taille

Cette fonction utilitaire convertit les octets en format lisible:

```python
def get_size(bytes_value, suffix="B"):
    """
    Convertit une taille en octets vers un format lisible.

    Exemple: 1536 → "1.50 KB"
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T"]:
        if bytes_value < factor:
            return f"{bytes_value:.2f} {unit}{suffix}"
        bytes_value /= factor
    return f"{bytes_value:.2f} P{suffix}"
```

### 3.3 Collecte des informations système

La fonction la plus importante - elle collecte toutes les données:

```python
def get_system_info():
    """
    Collecte complète des informations système.

    Returns:
        dict: Toutes les informations système formatées
    """
    # IP publique via service externe
    try:
        public_ip = requests.get("https://api.ipify.org", timeout=5).text
        logger.info(f"IP publique récupérée: {public_ip}")
    except Exception as e:
        logger.warning(f"Impossible de récupérer l'IP publique: {e}")
        public_ip = "Non disponible"

    # Temps de démarrage et uptime
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time

    # Informations des disques
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
            continue

    # Informations réseau
    net_info = []
    mac_address = "Non disponible"
    for interface_name, interface_addresses in psutil.net_if_addrs().items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                net_info.append({
                    "interface": interface_name,
                    "ip": address.address,
                    "netmask": address.netmask if address.netmask else "N/A"
                })

    # Dictionnaire de retour
    return {
        "hostname": socket.gethostname(),
        "username": os.getlogin(),
        "os": f"{platform.system()} {platform.release()}",
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
```

![Console montrant les informations système](images/system-info-console.png)
*Emplacement: `/images/tutoriels/helpdesk-info/system-info-console.png`*

**🔑 Points clés:**
- `psutil.cpu_percent()`: Utilisation CPU en temps réel
- `psutil.virtual_memory()`: Statistiques mémoire RAM
- `psutil.disk_partitions()`: Liste des disques
- Gestion des erreurs avec `try/except` pour éviter les crashs

### 3.4 Route principale

```python
@app.route("/", methods=["GET", "POST"])
def index():
    """Page d'accueil principale"""
    try:
        system_info = get_system_info()
        problem = ""

        if request.method == "POST":
            problem = request.form.get("problem", "")
            if problem:
                logger.info(f"Problème signalé: {problem[:100]}...")

        return render_template("index.html", info=system_info, problem=problem)

    except Exception as e:
        logger.error(f"Erreur: {e}")
        return jsonify({"error": str(e)}), 500
```

### 3.5 Lancement du serveur

Ajoutez à la fin du fichier:

```python
if __name__ == "__main__":
    import webbrowser

    HOST = "127.0.0.1"
    PORT = 5000

    logger.info("=" * 60)
    logger.info("HelpDesk Info - Démarrage")
    logger.info(f"URL: http://{HOST}:{PORT}")
    logger.info("=" * 60)

    # Ouverture automatique du navigateur
    webbrowser.open(f"http://{HOST}:{PORT}")

    # Lancement du serveur
    app.run(host=HOST, port=PORT, debug=True, threaded=True)
```

**🧪 Test:** Lancez `python main.py` - Le navigateur devrait s'ouvrir automatiquement!

---

## 🎨 Étape 4 : Interface utilisateur moderne {#étape-4-frontend}

### 4.1 Structure HTML de base

Ouvrez `templates/index.html`:

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>HelpDesk Info - Diagnostic PC Professionnel</title>

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />

  <!-- DataTables CSS -->
  <link href="https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css" rel="stylesheet" />

  <!-- Bootstrap Icons -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet" />

  <!-- Notre CSS personnalisé -->
  <link href="{{ url_for('static', filename='style.css') }}" rel="stylesheet" />
</head>
<body>
  <!-- Contenu à venir -->
</body>
</html>
```

### 4.2 Header avec icône

```html
<body>
  <div class="container py-5">
    <div class="card shadow-lg rounded-4 main-card">
      <!-- En-tête avec dégradé -->
      <div class="card-header text-white text-center main-header">
        <h3 class="mb-0">
          <i class="bi bi-pc-display-horizontal header-icon"></i>
          HelpDesk Info – Diagnostic PC Professionnel
        </h3>
      </div>

      <div class="card-body p-4">
        <!-- Navigation et contenu ici -->
      </div>
    </div>
  </div>
</body>
```

![Header de l'application](images/header-design.png)
*Emplacement: `/images/tutoriels/helpdesk-info/header-design.png`*

### 4.3 Navigation par onglets

```html
<!-- Navigation par onglets -->
<ul class="nav nav-tabs mb-4" id="infoTabs" role="tablist">
  <li class="nav-item" role="presentation">
    <button class="nav-link active" id="sys-tab" data-bs-toggle="tab"
            data-bs-target="#system" type="button" role="tab">
      <i class="bi bi-info-circle"></i>
      Infos Système
    </button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="prog-tab" data-bs-toggle="tab"
            data-bs-target="#programs" type="button" role="tab">
      <i class="bi bi-app-indicator"></i>
      Programmes
    </button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="serv-tab" data-bs-toggle="tab"
            data-bs-target="#services" type="button" role="tab">
      <i class="bi bi-gear"></i>
      Services
    </button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="proc-tab" data-bs-toggle="tab"
            data-bs-target="#processes" type="button" role="tab">
      <i class="bi bi-cpu"></i>
      Processus
    </button>
  </li>
</ul>
```

### 4.4 Contenu de l'onglet "Infos Système"

```html
<div class="tab-content">
  <!-- Onglet Infos Système -->
  <div class="tab-pane fade show active" id="system" role="tabpanel">
    <div class="row g-3">
      {% for key, value in info.items() if not value is iterable or value is string %}
        <div class="col-md-4">
          <label class="form-label">{{ key.replace('_', ' ').title() }}</label>
          <input type="text" class="form-control" value="{{ value }}" readonly>
        </div>
      {% endfor %}
    </div>

    <hr class="my-4">

    <!-- Formulaire de problème -->
    <form method="POST">
      <label class="form-label">
        <i class="bi bi-chat-left-text"></i>
        Décrivez votre problème
      </label>
      <textarea name="problem" class="form-control mb-3" rows="4"
                placeholder="Décrivez en détail le problème rencontré...">{{ problem }}</textarea>
      <div class="d-flex justify-content-end gap-2">
        <a href="/export" class="btn btn-outline-secondary">
          <i class="bi bi-download"></i>
          Exporter le rapport
        </a>
        <button type="submit" class="btn btn-primary">
          <i class="bi bi-send"></i>
          Envoyer le rapport
        </button>
      </div>
    </form>
  </div>
</div>
```

![Onglet Infos Système](images/system-tab.png)
*Emplacement: `/images/tutoriels/helpdesk-info/system-tab.png`*

---

## 🎨 Étape 5 : Design CSS professionnel {#étape-5-design}

### 5.1 Variables CSS et thème

Ouvrez `static/style.css`:

```css
/* Palette de couleurs professionnelle */
:root {
  /* Couleurs principales */
  --primary-color: #2563eb;
  --primary-dark: #1e40af;
  --secondary-color: #8b5cf6;
  --success-color: #10b981;
  --danger-color: #ef4444;

  /* Fond */
  --bg-gradient-start: #f0f9ff;
  --bg-gradient-end: #e0e7ff;

  /* Texte */
  --text-primary: #1e293b;
  --text-secondary: #64748b;

  /* Ombres */
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);

  /* Transitions */
  --transition-base: 300ms ease-in-out;
}
```

**💡 Pourquoi des variables CSS?**
- Cohérence du design
- Modifications rapides
- Maintenance facilitée

### 5.2 Styles globaux et animations

```css
body {
  background: linear-gradient(135deg, var(--bg-gradient-start) 0%, var(--bg-gradient-end) 100%);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: var(--text-primary);
  min-height: 100vh;
}

/* Animation d'apparition */
.container {
  animation: fadeInUp 0.6s ease-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### 5.3 Header avec effet shimmer

```css
.card-header.main-header {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
  padding: 2rem;
  position: relative;
  overflow: hidden;
}

/* Effet de brillance animé */
.card-header.main-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  animation: shimmer 3s infinite;
}

@keyframes shimmer {
  0% { left: -100%; }
  100% { left: 100%; }
}
```

![Effet shimmer animé](images/shimmer-effect.gif)
*Emplacement: `/images/tutoriels/helpdesk-info/shimmer-effect.gif`*

### 5.4 Onglets stylisés

```css
.nav-tabs .nav-link {
  border: none;
  color: var(--text-secondary);
  font-weight: 600;
  padding: 0.75rem 1.5rem;
  border-radius: 10px 10px 0 0;
  transition: all var(--transition-base);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-tabs .nav-link:hover {
  color: var(--primary-color);
  background-color: #f1f5f9;
  transform: translateY(-2px);
}

.nav-tabs .nav-link.active {
  color: var(--primary-color);
  background: linear-gradient(to bottom, #ffffff 0%, #f8fafc 100%);
  border-bottom: 3px solid var(--primary-color);
}
```

### 5.5 Boutons avec dégradés

```css
.btn {
  border-radius: 10px;
  font-weight: 600;
  padding: 0.625rem 1.5rem;
  transition: all var(--transition-base);
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
  border: none;
}

.btn-danger {
  background: linear-gradient(135deg, var(--danger-color) 0%, #dc2626 100%);
  border: none;
}
```

![Boutons stylisés](images/buttons-design.png)
*Emplacement: `/images/tutoriels/helpdesk-info/buttons-design.png`*

---

## 💾 Étape 6 : Gestion des programmes {#étape-6-programmes}

### 6.1 Fonction de récupération des programmes (Backend)

Dans `main.py`, ajoutez:

```python
def get_installed_programs():
    """
    Récupère la liste des programmes installés via le registre Windows.
    """
    programs = []

    # Chemins de registre
    reg_paths = [
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
        (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
    ]

    for root, path in reg_paths:
        try:
            with winreg.OpenKey(root, path) as key:
                for i in range(winreg.QueryInfoKey(key)[0]):
                    try:
                        subkey_name = winreg.EnumKey(key, i)
                        with winreg.OpenKey(key, subkey_name) as subkey:
                            name = None
                            install_date = None

                            # Nom du programme
                            try:
                                name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                            except FileNotFoundError:
                                pass

                            # Date d'installation
                            try:
                                install_date = winreg.QueryValueEx(subkey, "InstallDate")[0]
                            except FileNotFoundError:
                                pass

                            if name:
                                programs.append({
                                    "name": name,
                                    "install_date": install_date if install_date else "Non disponible"
                                })
                    except Exception:
                        continue
        except Exception as e:
            logger.error(f"Erreur registre: {e}")
            continue

    # Suppression des doublons et tri
    seen = set()
    unique_programs = []
    for prog in programs:
        if prog['name'] not in seen:
            seen.add(prog['name'])
            unique_programs.append(prog)

    return sorted(unique_programs, key=lambda x: x['name'].lower())

# Route API
@app.route("/programs")
def programs():
    """Endpoint retournant la liste des programmes (JSON)"""
    try:
        programs_list = get_installed_programs()
        logger.info(f"Liste de {len(programs_list)} programmes récupérée")
        return jsonify(programs_list)
    except Exception as e:
        logger.error(f"Erreur: {e}")
        return jsonify([]), 500
```

**🔍 Explications:**
- `winreg.OpenKey()`: Ouvre une clé du registre Windows
- `winreg.EnumKey()`: Énumère les sous-clés
- `QueryValueEx()`: Lit une valeur dans le registre

### 6.2 Interface HTML pour les programmes

Dans `templates/index.html`, après l'onglet système:

```html
<!-- Onglet Programmes -->
<div class="tab-pane fade" id="programs" role="tabpanel">
  <div class="alert alert-info alert-custom mb-3">
    <i class="bi bi-info-circle"></i>
    <strong>Programmes installés</strong> - Liste complète des applications présentes sur le système
  </div>

  <table id="programsTable" class="table table-striped" style="width:100%">
    <thead>
      <tr>
        <th><i class="bi bi-app"></i> Nom du programme</th>
        <th><i class="bi bi-calendar-event"></i> Date d'installation</th>
        <th><i class="bi bi-gear"></i> Actions</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>
</div>
```

### 6.3 Chargement des données avec JavaScript

Avant la balise `</body>`, ajoutez:

```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.min.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/dataTables.bootstrap5.min.js"></script>

<script>
// Fonction de chargement de table
function loadTable(url, tableId, columns) {
  $.getJSON(url, function(data) {
    $(tableId).DataTable({
      destroy: true,
      data: data,
      columns: columns,
      language: {
        search: "Rechercher :",
        lengthMenu: "Afficher _MENU_ entrées",
        info: "Affichage de _START_ à _END_ sur _TOTAL_ entrées",
        paginate: {
          first: "Premier",
          last: "Dernier",
          next: "Suivant",
          previous: "Précédent"
        }
      }
    });
  });
}

// Chargement de l'onglet Programmes
$('#prog-tab').on('shown.bs.tab', () => {
  loadTable('/programs', '#programsTable', [
    { data: 'name' },
    { data: 'install_date' },
    {
      data: null,
      render: function(data, type, row) {
        return `<button class="btn btn-sm btn-danger" onclick="uninstallProgram('${row.name}')">
          <i class="bi bi-trash"></i> Désinstaller
        </button>`;
      }
    }
  ]);
});
</script>
```

![Table des programmes avec DataTables](images/programs-table.png)
*Emplacement: `/images/tutoriels/helpdesk-info/programs-table.png`*

**📊 Avantages de DataTables:**
- Tri des colonnes
- Recherche instantanée
- Pagination automatique
- Responsive design

---

## ⚙️ Étape 7 : Contrôle des services Windows {#étape-7-services}

### 7.1 Backend - Récupération des services

```python
def get_services():
    """Récupère la liste des services Windows via PowerShell"""
    services = []
    try:
        result = subprocess.check_output(
            "powershell -Command \"Get-Service | Select-Object Name, DisplayName, Status\"",
            shell=True,
            text=True,
            timeout=10
        )

        lines = result.strip().split('\n')

        # Les 3 premières lignes sont les en-têtes
        for line in lines[3:]:
            parts = line.strip().split(None, 2)
            if len(parts) == 3:
                services.append({
                    "name": parts[0],
                    "display_name": parts[1],
                    "status": parts[2]
                })

        logger.info(f"{len(services)} services récupérés")
    except Exception as e:
        logger.error(f"Erreur services: {e}")

    return services

@app.route("/services")
def services():
    """Endpoint API pour les services"""
    try:
        return jsonify(get_services())
    except Exception as e:
        logger.error(f"Erreur: {e}")
        return jsonify([]), 500
```

### 7.2 Actions sur les services

```python
@app.route("/service_action", methods=["POST"])
def service_action():
    """Démarre/Arrête/Redémarre un service"""
    try:
        data = request.get_json()

        if not data or 'name' not in data or 'action' not in data:
            return jsonify({"success": False, "message": "Paramètres manquants"}), 400

        service_name = data.get("name")
        action = data.get("action").lower()

        # Validation
        if action not in ['start', 'stop', 'restart']:
            return jsonify({"success": False, "message": "Action invalide"}), 400

        logger.info(f"Action '{action}' sur service: {service_name}")

        # Sécurisation
        safe_name = service_name.replace("'", "''")

        # Commandes PowerShell
        commands = {
            'start': f"Start-Service -Name '{safe_name}'",
            'stop': f"Stop-Service -Name '{safe_name}'",
            'restart': f"Restart-Service -Name '{safe_name}'"
        }

        # Exécution
        result = subprocess.run(
            ["powershell", "-Command", commands[action]],
            capture_output=True,
            text=True,
            shell=True,
            timeout=30
        )

        if result.returncode == 0:
            return jsonify({
                "success": True,
                "message": f"Service {action} avec succès"
            })
        else:
            return jsonify({
                "success": False,
                "message": result.stderr.strip()
            })

    except Exception as e:
        logger.error(f"Erreur: {e}")
        return jsonify({"success": False, "message": str(e)}), 500
```

**🔐 Points de sécurité:**
- Validation de l'action (whitelist)
- Échappement des guillemets (`replace("'", "''")`)
- Timeout pour éviter les blocages
- Logs de toutes les actions

### 7.3 Frontend - Interface des services

```html
<!-- Onglet Services -->
<div class="tab-pane fade" id="services" role="tabpanel">
  <div class="alert alert-warning alert-custom mb-3">
    <i class="bi bi-exclamation-triangle"></i>
    <strong>Services Windows</strong> - Privilèges administrateur requis
  </div>

  <table id="servicesTable" class="table table-striped" style="width:100%">
    <thead>
      <tr>
        <th><i class="bi bi-tag"></i> Nom</th>
        <th><i class="bi bi-card-text"></i> Nom affiché</th>
        <th><i class="bi bi-activity"></i> Statut</th>
        <th><i class="bi bi-sliders"></i> Actions</th>
      </tr>
    </thead>
    <tbody></tbody>
  </table>
</div>
```

### 7.4 JavaScript - Affichage et actions

```javascript
// Fonction d'action sur service
function serviceAction(name, action) {
  const actionLabels = {
    start: 'démarrage',
    stop: 'arrêt',
    restart: 'redémarrage'
  };

  showToast(`${actionLabels[action]} du service "${name}" en cours...`, 'info');

  fetch('/service_action', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, action })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      showToast(data.message, 'success');
      setTimeout(() => $('#serv-tab').click(), 1500);
    } else {
      showToast(data.message, 'error');
    }
  })
  .catch(() => showToast('Erreur réseau', 'error'));
}

// Chargement de l'onglet Services
$('#serv-tab').on('shown.bs.tab', () => {
  loadTable('/services', '#servicesTable', [
    { data: 'name' },
    { data: 'display_name' },
    {
      data: 'status',
      render: function(data) {
        const isRunning = data === 'Running';
        return `<span class="badge ${isRunning ? 'status-running' : 'status-stopped'}">
          <i class="bi ${isRunning ? 'bi-play-circle' : 'bi-stop-circle'}"></i> ${data}
        </span>`;
      }
    },
    {
      data: null,
      render: function(data, type, row) {
        return `
          <button class="btn btn-sm btn-success me-1" onclick="serviceAction('${row.name}','start')" title="Démarrer">
            <i class="bi bi-play-fill"></i>
          </button>
          <button class="btn btn-sm btn-warning me-1" onclick="serviceAction('${row.name}','stop')" title="Arrêter">
            <i class="bi bi-stop-fill"></i>
          </button>
          <button class="btn btn-sm btn-info" onclick="serviceAction('${row.name}','restart')" title="Redémarrer">
            <i class="bi bi-arrow-clockwise"></i>
          </button>
        `;
      }
    }
  ]);
});
```

![Gestion des services](images/services-management.png)
*Emplacement: `/images/tutoriels/helpdesk-info/services-management.png`*

---

## 🔄 Étape 8 : Monitoring des processus {#étape-8-processus}

### 8.1 Backend - Liste des processus

```python
def get_processes():
    """Récupère la liste des processus actifs"""
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            info = proc.info
            info['memory'] = get_size(info['memory_info'].rss)
            del info['memory_info']
            processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return processes

@app.route("/processes")
def processes():
    """Endpoint API pour les processus"""
    try:
        return jsonify(get_processes())
    except Exception as e:
        logger.error(f"Erreur: {e}")
        return jsonify([]), 500
```

### 8.2 Backend - Terminaison de processus

```python
@app.route("/kill_process", methods=["POST"])
def kill_process():
    """Termine un processus par son PID"""
    try:
        data = request.get_json()

        if not data or 'pid' not in data:
            return jsonify({"success": False, "message": "PID manquant"}), 400

        pid = int(data.get("pid"))

        if not psutil.pid_exists(pid):
            return jsonify({"success": False, "message": "Processus inexistant"}), 404

        logger.info(f"Terminaison du processus PID: {pid}")

        process = psutil.Process(pid)
        process_name = process.name()

        process.terminate()

        try:
            process.wait(timeout=5)
            return jsonify({
                "success": True,
                "message": f"Processus '{process_name}' (PID: {pid}) terminé"
            })
        except psutil.TimeoutExpired:
            process.kill()
            return jsonify({
                "success": True,
                "message": f"Processus forcé à se terminer"
            })

    except psutil.AccessDenied:
        return jsonify({
            "success": False,
            "message": "Accès refusé. Privilèges administrateur requis."
        }), 403
    except Exception as e:
        logger.error(f"Erreur: {e}")
        return jsonify({"success": False, "message": str(e)}), 500
```

### 8.3 Frontend - Affichage des processus

```javascript
// Fonction de terminaison de processus
function killProcess(pid, name) {
  if (!confirm(`Terminer "${name}" (PID: ${pid}) ?\n\nCela peut causer une perte de données.`)) {
    return;
  }

  showToast(`Arrêt du processus ${pid} en cours...`, 'info');

  fetch('/kill_process', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ pid })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      showToast(data.message, 'success');
      setTimeout(() => $('#proc-tab').click(), 1500);
    } else {
      showToast(data.message, 'error');
    }
  });
}

// Chargement des processus
$('#proc-tab').on('shown.bs.tab', () => {
  loadTable('/processes', '#processesTable', [
    { data: 'pid' },
    { data: 'name' },
    {
      data: 'cpu_percent',
      render: function(data) {
        const percentage = parseFloat(data) || 0;
        let colorClass = 'text-success';
        if (percentage > 50) colorClass = 'text-warning';
        if (percentage > 80) colorClass = 'text-danger';
        return `<span class="${colorClass} fw-bold">${percentage.toFixed(1)}%</span>`;
      }
    },
    { data: 'memory' },
    {
      data: null,
      render: function(data, type, row) {
        return `<button class="btn btn-sm btn-danger" onclick="killProcess(${row.pid}, '${row.name}')" title="Terminer">
          <i class="bi bi-x-circle"></i> Tuer
        </button>`;
      }
    }
  ]);
});
```

![Monitoring des processus](images/processes-monitoring.png)
*Emplacement: `/images/tutoriels/helpdesk-info/processes-monitoring.png`*

**🎯 Fonctionnalités:**
- Mise en couleur selon l'utilisation CPU
- Confirmation avant terminaison
- Gestion des erreurs (accès refusé)

---

## 📄 Étape 9 : Export de rapports {#étape-9-export}

### 9.1 Fonction d'export

Dans `main.py`:

```python
@app.route("/export")
def export():
    """Génère et télécharge un rapport système"""
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
        logger.info(f"Export: {filename}")

        return send_file(
            file_buffer,
            as_attachment=True,
            download_name=filename,
            mimetype='text/plain'
        )

    except Exception as e:
        logger.error(f"Erreur export: {e}")
        return jsonify({"error": "Erreur lors de la génération"}), 500
```

![Exemple de rapport exporté](images/exported-report.png)
*Emplacement: `/images/tutoriels/helpdesk-info/exported-report.png`*

---

## 🔐 Étape 10 : Sécurité et production {#étape-10-production}

### 10.1 Gestionnaires d'erreurs

```python
@app.errorhandler(404)
def not_found(error):
    """Erreur 404"""
    return jsonify({"error": "Ressource non trouvée"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Erreur 500"""
    logger.error(f"Erreur serveur: {error}")
    return jsonify({"error": "Erreur interne du serveur"}), 500
```

### 10.2 Configuration pour la production

```python
if __name__ == "__main__":
    import webbrowser

    # Configuration
    HOST = "127.0.0.1"  # 0.0.0.0 pour accès réseau
    PORT = 5000
    DEBUG = False  # False en production !

    logger.info("=" * 60)
    logger.info("HelpDesk Info - Mode Production")
    logger.info(f"URL: http://{HOST}:{PORT}")
    logger.info("=" * 60)

    # Lancement
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
        threaded=True
    )
```

### 10.3 Checklist de sécurité

✅ **À faire avant la production:**

1. **Désactiver le mode debug**
   ```python
   DEBUG = False
   ```

2. **Utiliser un serveur WSGI**
   ```bash
   pip install waitress
   waitress-serve --host=127.0.0.1 --port=5000 main:app
   ```

3. **Logs sécurisés**
   - Ne jamais logger de mots de passe
   - Limiter la taille des logs

4. **Validation des entrées**
   - Tous les inputs utilisateur sont validés
   - Échappement des commandes shell

5. **HTTPS** (si accessible via réseau)
   - Certificat SSL/TLS
   - Redirection HTTP → HTTPS

---

## 📦 Compilation en exécutable {#compilation}

### 11.1 Installation de PyInstaller

```bash
pip install pyinstaller
```

### 11.2 Création du fichier de spec

Créez `main.spec`:

```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('templates', 'templates'), ('static', 'static')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='HelpDeskInfo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='HelpDeskInfo',
)
```

### 11.3 Compilation

```bash
pyinstaller main.spec
```

L'exécutable se trouve dans `dist/HelpDeskInfo/HelpDeskInfo.exe`

![Exécutable compilé](images/compiled-exe.png)
*Emplacement: `/images/tutoriels/helpdesk-info/compiled-exe.png`*

**✨ Avantages:**
- Aucune installation Python requise
- Distribution simplifiée
- Portable

---

## 🎓 Conclusion et prochaines étapes {#conclusion}

### Ce que nous avons accompli

🎉 **Félicitations!** Vous avez créé une application web professionnelle complète de diagnostic système avec:

✅ Interface web moderne et responsive
✅ Backend Flask robuste et sécurisé
✅ Collecte d'informations système
✅ Gestion des programmes et services
✅ Monitoring des processus
✅ Export de rapports
✅ Design professionnel avec animations
✅ Gestion d'erreurs complète
✅ Système de logs

### Améliorations possibles

🚀 **Pour aller plus loin:**

1. **Authentification utilisateur**
   - Flask-Login pour la gestion des sessions
   - Base de données SQLite pour les utilisateurs
   - Hash des mots de passe avec bcrypt

2. **Monitoring en temps réel**
   - WebSocket avec Flask-SocketIO
   - Graphiques en temps réel avec Chart.js
   - Alertes automatiques

3. **Multi-machines**
   - Agent à installer sur chaque PC
   - Dashboard centralisé
   - Gestion de parc informatique

4. **Export avancé**
   - PDF avec ReportLab
   - Excel avec openpyxl
   - Envoi par email automatique

5. **Support multi-OS**
   - Adaptation pour Linux
   - Support macOS
   - Interface unifiée

### Ressources supplémentaires

📚 **Pour approfondir:**

- [Documentation Flask officielle](https://flask.palletsprojects.com/)
- [Documentation psutil](https://psutil.readthedocs.io/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)
- [DataTables Documentation](https://datatables.net/)

### Support et code source

📦 **Projet complet disponible:**

- 🔗 GitHub: [https://github.com/LM-Code-Be/helpdesk-info](https://github.com/LM-Code-Be/helpdesk-info)
- 📧 Contact: [contact@lm-code.be](mailto:contact@lm-code.be)
- 🌐 Site: [lm-code.be](https://lm-code.be)

### Rejoignez la communauté

💬 **Partagez vos créations:**

- Partagez vos améliorations sur GitHub
- Créez une issue pour signaler un bug
- Proposez des Pull Requests
- Rejoignez les discussions

---

## 📝 Notes finales de l'auteur

Merci d'avoir suivi ce tutoriel jusqu'au bout! J'espère que vous avez appris des techniques utiles pour vos futurs projets.

N'hésitez pas à adapter ce projet à vos besoins spécifiques. Le code est libre (licence MIT) et vous pouvez le modifier comme bon vous semble.

Si vous avez des questions ou des suggestions d'amélioration, n'hésitez pas à me contacter à [contact@lm-code.be](mailto:contact@lm-code.be).

**Happy coding! 🚀**

---

**Michael - LM-Code**
Développeur Full Stack & Expert IT
🌐 [lm-code.be](https://lm-code.be)

---

## 🏷️ Tags et catégories

**Catégories:** Développement Web, Python, Administration Système, IT

**Tags:** #Python #Flask #Windows #Système #HelpDesk #WebDev #Tutorial #IT #PowerShell #Bootstrap

**Difficulté:** ⭐⭐⭐ Intermédiaire

**Dernière mise à jour:** 29 janvier 2025

---

*Cet article fait partie de la série "Développement d'applications IT professionnelles" sur LM-Code.be*
