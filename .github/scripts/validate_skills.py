#!/usr/bin/env python3
"""
Valide les fichiers SKILL.md du depot : frontmatter YAML et champs obligatoires.
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML manquant : pip install pyyaml")
    sys.exit(1)

REQUIRED_FIELDS = ["name", "description", "version", "author", "license", "tags"]
KNOWN_LICENSES = ["MIT", "Apache-2.0", "GPL-3.0", "BSD-3-Clause"]
ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / "skills"


def validate_skill_md(file_path):
    """Retourne (errors, warnings) pour un SKILL.md."""
    errors, warnings = [], []

    try:
        content = file_path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"lecture impossible: {exc}"], []

    if not content.startswith("---"):
        return ["frontmatter YAML manquant (---)"], []

    parts = content.split("---", 2)
    if len(parts) < 3:
        return ["frontmatter YAML invalide"], []

    try:
        frontmatter = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        return [f"YAML invalide: {exc}"], []

    if not isinstance(frontmatter, dict):
        return ["frontmatter YAML n'est pas un mapping"], []

    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            errors.append(f"champ obligatoire manquant: {field}")
        elif frontmatter[field] in (None, "", [], {}):
            warnings.append(f"champ vide: {field}")

    name = frontmatter.get("name")
    if name and name != file_path.parent.name:
        warnings.append(f"name '{name}' != dossier '{file_path.parent.name}'")

    version = frontmatter.get("version")
    if version is not None and not str(version)[0].isdigit():
        warnings.append(f"version devrait commencer par un chiffre: {version}")

    tags = frontmatter.get("tags")
    if tags is not None:
        if not isinstance(tags, list):
            errors.append("tags doit etre une liste")
        elif not tags:
            warnings.append("tags est vide")

    license_value = frontmatter.get("license")
    if license_value and license_value not in KNOWN_LICENSES:
        warnings.append(f"licence inhabituelle: {license_value}")

    body = parts[2].strip()
    if len(body) < 200:
        warnings.append("corps du SKILL.md tres court (< 200 caracteres)")

    return errors, warnings


def main():
    print(f"Validation des SKILL.md dans {SKILLS_DIR}")

    if not SKILLS_DIR.exists():
        print(f"ERREUR: dossier skills introuvable: {SKILLS_DIR}")
        sys.exit(1)

    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir() and not d.name.startswith("."))
    if not skill_dirs:
        print("ERREUR: aucun skill trouve")
        sys.exit(1)

    total_errors, total_warnings = 0, 0

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            print(f"  x {skill_dir.name}: SKILL.md manquant")
            total_errors += 1
            continue

        errors, warnings = validate_skill_md(skill_file)
        total_errors += len(errors)
        total_warnings += len(warnings)

        if not errors and not warnings:
            print(f"  ok {skill_dir.name}")
        else:
            for err in errors:
                print(f"  x {skill_dir.name}: {err}")
            for warn in warnings:
                print(f"  ! {skill_dir.name}: {warn}")

    print(f"\n{len(skill_dirs)} skill(s) verifie(s) - erreurs: {total_errors} - avertissements: {total_warnings}")

    if total_errors:
        print("Validation ECHOUEE")
        sys.exit(1)

    print("Validation REUSSIE")


if __name__ == "__main__":
    main()
