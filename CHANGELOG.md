# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-based versioning style during early specification development.

---

## v0.4.0-candidate

### Added

* Added `docs/breathing-reasoning-model.md`.

  * Defines Breathing Reasoning Model.

  * Connects memory weight to reasoning intensity.

  * Introduces the principle:

    ```text
    Reasoning intensity should follow question gravity and memory weight.
    ```

  * Defines five reasoning modes:

    * Shallow Breathing
    * Natural Breathing
    * Deep Breathing
    * Tanden Breathing
    * Focused Stillness

* Added reasoning-memory synchronization model:

  ```text
  Question Gravity        Memory Layer              Breathing Mode
  ----------------------------------------------------------------
  Low                     Transient Data            Shallow Breathing
  Medium-Low              Context Memory            Natural Breathing
  Medium-High             Context + Evolvable Core  Deep Breathing
  High                    Core Memory               Tanden Breathing
  Critical                Immutable Core / Trace    Focused Stillness
  ```

* Added energy-aware reasoning model.

  * Light questions use light memory access and low-energy reasoning.
  * Core questions justify deeper memory access and focused reasoning.
  * Critical questions trigger high-integrity reasoning and trace requirements.

* Added warning rule for high-gravity questions with insufficient memory access.

  * If core-level reasoning is required but only transient or context-level memory is available, the system should mark its response as limited.

* Added Trace requirement mapping by breathing mode:

  * Shallow Breathing: no trace required
  * Natural Breathing: no trace required
  * Deep Breathing: optional trace
  * Tanden Breathing: recommended trace
  * Focused Stillness: trace required

* Added `schemas/breathing-reasoning-event.schema.json`.

  * Defines a validation-ready structure for Breathing Reasoning Events.
  * Supports validation of:

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

* Added `examples/breathing-reasoning-event.example.yaml`.

  * Provides a concrete example of a high-gravity question selecting Tanden Breathing.
  * Demonstrates how Core Memory, Q-Point context, and focused structural reasoning can be synchronized.

### Changed

* Expanded the project from origin-aware memory governance into reasoning-memory synchronization.
* Updated `README.md` to reflect v0.4.0-candidate structure.
* Added Breathing Reasoning Model to the Civilization OS / Kazene OS stack.
* Extended schema/example validation to include Breathing Reasoning Event records through automatic discovery.
* Fixed `examples/q-point-memory-link.example.yaml`.
* Fixed `examples/breathing-reasoning-event.example.yaml`.

### Validation

* Confirmed that the following examples can be validated against their corresponding schemas through the validation script and GitHub Actions workflow:

  * `examples/memory-weight-record.example.yaml`
  * `examples/q-point-memory-link.example.yaml`
  * `examples/breathing-reasoning-event.example.yaml`

---

## v0.3.0-candidate

### Added

* Added `docs/q-point-memory-weight-integration.md`.

  * Defines how Q-Point values influence Memory Weight classification.

  * Connects question-origin value to memory governance.

  * Introduces the principle:

    ```text
    Question value influences memory weight.
    ```

  * Defines the flow:

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

* Added Q-Point to Memory Weight mapping:

  * `origin_strength` → `origin_value`
  * `question_depth` → `persistence_score`
  * `tension_score` → `structural_importance`
  * `resonance_score` → `cross_context_score`
  * `risk_sensitivity` → `risk_score`
  * `reuse_potential` → `reuse_score`

* Added Q-Point-derived memory scoring model:

  * `q_point_memory_score`
  * `integrated_memory_weight_score`

* Added Q-Point override rules for:

  * High-origin questions
  * Structural tension anchors
  * Cross-context resonance
  * Low-origin low-reuse fragments
  * High-risk Q-Points requiring review

* Added Trace Protocol integration rules for Q-Point-linked Core Memory promotion.

* Added Royalty OS integration pathway:

  * Q-Point
  * Memory Weight Record
  * Trace Record
  * Derived Output
  * Royalty / Return Route

* Added `schemas/q-point-memory-link.schema.json`.

  * Defines a validation-ready structure for linking Q-Point Records to Memory Weight Records.
  * Supports validation of:

    * Q-Point identifiers
    * Memory record identifiers
    * Q-Point-derived scores
    * Integrated memory influence
    * Final memory layer
    * Decision records
    * Trace requirements
    * Royalty relevance
    * Related links

* Added `examples/q-point-memory-link.example.yaml`.

  * Provides a concrete example of a Q-Point-linked Memory Weight Record.
  * Demonstrates how the Data as Wind Principle can be reinforced by Q-Point scores and preserved as Core Memory.

