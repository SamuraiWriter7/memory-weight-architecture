# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-based versioning style during early specification development.

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

### v0.3.0-candidate

Potential next additions:

* Archive Layer
* Frozen Trace
* Historical Memory
* Memory Review Protocol
* Promotion / Demotion audit log schema
* Breathing Reasoning schema
* Question Gravity schema

### v1.0.0

Potential stabilization goals:

* Stable Memory Weight Record schema
* Stable validation workflow
* Formal classification algorithm
* Complete documentation stack
* Compatibility with Trace Protocol and Q-Point Protocol
