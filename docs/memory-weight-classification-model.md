# Memory Weight Classification Model

## 記憶重み分類モデル Specification v0.2.0-candidate

## 1. Overview

**Memory Weight Classification Model** defines how data should be automatically classified into the three layers introduced by **Memory Weight Architecture v0.1**.

Memory Weight Architecture v0.1 defines the three-layer memory structure:

```text
Strong  → Core Memory
Medium  → Context Memory
Light   → Transient Data
```

This document defines how a system determines which layer a given data item should belong to.

The goal is to prevent uniform memory storage, reduce context bloat, lower reasoning cost, and synchronize memory access with **Breathing Reasoning**.

In this model, data is not stored simply because it exists.
Data is stored only when its origin, persistence, reuse value, risk, and structural importance justify its weight.

---

## 2. Design Principle

The core principle is:

```text
Memory weight should be determined by structure, not by volume.
```

A long document may be light if it has low structural value.
A single sentence may be strong if it contains a foundational principle.

The system should classify data according to the following question:

```text
Does this data deserve to remain, move, or pass away?
```

---

## 3. Classification Axes

Each memory candidate should be evaluated across six axes.

```yaml
classification_axes:
  origin_value: 0-100
  persistence_score: 0-100
  reuse_score: 0-100
  structural_importance: 0-100
  risk_score: 0-100
  cross_context_score: 0-100
```

### 3.1 origin_value

Measures how close the data is to a meaningful human origin, question, intention, or Q-Point.

High score examples:

```text
- Foundational human question
- Original concept
- Epicenter-level insight
- Signed Q-Point record
- Author-defined principle
```

Low score examples:

```text
- Generic filler
- Repeated boilerplate
- Unattributed surface fragment
```

---

### 3.2 persistence_score

Measures whether the data should remain useful over time.

High score examples:

```text
- Long-term principle
- Stable architecture
- Safety rule
- Protocol definition
```

Low score examples:

```text
- One-time instruction
- Temporary phrasing
- Session-only remark
```

---

### 3.3 reuse_score

Measures how likely the data is to be reused.

High score examples:

```text
- Repeatedly cited concept
- Reusable template
- Frequently referenced decision
- Generalizable structure
```

Low score examples:

```text
- Single-use note
- Casual reaction
- Context-bound detail
```

---

### 3.4 structural_importance

Measures how much the data affects the system architecture.

High score examples:

```text
- Defines system behavior
- Changes protocol structure
- Connects multiple layers
- Serves as a core design anchor
```

Low score examples:

```text
- Minor wording
- Surface example
- Non-essential detail
```

---

### 3.5 risk_score

Measures safety, governance, corruption, misuse, or integrity risk.

High score examples:

```text
- Safety-critical rule
- Governance boundary
- Security-relevant trace
- High-risk instruction
- Data requiring human review
```

Low score examples:

```text
- Harmless casual data
- Low-impact stylistic fragment
```

Important note:

High risk does not always mean the data should be preserved as Core Memory.
Some high-risk data should be quarantined, reviewed, or discarded.
Risk score should trigger review before promotion.

---

### 3.6 cross_context_score

Measures whether the data appears useful across multiple contexts.

High score examples:

```text
- Used across different projects
- Referenced in multiple documents
- Appears in different reasoning chains
- Connects several protocols
```

Low score examples:

```text
- Useful only in one narrow exchange
- Project-local temporary detail
```

---

## 4. Memory Weight Score

The system calculates a total score called `memory_weight_score`.

Recommended default formula:

```text
memory_weight_score =
  origin_value * 0.20
+ persistence_score * 0.15
+ reuse_score * 0.15
+ structural_importance * 0.25
+ risk_score * 0.15
+ cross_context_score * 0.10
```

The weights may be adjusted by implementation, but `structural_importance` and `origin_value` should remain highly weighted.

---

## 5. Classification Thresholds

The default classification thresholds are:

```yaml
classification_thresholds:
  strong:
    score: ">= 80"
    layer: "core_memory"

  medium:
    score: ">= 40 and < 80"
    layer: "context_memory"

  light:
    score: "< 40"
    layer: "transient_data"
```

### 5.1 Strong / Core Memory

Data classified as Strong should be treated as structural memory.

It may include:

```text
- Foundational principles
- Protocol definitions
- Safety-critical rules
- Q-Point records
- Origin records
- Repeatedly referenced concepts
```

### 5.2 Medium / Context Memory

Data classified as Medium should be retained while useful to an active task or project.

It may include:

```text
- Current project context
- Draft notes
- Supporting references
- Recent decisions
- Temporary working material
```

### 5.3 Light / Transient Data

Data classified as Light should pass through the system and not be retained long-term.

It may include:

```text
- Casual replies
- One-time fragments
- Low-value noise
- Minor confirmations
- Non-reusable surface details
```

---

## 6. Override Rules

Some data should override normal score-based classification.

```yaml
override_rules:
  safety_critical:
    condition: "risk_score >= 90 and structural_importance >= 70"
    action: "force_core_memory_review"

  high_origin_anchor:
    condition: "origin_value >= 90 and structural_importance >= 70"
    action: "promote_to_core_memory"

  repeated_cross_context_use:
    condition: "reference_count >= 3 and cross_context_count >= 2"
    action: "promote_to_core_memory_candidate"

  low_value_noise:
    condition: "reuse_score <= 20 and structural_importance <= 20 and origin_value <= 30"
    action: "force_transient_data"

  high_risk_uncertain:
    condition: "risk_score >= 90 and structural_importance < 70"
    action: "quarantine_for_review"
```

### 6.1 Quarantine

Quarantine is not a memory layer.

