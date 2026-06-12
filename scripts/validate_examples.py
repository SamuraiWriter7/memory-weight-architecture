#!/usr/bin/env python3
"""
Validate example YAML files against their corresponding JSON Schemas.

This script validates examples under examples/ against schemas under schemas/.
It supports both explicitly declared validation targets and automatic discovery
based on the naming convention:

examples/<name>.example.yaml
schemas/<name>.schema.json
"""

from **future** import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError, SchemaError

ROOT_DIR = Path(**file**).resolve().parents[1]
SCHEMAS_DIR = ROOT_DIR / "schemas"
EXAMPLES_DIR = ROOT_DIR / "examples"

@dataclass(frozen=True)
class ValidationTarget:
name: str
schema_path: Path
example_path: Path

EXPLICIT_TARGETS: list[ValidationTarget] = [
ValidationTarget(
name="Memory Weight Record",
schema_path=SCHEMAS_DIR / "memory-weight-record.schema.json",
example_path=EXAMPLES_DIR / "memory-weight-record.example.yaml",
),
]

def title_from_stem(stem: str) -> str:
"""Convert a file stem into a readable validation target name."""
return stem.replace("-", " ").replace("_", " ").title()

def discover_targets() -> list[ValidationTarget]:
"""
Discover validation targets using the standard naming convention.

```
Example:
  examples/memory-weight-record.example.yaml
  schemas/memory-weight-record.schema.json
"""
targets: list[ValidationTarget] = []

if not EXAMPLES_DIR.exists():
    return targets

for example_path in sorted(EXAMPLES_DIR.glob("*.example.yaml")):
    stem = example_path.name.removesuffix(".example.yaml")
    schema_path = SCHEMAS_DIR / f"{stem}.schema.json"

    if schema_path.exists():
        targets.append(
            ValidationTarget(
                name=title_from_stem(stem),
                schema_path=schema_path,
                example_path=example_path,
            )
        )

return targets
```

def merge_targets(
explicit_targets: Iterable[ValidationTarget],
discovered_targets: Iterable[ValidationTarget],
) -> list[ValidationTarget]:
"""
Merge explicit and discovered targets without duplicates.

```
Explicit targets are kept first so important validations remain visible
in the output.
"""
merged: list[ValidationTarget] = []
seen: set[tuple[Path, Path]] = set()

for target in list(explicit_targets) + list(discovered_targets):
    key = (target.schema_path.resolve(), target.example_path.resolve())

    if key in seen:
        continue

    seen.add(key)
    merged.append(target)

return merged
```

def load_json(path: Path) -> dict:
"""Load a JSON file."""
with path.open("r", encoding="utf-8") as file:
return json.load(file)

def load_yaml(path: Path) -> object:
"""Load a YAML file."""
with path.open("r", encoding="utf-8") as file:
return yaml.safe_load(file)

def validate_target(target: ValidationTarget) -> None:
"""Validate one example YAML file against one JSON Schema."""
print(f"Validating target: {target.name}")
print(f"Validating example: {target.example_path.relative_to(ROOT_DIR)}")
print(f"Using schema: {target.schema_path.relative_to(ROOT_DIR)}")

```
if not target.schema_path.exists():
    raise FileNotFoundError(f"Schema not found: {target.schema_path}")

if not target.example_path.exists():
    raise FileNotFoundError(f"Example not found: {target.example_path}")

schema = load_json(target.schema_path)
example = load_yaml(target.example_path)

Draft202012Validator.check_schema(schema)

validator = Draft202012Validator(
    schema=schema,
    format_checker=FormatChecker(),
)
validator.validate(example)

print("Validation passed.")
print()
```

def main() -> int:
"""Run all validations."""
targets = merge_targets(
explicit_targets=EXPLICIT_TARGETS,
discovered_targets=discover_targets(),
)

```
if not targets:
    print("No validation targets found.")
    return 1

failures: list[tuple[ValidationTarget, Exception]] = []

for target in targets:
    try:
        validate_target(target)
    except (ValidationError, SchemaError, FileNotFoundError, json.JSONDecodeError, yaml.YAMLError) as error:
        failures.append((target, error))

        print("Validation failed.")
        print(f"Target: {target.name}")
        print(f"Error: {error}")
        print()

if failures:
    print(f"{len(failures)} validation target(s) failed.")
    return 1

print(f"All validations passed. Total targets: {len(targets)}")
return 0
```

if **name** == "**main**":
sys.exit(main())
