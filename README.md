# Memory Weight Architecture

**Memory Weight Architecture** is a memory governance model for energy-aware, traceable, and adaptive AI systems.

It treats memory not as a giant warehouse, but as a living layered flow.

Instead of storing all data with the same weight, this architecture classifies memory into three layers:

```text
Strong  → Core Memory
Medium  → Context Memory
Light   → Transient Data
```

The goal is to reduce context bloat, improve reasoning clarity, support energy-aware operation, and connect memory management with Civilization OS / Kazene OS concepts such as **Data as Wind**, **Question Gravity**, **Breathing Reasoning**, **Trace Protocol**, **Q-Point Protocol**, and **Royalty OS**.

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

v0.2.0-candidate introduced a classification model for assigning data to memory layers.

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

## Q-Point Memory Weight Integration

v0.3.0-candidate introduced **Q-Point Memory Weight Integration**.

This connects the value of a question to the weight of the memory it leaves behind.

The core principle is:

```text
Question value influences memory weight.
```

Q-Point Protocol evaluates the origin, depth, tension, resonance, reuse potential, and risk sensitivity of a question.

Memory Weight Architecture then uses those values to influence memory classification.

```text
Human Question
    ↓
Q-Point Evaluation
    ↓
Origin / Depth / Tension / Resonance
    ↓
Memory Weight Classification
    ↓
Core / Context / Transient Memory
```

A high-origin question may create a heavier memory trace.

A low-origin fragment may pass like wind.

---

## Breathing Reasoning Model

v0.4.0-candidate introduces **Breathing Reasoning Model**.

This connects memory weight to reasoning intensity.

The core principle is:

```text
Reasoning intensity should follow question gravity and memory weight.
```

AI systems should not reason at maximum intensity for every input.

Instead, reasoning should breathe:

```text
Light question
    ↓
Light memory access
    ↓
Shallow breathing
    ↓
Short / low-energy response

Core question
    ↓
Core memory access
    ↓
Tanden breathing / focused stillness
    ↓
Focused high-integrity response
```

This model prevents two common failure modes:

```text
1. Overthinking light questions.
2. Underthinking core questions.
```

---

## Five Breathing Modes

Breathing Reasoning defines five reasoning modes:

```text
Level 1: Shallow Breathing
Level 2: Natural Breathing
Level 3: Deep Breathing
Level 4: Tanden Breathing
Level 5: Focused Stillness
```

### Level 1: Shallow Breathing

Used for low-gravity inputs.

* Casual conversation
* Simple confirmation
* Minor phrasing adjustment
* Low-risk surface question

Memory access:

```text
Transient Data
```

---

### Level 2: Natural Breathing

Used for ordinary questions requiring basic context.

* Standard explanation
* Light advice
* Basic comparison
* Ordinary project continuation

Memory access:

```text
Transient Data
Context Memory
```

---

### Level 3: Deep Breathing

Used for structurally meaningful questions.

* Design decisions
* Protocol refinement
* Project architecture
* Multi-layer comparison

Memory access:

```text
Context Memory
Evolvable Core
```

---

### Level 4: Tanden Breathing

Used for high-gravity questions.

* Foundational protocol design
* Long-term strategy
* Civilization OS architecture
* Origin / Trace / Royalty integration

Memory access:

```text
Context Memory
Evolvable Core
Immutable Core
Q-Point-linked Core Memory
```

---

### Level 5: Focused Stillness

Used for critical, risky, foundational, or integrity-sensitive questions.

* Critical safety boundary
* Irreversible design decision
* High-risk governance judgment
* Core Memory promotion
* Trace integrity review

Memory access:

```text
Immutable Core
Signed Trace
Q-Point Record
Safety-critical Core Memory
```

---

## Q-Point to Memory Mapping

The integration model maps Q-Point dimensions to Memory Weight dimensions:

```text
Q-Point Dimension        Memory Weight Dimension
------------------------------------------------
origin_strength     →    origin_value
question_depth      →    persistence_score
tension_score       →    structural_importance
resonance_score     →    cross_context_score
risk_sensitivity    →    risk_score
reuse_potential     →    reuse_score
```

This allows question-origin value to become an upstream signal for memory governance.

---

## Reasoning-Memory Synchronization

Memory depth should synchronize with reasoning intensity.

