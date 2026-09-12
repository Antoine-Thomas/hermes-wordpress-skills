# Hermes WordPress Skills

Collection de skills [Hermes Agent](https://hermes-agent.nousresearch.com/) pour développer, gérer et déployer des sites **WordPress** avec **Local by Flywheel**.

## Objectif

Fournir des skills prêts à l'emploi pour :

- Installer et configurer Local by Flywheel
- Créer et gérer des sites WordPress locaux
- Automatiser les tâches WP-CLI (mises à jour, plugins, thèmes, base de données)
- Sauvegarder et restaurer un site complet (fichiers + base de données)
- Déployer un site local vers un serveur distant (FTP/SFTP, SSH/rsync)

Chaque skill contient un `SKILL.md` (documentation), des scripts exécutables et des références.

## Skills disponibles

| Skill | Description | Scripts |
|-------|-------------|---------|
| [`local-flywheel-setup`](skills/local-flywheel-setup/) | Installation et configuration de Local by Flywheel, création du premier site | `install_local.py`, `configure_local.py`, `create_site.py`, `list_sites.py`, `manage_site.py` |
| [`wordpress-site-management`](skills/wordpress-site-management/) | Gestion complète des sites locaux (création, liste, suppression, plugins/thèmes) | `create_site.py`, `list_sites.py`, `delete_site.py`, `configure_site.py` |
| [`wp-cli-automation`](skills/wp-cli-automation/) | Automatisation WP-CLI : mises à jour, plugins, thèmes, export/import BDD | `update_plugins.py`, `update_themes.py`, `update_core.py`, `export_db.py`, `import_db.py`, `install_plugins.py` |
| [`wordpress-backup-restore`](skills/wordpress-backup-restore/) | Sauvegarde et restauration complètes (fichiers + base de données) | `backup_site.py`, `restore_site.py`, `list_backups.py` |
| [`wordpress-deployment`](skills/wordpress-deployment/) | Déploiement vers un serveur distant et migration d'URL | `deploy_ftp.py`, `deploy_ssh.py`, `sync_database.py`, `search_replace.py` |

## Prérequis

- [Hermes Agent](https://hermes-agent.nousresearch.com/) installé
- [Local by Flywheel](https://localwp.com/) installé
- [WP-CLI](https://make.wordpress.org/cli/handbook/) disponible dans le `PATH`
- Python 3.8+
- Git
- Optionnel : `lftp` (déploiement FTP), `rsync` + `ssh` (déploiement SSH)

## Installation

```bash
git clone https://github.com/Antoine-Thomas/hermes-wordpress-skills.git
cd hermes-wordpress-skills
```

Copier les skills dans votre dossier Hermes :

```bash
# Linux / macOS
cp -r skills/* ~/.config/hermes/skills/

# Windows (PowerShell)
Copy-Item -Recurse skills\* $env:LOCALAPPDATA\hermes\skills\
```

Configurer les variables d'environnement :

```bash
cp .env.example .env
# Éditer .env avec vos valeurs
```

## Utilisation

Créer un site WordPress local :

```bash
python skills/local-flywheel-setup/scripts/create_site.py --name "mon-site" --domain "mon-site.local"
```

Mettre à jour tous les plugins :

```bash
python skills/wp-cli-automation/scripts/update_plugins.py --site "mon-site"
```

Sauvegarder un site complet :

```bash
python skills/wordpress-backup-restore/scripts/backup_site.py --site "mon-site" --output "./backups" --compress
```

Déployer vers un serveur distant :

```bash
python skills/wordpress-deployment/scripts/deploy_ssh.py --site "mon-site" --host "user@server.com" --remote-path "/var/www/html"
```

Chaque script accepte `--help` pour la liste complète des options.

## Structure du dépôt

```
hermes-wordpress-skills/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── skills/
│   ├── local-flywheel-setup/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── references/
│   ├── wordpress-site-management/
│   ├── wp-cli-automation/
│   ├── wordpress-backup-restore/
│   └── wordpress-deployment/
├── templates/
│   └── skill-template/
└── .github/
    ├── workflows/validate-skills.yml
    └── scripts/validate_skills.py
```

## Contribuer

1. Fork le dépôt
2. Créer une branche : `git checkout -b feature/mon-skill`
3. Ajouter le skill dans `skills/` en suivant [`templates/skill-template`](templates/skill-template/)
4. Vérifier : `python .github/scripts/validate_skills.py`
5. Ouvrir une Pull Request

## Licence

MIT — voir [LICENSE](LICENSE).

## Liens

- [Hermes Agent — documentation](https://hermes-agent.nousresearch.com/docs)
- [Local by Flywheel](https://localwp.com/)
- [WP-CLI Handbook](https://make.wordpress.org/cli/handbook/)
- [WordPress Developer Resources](https://developer.wordpress.org/)

---

Maintenu par [Searching Murphy](https://github.com/Antoine-Thomas).
