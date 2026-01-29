# 🖥️ HelpDesk Info - Diagnostic PC Professionnel

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Flask](https://img.shields.io/badge/flask-3.0+-red.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

Application web professionnelle de diagnostic système pour techniciens IT. Interface moderne permettant la collecte d'informations système, la gestion des programmes, le contrôle des services Windows et le monitoring des processus.

**👨‍💻 Développé par:** Michael - [LM-Code](https://lm-code.be)
**📧 Contact:** [contact@lm-code.be](mailto:contact@lm-code.be)
**🌐 Site web:** [lm-code.be](https://lm-code.be)
**📦 GitHub:** [LM-Code-Be/helpdesk-info](https://github.com/LM-Code-Be/helpdesk-info)

---

## ✨ Fonctionnalités principales

- 📊 **Diagnostic système complet** - CPU, RAM, Disques, Réseau, IP publique/locale
- 💾 **Gestion des programmes** - Liste et désinstallation à distance
- ⚙️ **Contrôle des services Windows** - Démarrer/Arrêter/Redémarrer
- 🔄 **Monitoring des processus** - Visualisation et terminaison
- 📁 **Export de rapports** - Génération de rapports système au format texte
- 🎨 **Interface moderne** - Design professionnel avec animations et icônes Bootstrap
- 🔔 **Notifications toast** - Retours visuels élégants pour chaque action

---

## 🚀 Installation rapide

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/LM-Code-Be/helpdesk-info.git
cd helpdesk-info
```

### 2️⃣ Créer l'environnement virtuel

```bash
# Créer l'environnement
python -m venv venv

# Activer l'environnement (Windows)
venv\Scripts\activate

# Activer l'environnement (Linux/MacOS)
source venv/bin/activate
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4️⃣ Lancer l'application

```bash
python main.py
```

L'application s'ouvre automatiquement dans votre navigateur à l'adresse `http://127.0.0.1:5000`

**⚠️ Note:** Certaines fonctionnalités requièrent des privilèges administrateur (gestion des services, désinstallation de programmes).

---

## 📁 Structure du projet

```
helpdesk-info/
│
├── main.py                 # Application Flask principale
├── requirements.txt        # Dépendances Python
├── start.bat              # Script de démarrage Windows
├── README.md              # Ce fichier
├── TUTORIEL.md            # Tutoriel complet de développement
├── CHANGELOG.md           # Historique des versions
├── LICENSE                # Licence MIT
├── .gitignore             # Fichiers exclus du versioning
│
├── static/
│   └── style.css          # Styles CSS personnalisés
│
└── templates/
    └── index.html         # Interface web principale
```

---

## 🛠️ Technologies utilisées

### Backend
- **Flask 3.0+** - Framework web Python
- **psutil** - Monitoring système (CPU, RAM, processus)
- **requests** - Récupération IP publique
- **winreg** - Accès au registre Windows
- **subprocess** - Exécution de commandes PowerShell

### Frontend
- **Bootstrap 5.3.2** - Framework CSS responsive
- **Bootstrap Icons** - Bibliothèque d'icônes modernes
- **DataTables** - Tables interactives avec tri et recherche
- **jQuery** - Manipulation DOM et requêtes AJAX

---

## 💻 Utilisation

### Interface

L'application propose 4 onglets principaux:

1. **Infos Système** - Vue d'ensemble complète du système + formulaire de signalement
2. **Programmes** - Liste des applications installées avec option de désinstallation
3. **Services** - Gestion des services Windows (Start/Stop/Restart)
4. **Processus** - Monitoring et terminaison des processus actifs

### Fonctionnalités avancées

- **Export de rapport** - Télécharge un fichier `.txt` avec toutes les informations système
- **Recherche et tri** - Toutes les tables sont triables et recherchables
- **Notifications en temps réel** - Retours visuels pour chaque action
- **Confirmations** - Demandes de confirmation avant actions critiques

---

## 🔧 Configuration

### Changer le port

Éditez `main.py` ligne 540:

```python
HOST = "127.0.0.1"  # Modifier pour "0.0.0.0" pour accès réseau
PORT = 5000         # Modifier le port si nécessaire
DEBUG = True        # Mettre False en production
```

### Mode Production

Pour un déploiement en production:

1. Désactiver le mode debug dans `main.py`:
   ```python
   DEBUG = False
   ```

2. Utiliser un serveur WSGI (recommandé):
   ```bash
   pip install waitress
   waitress-serve --host=127.0.0.1 --port=5000 main:app
   ```

---

## 📦 Compilation en exécutable

Pour créer un fichier `.exe` standalone (sans installation Python):

```bash
# Installer PyInstaller
pip install pyinstaller

# Compiler l'application
pyinstaller --onefile --noconsole --add-data "templates;templates" --add-data "static;static" --name HelpDeskInfo main.py
```

L'exécutable se trouve dans `dist/HelpDeskInfo.exe`

---

## 🔒 Sécurité

### Avertissements

- ⚠️ **Privilèges administrateur requis** pour certaines fonctionnalités
- ⚠️ **Accès local uniquement** par défaut (`127.0.0.1`)
- ⚠️ **Environnement contrôlé** - Outil destiné aux techniciens IT

### Bonnes pratiques

- Ne jamais exposer sur Internet sans authentification et HTTPS
- Exécuter avec les privilèges minimum nécessaires
- Vérifier régulièrement les logs (`helpdesk.log`)
- Valider toutes les actions critiques

---

## 📝 Prérequis

- **Système d'exploitation:** Windows 10/11
- **Python:** 3.8 ou supérieur
- **PowerShell:** 5.0+ (inclus dans Windows 10/11)
- **Navigateur:** Chrome, Edge, Firefox (moderne)

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer:

1. Fork le projet
2. Créez une branche (`git checkout -b feature/amelioration`)
3. Committez vos changements (`git commit -m 'Ajout fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrez une Pull Request

---

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

```
Copyright (c) 2025 Michael - LM-Code
```

---

## 📞 Support & Contact

**Michael - LM-Code**
Développeur Full Stack & Expert IT

- 🌐 **Site web:** [lm-code.be](https://lm-code.be)
- 📧 **Email:** [contact@lm-code.be](mailto:contact@lm-code.be)
- 💼 **GitHub:** [@LM-Code-Be](https://github.com/LM-Code-Be)
- 🐛 **Issues:** [GitHub Issues](https://github.com/LM-Code-Be/helpdesk-info/issues)

Pour un tutoriel complet de développement, consultez [TUTORIEL.md](TUTORIEL.md)

---

## 🙏 Remerciements

- [Flask](https://flask.palletsprojects.com/) - Framework web Python
- [Bootstrap](https://getbootstrap.com/) - Framework CSS
- [psutil](https://github.com/giampaolo/psutil) - Monitoring système
- [DataTables](https://datatables.net/) - Tables interactives
- La communauté open-source

---

<div align="center">

**⭐ Si ce projet vous est utile, n'hésitez pas à lui donner une étoile sur GitHub ! ⭐**

Développé avec ❤️ par [Michael - LM-Code](https://lm-code.be)

[⬆ Retour en haut](#-helpdesk-info---diagnostic-pc-professionnel)

</div>
