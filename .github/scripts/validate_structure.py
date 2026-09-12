#!/usr/bin/env python3
"""
Valide la structure du depot : dossiers obligatoires, scripts et references par skill.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / "skills"

REQUIRED_ROOT_ITEMS = ["README.md", "LICENSE", ".gitignore", ".env.example"]
REQUIRED_SKILL_ITEMS = ["SKILL.md", "scripts", "references"]


def validate():
    errors, warnings = [], []

    for item in REQUIRED_ROOT_ITEMS:
        if not (ROOT / item).exists():
            errors.append(f"element racine manquant: {item}")

    if not (ROOT / ".github" / "workflows").exists():
        errors.append("dossier .github/workflows manquant")

    if not SKILLS_DIR.exists():
        return ["dossier skills manquant"], warnings

    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir() and not d.name.startswith("."))
    if not skill_dirs:
        errors.append("aucun skill dans skills/")

    for skill_dir in skill_dirs:
        for item in REQUIRED_SKILL_ITEMS:
            target = skill_dir / item
            if not target.exists():
                errors.append(f"{skill_dir.name}: {item} manquant")

        scripts_dir = skill_dir / "scripts"
        if scripts_dir.exists():
            scripts = list(scripts_dir.glob("*.py"))
            if not scripts:
                warnings.append(f"{skill_dir.name}: aucun script Python")
            for script in scripts:
                if not script.read_text(encoding="utf-8", errors="ignore").startswith("#!"):
                    warnings.append(f"{skill_dir.name}/{script.name}: shebang manquant")

        refs_dir = skill_dir / "references"
        if refs_dir.exists() and not any(refs_dir.iterdir()):
            warnings.append(f"{skill_dir.name}: references/ vide")

    template = ROOT / "templates" / "skill-template"
    if not template.exists():
        warnings.append("template de skill manquant")
    elif not (template / "SKILL.md").exists():
        warnings.append("templates/skill-template/SKILL.md manquant")

    return errors, warnings


def main():
    print(f"Validation de la structure du depot: {ROOT}")
    errors, warnings = validate()

    for err in errors:
        print(f"  x {err}")
    for warn in warnings:
        print(f"  ! {warn}")

    print(f"\nerreurs: {len(errors)} - avertissements: {len(warnings)}")

    if errors:
        print("Validation ECHOUEE")
        sys.exit(1)

    print("Validation REUSSIE")


if __name__ == "__main__":
    main()
