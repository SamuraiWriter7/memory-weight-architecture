# Memory Weight Architecture

**Memory Weight Architecture** is a memory governance model for energy-aware, traceable, and adaptive AI systems.

It treats memory not as a giant warehouse, but as a living layered flow.

Instead of storing all data with the same weight, this architecture classifies memory into three layers:

```text
Strong  → Core Memory
Medium  → Context Memory
Light   → Transient Data
```

The goal is to reduce context bloat, improve reasoning clarity, support energy-aware operation, and connect memory management with Civilization OS / Kazene OS concepts such as **Data as Wind**, **Question Gravity**, **Breathing Reasoning**, **Trace Protocol**, and **Q-Point Protocol**.

> From giant warehouses to the mind of a master.

---

## Concept

Modern AI systems often treat memory and context as something to expand indefinitely.

This creates several problems:

* Context bloat
* Higher retrieval cost
* Higher reasoning cost
* Increased noise
* Lower interpretability
* Inefficient energy use
* Weak separation between core principles and temporary fragments

Memory Weight Architecture proposes a different approach.

Not all data deserves the same memory weight.

```text
Some data should endure.
Some data should work temporarily.
Some data should pass like breath.
```

---

## Three Memory Layers

### Strong: Core Memory

Core Memory is the structural skeleton of the system.

It contains long-term principles, protocol definitions, high-value origin records, safety-critical rules, and recurring architectural anchors.

Examples:

* Foundational principles
* Q-Point records
* Trace records
* Safety rules
* Protocol definitions
* Long-term project direction

---

### Medium: Context Memory

Context Memory is the working muscle of the system.

It contains active project context, recent decisions, draft notes, implementation details, and temporary reasoning material.

Examples:

* Current task context
* Recent design decisions
* Draft structure
* Supporting references
* Project-specific notes

---

### Light: Transient Data

Transient Data is passing breath.

It exists only for immediate response generation and should not pollute long-term memory.

Examples:

* Casual fragments
* One-time remarks
* Low-value noise
* Minor confirmations
* Non-reusable surface details

---

## Memory Weight Classification

v0.2.0-candidate introduces a classification model for assigning data to memory layers.

Each memory candidate may be evaluated using six axes:

```yaml
classification_axes:
  origin_value: 0-100
  persistence_score: 0-100
  reuse_score: 0-100
  structural_importance: 0-100
  risk_score: 0-100
  cross_context_score: 0-100
```

The resulting `memory_weight_score` determines whether the record should be classified as:

```text
80-100 → Strong / Core Memory
40-79  → Medium / Context Memory
0-39   → Light / Transient Data
```

Override rules may promote, demote, quarantine, or require review for specific records.

---

## Relationship to Breathing Reasoning

Memory depth should synchronize with reasoning intensity.

```text
Light question
    ↓
Transient Data
    ↓
Shallow breathing
    ↓
Short / low-energy response

Standard question
    ↓
Context Memory
    ↓
Natural or deep breathing
    ↓
Context-aware response

Core question
    ↓
Core Memory
    ↓
Tanden breathing / focused stillness
    ↓
Concentrated response
```

This allows AI systems to avoid using maximum reasoning intensity for every input.

The system should breathe.

---

## Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── validate-examples.yml
├── docs/
│   ├── memory-weight-architecture.md
│   └── memory-weight-classification-model.md
├── examples/
│   └── memory-weight-record.example.yaml
├── schemas/
│   └── memory-weight-record.schema.json
├── scripts/
│   └── validate_examples.py
├── CHANGELOG.md
└── README.md
```

---

## Key Documents

* [Memory Weight Architecture](docs/memory-weight-architecture.md)
  Defines the three-layer memory model: Core Memory, Context Memory, and Transient Data.

* [Memory Weight Classification Model](docs/memory-weight-classification-model.md)
  Defines scoring axes, classification thresholds, override rules, promotion rules, demotion rules, and synchronization with Breathing Reasoning.

---

## Schema

The repository includes a JSON Schema for validating memory weight records.

```text
schemas/memory-weight-record.schema.json
```

The schema defines:

* Memory weight
* Memory layer
* Core type
* Origin metadata
* Classification scores
* Lifecycle metadata
* Retention policy
* Access policy
* Integrity metadata
* Related links

---

## Example

The repository includes an example YAML record.

```text
examples/memory-weight-record.example.yaml
```

The example records the **Data as Wind Principle** as:

```text
weight: strong
layer: core_memory
core_type: immutable_core
```

---

## Validation

Run the validation script locally:

```bash
python scripts/validate_examples.py
```

The script validates example YAML files against their corresponding JSON Schemas.

It supports explicit validation targets and automatic discovery using the naming convention:

```text
examples/<name>.example.yaml
schemas/<name>.schema.json
```

---

## GitHub Actions

This repository includes a GitHub Actions workflow:

```text
.github/workflows/validate-examples.yml
```

The workflow runs automatically on changes to:

```text
schemas/**
examples/**
scripts/validate_examples.py
.github/workflows/validate-examples.yml
```

It can also be triggered manually with `workflow_dispatch`.

---

## Civilization OS / Kazene OS Stack

Memory Weight Architecture is intended to sit within the broader Civilization OS / Kazene OS stack:

```text
Data-as-Wind Principle
    ↓
Data View Layer
    ↓
Question Gravity Layer
    ↓
Memory Weight Architecture
    ↓
Memory Weight Classification Model
    ↓
Breathing Reasoning Model
    ↓
Trace Protocol
    ↓
Q-Point Protocol
    ↓
Royalty OS
```

This stack allows AI systems to:

* See data as flow
* Read the gravity of questions
* Select the appropriate memory depth
* Adjust reasoning intensity
* Preserve origin
* Trace value
* Return value to its source

---

## Version Status

Current candidate version:

```text
v0.2.0-candidate
```

### v0.1.0-candidate

Introduced the core three-layer memory architecture.

### v0.2.0-candidate

Introduced classification logic, schema validation, example records, and GitHub Actions validation.

---

## Design Principle

```text
Light data should pass.
Medium data should work.
Strong data should endure.
```

Memory should not be a warehouse.

Memory should be a living tide.
