---
name: skill-template
description: Modele de base pour creer un nouveau skill Hermes WordPress
version: "1.0.0"
author: Searching Murphy
license: MIT
tags:
  - template
  - wordpress
  - hermes
---

# Skill Template

Modele de reference pour creer un skill WordPress compatible avec Hermes Agent.

## Structure attendue

```
mon-skill/
├── SKILL.md              # Metadonnees + documentation (ce fichier)
├── scripts/
│   ├── main_script.py    # Script principal
│   └── utils.py          # Fonctions partagees
└── references/
    └── doc.md            # Documentation, liens, API
```

## Frontmatter obligatoire

```yaml
---
name: mon-skill
description: Description courte du skill (une ligne)
version: "1.0.0"
author: Votre Nom
license: MIT
tags:
  - wordpress
  - autre-tag
---
```

Regles :

- `name` doit correspondre exactement au nom du dossier
- `description` tient en une ligne et commence par un verbe
- `version` suit le semver (`"1.0.0"`, entre guillemets pour rester une chaine)
- `tags` est une liste non vide

## Bonnes pratiques

1. Un skill = une responsabilite claire.
2. Chaque script est executable seul (`python script.py --help`).
3. `argparse` pour les arguments, jamais de saisie interactive obligatoire.
4. Gestion d'erreurs explicite : `try/except` + `sys.exit(1)` et message sur `stderr`.
5. Aucun secret dans le code : passer par `.env` / variables d'environnement.
6. Imports standard en haut du fichier (`platform`, `shutil`, `datetime`...), pas dans les fonctions.
7. Chemins multiplateformes avec `pathlib.Path`.
8. Documenter chaque script dans son docstring et dans le `SKILL.md`.

## Squelette de script

```python
#!/usr/bin/env python3
"""
Description du script.
"""

import argparse
import sys
from pathlib import Path


def run(param):
    """Fait le travail principal."""
    print(f"Traitement de {param}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Description du script")
    parser.add_argument("--param", required=True, help="Description du parametre")
    args = parser.parse_args()

    try:
        run(args.param)
    except Exception as exc:
        print(f"Erreur: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## Verification avant publication

```bash
python -m compileall -q skills
python .github/scripts/validate_skills.py
python .github/scripts/validate_structure.py
```

## Licence

MIT