It is a temporary review state for data that may be risky, corrupted, adversarial, or unsuitable for automatic promotion.

```text
Light / Medium / Strong = memory layers
Quarantine = review state
```

---

## 7. Promotion Rules

Memory weight is dynamic.

Data may be promoted when it proves useful across time or context.

```yaml
promotion_rules:
  light_to_medium:
    conditions:
      - "reference_count >= 2"
      - "reuse_score >= 40"
      - "structural_importance >= 40"

  medium_to_strong:
    conditions:
      - "reference_count >= 3"
      - "cross_context_count >= 2"
      - "structural_importance >= 80"

  medium_to_strong_origin_based:
    conditions:
      - "origin_value >= 90"
      - "persistence_score >= 80"
      - "structural_importance >= 70"
```

Promotion should create a trace record when the target layer is Core Memory.

---

## 8. Demotion Rules

Data may also be demoted when it becomes obsolete, unused, superseded, or noisy.

```yaml
demotion_rules:
  strong_to_medium:
    conditions:
      - "obsolete == true"
      - "structural_importance < 60"
      - "demotion_allowed == true"

  medium_to_light:
    conditions:
      - "reference_count == 0"
      - "last_referenced_days >= 90"
      - "reuse_score < 20"

  light_to_purge:
    conditions:
      - "reuse_score <= 10"
      - "structural_importance <= 10"
      - "origin_value <= 10"
```

Demotion from Core Memory should require review.

---

## 9. Core Memory Subtypes

Core Memory may be divided into two subtypes.

```text
Core Memory
├─ Immutable Core
└─ Evolvable Core
```

### 9.1 Immutable Core

Immutable Core contains data that should not be changed casually.

Examples:

```text
- Origin records
- Signed traces
- Foundational principles
- Safety constitution
- Initial Q-Point records
```

Update policy:

```text
- Append-only
- Versioned
- Review required
- No silent overwrite
```

### 9.2 Evolvable Core

Evolvable Core contains important data that may evolve over time.

Examples:

```text
- Living specifications
- Protocol improvements
- Updated architecture models
- Operational rules
```

Update policy:

```text
- Versioned update allowed
- Changelog required
- Superseded versions retained or archived
```

---

## 10. Synchronization with Breathing Reasoning

Memory classification should synchronize with reasoning intensity.

```yaml
reasoning_memory_sync:
  shallow_breathing:
    question_gravity: "low"
    allowed_layers:
      - "transient_data"
    response_style: "short, low-energy, minimal context"

  natural_breathing:
    question_gravity: "medium-low"
    allowed_layers:
      - "transient_data"
      - "context_memory"
    response_style: "normal explanation"

  deep_breathing:
    question_gravity: "medium-high"
    allowed_layers:
      - "context_memory"
      - "evolvable_core"
    response_style: "structured analysis"

  tanden_breathing:
    question_gravity: "high"
    allowed_layers:
      - "context_memory"
      - "evolvable_core"
      - "immutable_core"
    response_style: "focused core reasoning"

  focused_stillness:
    question_gravity: "critical"
    allowed_layers:
      - "immutable_core"
      - "signed_trace"
      - "q_point_record"
    response_style: "minimal, precise, high-integrity response"
```

If a high-gravity question has access only to low-weight memory, the system should not pretend certainty.

It should return a warning such as:

```text
Core memory is required, but only transient or context-level data is available.
Response confidence should be treated as limited.
```

---

## 11. Minimal Memory Record Example

```yaml
memory_record:
  id: "memory-record-001"
  title: "Data as Wind Principle"

  weight: "strong"
  layer: "core_memory"
  core_type: "immutable_core"

  summary: "Data should be treated as flow rather than static property."

  origin:
    source_type: "human_question"
    q_point_id: "qpoint-001"
    trace_id: "trace-001"

  classification:
    origin_value: 95
    persistence_score: 90
    reuse_score: 88
    structural_importance: 96
    risk_score: 40
    cross_context_score: 85
    memory_weight_score: 89

  lifecycle:
    created_at: "2026-06-12T00:00:00Z"
    last_referenced: "2026-06-12T00:00:00Z"
    reference_count: 42
    cross_context_count: 8
    last_promotion: "2026-06-12"
    demotion_allowed: false

  integrity:
    checksum: "sha256-example"
    signed: false
    review_required: true
```

---

## 12. Classification Pseudocode

```python
def classify_memory(record):
    score = (
        record.origin_value * 0.20
        + record.persistence_score * 0.15
        + record.reuse_score * 0.15
        + record.structural_importance * 0.25
        + record.risk_score * 0.15
        + record.cross_context_score * 0.10
    )

    if record.risk_score >= 90 and record.structural_importance < 70:
        return "quarantine_for_review"

    if record.risk_score >= 90 and record.structural_importance >= 70:
        return "core_memory_review"

    if record.origin_value >= 90 and record.structural_importance >= 70:
        return "core_memory"

    if score >= 80:
        return "core_memory"

    if score >= 40:
        return "context_memory"

    return "transient_data"
```

---

## 13. Relationship to Memory Weight Architecture v0.1

This document extends Memory Weight Architecture v0.1.

```text
v0.1:
  Defines the three memory layers.

v0.2:
  Defines how data is classified into those layers.
```

Recommended stack:

```text
Data-as-Wind Principle
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

---

## 14. Closing Principle

The purpose of memory classification is not to remember more.

The purpose is to remember with weight.

```text
Light data should pass.
Medium data should work.
Strong data should endure.
```

A mature AI system should not become a giant warehouse.

It should become a living body:

```text
Strong memory as skeleton.
Medium memory as muscle.
Light memory as breath.
```

This is the foundation of energy-aware, traceable, adaptive intelligence.
