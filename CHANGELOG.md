# Changelog - HelpDesk Info

Développé par Michael - LM-Code (https://lm-code.be)

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [1.0.0] - 2025-01-29

**🎉 Première version publique - Production Ready**

### ✨ Ajouté
- Interface web moderne avec design professionnel
- Système de diagnostic complet des informations système
- Gestion des programmes installés avec désinstallation à distance
- Contrôle des services Windows (démarrer/arrêter/redémarrer)
- Monitoring des processus avec terminaison à distance
- Export de rapports système au format texte
- Système de notifications toast élégantes
- Interface responsive (mobile, tablette, desktop)
- Icônes Bootstrap Icons pour une meilleure UX
- Tables interactives avec DataTables (tri, recherche, pagination)
- Animations CSS modernes et dégradés de couleurs
- Système de logging complet
- Gestion d'erreurs robuste pour la production
- Documentation complète (README, LICENSE, CHANGELOG)
- Script de démarrage automatique (start.bat)
- Configuration PyInstaller pour compilation en .exe

### 🎨 Design
- Palette de couleurs professionnelle (bleu/violet)
- Animations de chargement et transitions fluides
- Scrollbar personnalisée
- Headers avec effets de shimmer
- Badges de statut colorés
- Confirmations avant actions critiques

### 🔒 Sécurité
- Échappement des entrées utilisateur
- Protection contre l'injection de commandes
- Timeouts sur les opérations longues
- Gestion des permissions et accès refusés
- Logs de sécurité pour toutes les actions critiques

### 📚 Documentation
- README.md complet avec guide d'installation
- Documentation des endpoints API
- Guide de compilation en exécutable
- Section de dépannage
- Commentaires de code détaillés et humanisés

### 🛠️ Technique
- Flask 3.0+ avec configuration production-ready
- psutil pour le monitoring système
- PowerShell integration pour gestion avancée
- Support des requêtes simultanées (threaded)
- Gestionnaires d'erreurs 404/500
- Récupération IP publique avec timeout
- Déduplication automatique des programmes

---

## [Unreleased]

### 🎯 À venir dans les prochaines versions
- [ ] Système d'authentification utilisateur
- [ ] Support multi-langue (FR/EN)
- [ ] Monitoring en temps réel avec WebSocket
- [ ] Export PDF et Excel
- [ ] Dashboard de statistiques
- [ ] Mode sombre automatique
- [ ] API REST complète avec documentation Swagger
- [ ] Support Linux/MacOS
- [ ] Base de données pour historique
- [ ] Notifications par email
- [ ] Planification de tâches
- [ ] Gestion multi-machines

---

## Format des versions

- **[Major]** : Changements incompatibles avec les versions précédentes
- **[Minor]** : Ajout de fonctionnalités rétro-compatibles
- **[Patch]** : Corrections de bugs rétro-compatibles

### Catégories de changements
- **Ajouté** : Nouvelles fonctionnalités
- **Modifié** : Changements dans les fonctionnalités existantes
- **Déprécié** : Fonctionnalités bientôt supprimées
- **Supprimé** : Fonctionnalités retirées
- **Corrigé** : Corrections de bugs
- **Sécurité** : Corrections de vulnérabilités
