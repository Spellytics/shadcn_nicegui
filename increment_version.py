#!/usr/bin/env python3
"""
Increment the patch version number in __init__.py and pyproject.toml
"""
import re
from pathlib import Path


def increment_patch_version(version: str) -> str:
    """Increment the patch version (e.g., 0.2.0 -> 0.2.1)"""
    major, minor, patch = map(int, version.split('.'))
    return f"{major}.{minor}.{patch + 1}"


def update_init_version(init_path: Path, new_version: str) -> None:
    """Update version in __init__.py"""
    content = init_path.read_text()
    updated = re.sub(
        r'__version__\s*=\s*["\'][\d.]+["\']',
        f'__version__ = "{new_version}"',
        content
    )
    init_path.write_text(updated)
    print(f"✓ Updated {init_path}: {new_version}")


def update_pyproject_version(pyproject_path: Path, new_version: str) -> None:
    """Update version in pyproject.toml"""
    content = pyproject_path.read_text()
    updated = re.sub(
        r'version\s*=\s*["\'][\d.]+["\']',
        f'version = "{new_version}"',
        content,
        count=1  # Only replace the first occurrence (in [project] section)
    )
    pyproject_path.write_text(updated)
    print(f"✓ Updated {pyproject_path}: {new_version}")


def main():
    # Get current version from __init__.py
    init_path = Path(__file__).parent / "shadcn_nicegui" / "__init__.py"
    pyproject_path = Path(__file__).parent / "pyproject.toml"

    if not init_path.exists():
        print(f"Error: {init_path} not found")
        return 1

    if not pyproject_path.exists():
        print(f"Error: {pyproject_path} not found")
        return 1

    # Extract current version
    init_content = init_path.read_text()
    match = re.search(r'__version__\s*=\s*["\']([\d.]+)["\']', init_content)

    if not match:
        print("Error: Could not find version in __init__.py")
        return 1

    current_version = match.group(1)
    new_version = increment_patch_version(current_version)

    print(f"Incrementing version: {current_version} → {new_version}")

    # Update both files
    update_init_version(init_path, new_version)
    update_pyproject_version(pyproject_path, new_version)

    print(f"\n✓ Version bumped to {new_version}")
    return 0


if __name__ == "__main__":
    exit(main())