### Changed

* Expanded the project from memory classification into origin-aware memory governance.
* Updated `README.md` to reflect v0.3.0-candidate structure.
* Added Q-Point Memory Weight Integration to the Civilization OS / Kazene OS stack.
* Extended schema/example validation to include Q-Point Memory Link records through automatic discovery.

### Validation

* Confirmed that the Q-Point Memory Link example can be validated against the Q-Point Memory Link schema through the validation script and GitHub Actions workflow.

---

## v0.2.0-candidate

### Added

* Added `docs/memory-weight-classification-model.md`.

  * Defines automatic memory classification logic.
  * Introduces six classification axes:

    * `origin_value`
    * `persistence_score`
    * `reuse_score`
    * `structural_importance`
    * `risk_score`
    * `cross_context_score`
  * Defines `memory_weight_score`.
  * Defines classification thresholds for:

    * Strong / Core Memory
    * Medium / Context Memory
    * Light / Transient Data
  * Adds override rules for:

    * Safety-critical records
    * High-origin anchors
    * Repeated cross-context use
    * Low-value noise
    * High-risk uncertain records
  * Adds promotion and demotion rules.
  * Adds Core Memory subtypes:

    * Immutable Core
    * Evolvable Core
  * Adds synchronization rules with Breathing Reasoning.

* Added `schemas/memory-weight-record.schema.json`.

  * Defines a JSON Schema for Memory Weight Records.
  * Supports validation of:

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

* Added `examples/memory-weight-record.example.yaml`.

  * Provides a concrete example of a Strong / Core Memory record.
  * Uses the Data as Wind Principle as an Immutable Core example.

* Added `scripts/validate_examples.py`.

  * Validates YAML examples against JSON Schemas.
  * Supports explicit validation targets.
  * Supports automatic target discovery based on:

    * `examples/<name>.example.yaml`
    * `schemas/<name>.schema.json`

* Added `.github/workflows/validate-examples.yml`.

  * Runs schema/example validation on GitHub Actions.
  * Triggers on changes to:

    * `schemas/**`
    * `examples/**`
    * `scripts/validate_examples.py`
    * `.github/workflows/validate-examples.yml`
  * Supports manual execution via `workflow_dispatch`.

### Changed

* Extended the project from a conceptual memory architecture into a validation-ready specification.
* Clarified the relationship between Memory Weight Architecture and Breathing Reasoning.
* Added a stronger implementation pathway for Civilization OS / Kazene OS integration.
* Updated `README.md` to reflect v0.2.0-candidate structure, validation workflow, schema, example, and repository layout.

### Validation

* Confirmed that the Memory Weight Record example can be validated against the Memory Weight Record schema through the validation script and GitHub Actions workflow.

---

## v0.1.0-candidate

### Added

* Added `docs/memory-weight-architecture.md`.

  * Introduces Memory Weight Architecture.
  * Defines the three-layer memory model:

    * Strong / Core Memory
    * Medium / Context Memory
    * Light / Transient Data
  * Defines memory as a living layered flow rather than a giant warehouse.
  * Connects memory depth with reasoning intensity.
  * Introduces the concept of memory as:

    * Skeleton
    * Muscle
    * Breath

### Core Concept

v0.1.0-candidate established the foundational principle:

```text
Not all data deserves the same memory weight.
```

It introduced the basic model:

```text
Strong memory remains as skeleton.
Medium memory moves as muscle.
Light memory passes as breath.
```

### Relationship to Civilization OS

* Positioned Memory Weight Architecture as a foundational layer of Civilization OS / Kazene OS.
* Connected the model to:

  * Data-as-Wind Principle
  * Question Gravity Layer
  * Breathing Reasoning Model
  * Trace Protocol
  * Q-Point Protocol
  * Royalty OS

---

## Roadmap

### v0.5.0-candidate

Potential next additions:

* Trace-linked memory promotion audit
* Memory review protocol
* Archive Layer
* Frozen Trace
* Historical Memory
* Promotion / Demotion audit log schema

### v0.6.0-candidate

Potential next additions:

* Royalty OS integration
* Origin attribution event schema
* Memory-to-value route model
* Return route integration
* Contribution weighting model

### v1.0.0

Potential stabilization goals:

* Stable Memory Weight Record schema
* Stable Q-Point Memory Link schema
* Stable Breathing Reasoning Event schema
* Stable validation workflow
* Formal classification algorithm
* Complete documentation stack
* Compatibility with Trace Protocol, Q-Point Protocol, Breathing Reasoning, and Royalty OS