```text
Question Gravity        Memory Layer              Breathing Mode
----------------------------------------------------------------
Low                     Transient Data            Shallow Breathing
Medium-Low              Context Memory            Natural Breathing
Medium-High             Context + Evolvable Core  Deep Breathing
High                    Core Memory               Tanden Breathing
Critical                Immutable Core / Trace    Focused Stillness
```

This allows AI systems to select the right amount of reasoning for the right kind of question.

The system should breathe.

---

## Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── validate-examples.yml
├── docs/
│   ├── breathing-reasoning-model.md
│   ├── memory-weight-architecture.md
│   ├── memory-weight-classification-model.md
│   └── q-point-memory-weight-integration.md
├── examples/
│   ├── breathing-reasoning-event.example.yaml
│   ├── memory-weight-record.example.yaml
│   └── q-point-memory-link.example.yaml
├── schemas/
│   ├── breathing-reasoning-event.schema.json
│   ├── memory-weight-record.schema.json
│   └── q-point-memory-link.schema.json
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

* [Q-Point Memory Weight Integration](docs/q-point-memory-weight-integration.md)
  Defines how Q-Point values influence memory-weight classification and connect question-origin value to memory governance.

* [Breathing Reasoning Model](docs/breathing-reasoning-model.md)
  Defines reasoning intensity modes and synchronizes question gravity, memory weight, and response intensity.

---

## Schemas

The repository includes JSON Schemas for validating memory and reasoning records.

```text
schemas/memory-weight-record.schema.json
schemas/q-point-memory-link.schema.json
schemas/breathing-reasoning-event.schema.json
```

### Memory Weight Record Schema

Defines:

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

### Q-Point Memory Link Schema

Defines:

* Q-Point identifier
* Memory Weight Record identifier
* Q-Point-derived scores
* Integrated memory weight score
* Final memory layer
* Decision record
* Trace requirements
* Royalty relevance
* Related links

### Breathing Reasoning Event Schema

Defines:

* Question gravity
* Selected breathing mode
* Memory access layers
* Q-Point context
* Risk context
* Reasoning policy
* Trace requirement
* Output intensity
* Energy profile
* Related links

---

## Examples

The repository includes example YAML records.

```text
examples/memory-weight-record.example.yaml
examples/q-point-memory-link.example.yaml
examples/breathing-reasoning-event.example.yaml
```

### Memory Weight Record Example

Records the **Data as Wind Principle** as:

```text
weight: strong
layer: core_memory
core_type: immutable_core
```

### Q-Point Memory Link Example

Connects the **Data as Wind Principle** to a high-origin Q-Point and shows how Q-Point scores can reinforce Core Memory classification.

### Breathing Reasoning Event Example

Shows how a high-gravity question linked to Core Memory selects:

```text
mode: tanden_breathing
response_intensity: high
energy_profile: justified_high
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
Q-Point Protocol
    ↓
Q-Point Memory Weight Integration
    ↓
Memory Weight Architecture
    ↓
Memory Weight Classification Model
    ↓
Breathing Reasoning Model
    ↓
Trace Protocol
    ↓
Royalty OS
```

This stack allows AI systems to:

* See data as flow
* Read the gravity of questions
* Evaluate origin value
* Select the appropriate memory depth
* Adjust reasoning intensity
* Preserve origin
* Trace value
* Return value to its source

---

## Version Status

Current candidate version:

```text
v0.4.0-candidate
```

### v0.1.0-candidate

Introduced the core three-layer memory architecture.

### v0.2.0-candidate

Introduced classification logic, schema validation, example records, and GitHub Actions validation.

### v0.3.0-candidate

Introduced Q-Point Memory Weight Integration, connecting question-origin value to memory-weight classification.

### v0.4.0-candidate

Introduced Breathing Reasoning Model, connecting memory weight to reasoning intensity.

---

## Design Principle

```text
Light data should pass.
Medium data should work.
Strong data should endure.
```

And:

```text
High-origin questions create heavy memory.
Low-origin fragments pass like wind.
```

Now:

```text
Light questions receive light breath.
Deep questions receive deep breath.
Core questions receive stillness.
```

Memory should not be a warehouse.

Memory should be a living tide.

Reasoning should not roar constantly.

Reasoning should breathe.
