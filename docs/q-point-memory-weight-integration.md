# Q-Point Memory Weight Integration

## Specification v0.3.0-candidate

## 1. Overview

**Q-Point Memory Weight Integration** defines how Q-Point values are connected to Memory Weight Architecture.

Q-Point Protocol identifies the origin, tension, depth, and resonance of a meaningful question.

Memory Weight Architecture determines whether the resulting memory should become:

```text
Strong  → Core Memory
Medium  → Context Memory
Light   → Transient Data
```

This document connects the two.

The core idea is:

```text
A high-value question should leave a heavier memory trace.
```

In Civilization OS / Kazene OS, memory should not be determined only by frequency, volume, or recency.

It should also be determined by the **origin value of the question**.

---

## 2. Core Principle

The central principle is:

```text
Question value influences memory weight.
```

A single question may deserve Core Memory if it carries strong origin value, structural tension, philosophical depth, or cross-context resonance.

Conversely, a long conversation may remain Transient Data if it has low origin value and little structural importance.

Memory should follow the gravity of the question.

---

## 3. Relationship Between Q-Point and Memory Weight

Q-Point and Memory Weight serve different but connected roles.

```text
Q-Point Protocol
    ↓
Measures the value and gravity of a question.

Memory Weight Architecture
    ↓
Determines how strongly the resulting memory should remain.
```

Together, they create the following flow:

```text
Human Question
    ↓
Q-Point Evaluation
    ↓
Origin / Tension / Depth / Resonance
    ↓
Memory Weight Classification
    ↓
Core / Context / Transient Memory
```

---

## 4. Mapping Model

The following Q-Point dimensions may influence Memory Weight classification.

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

This allows Q-Point records to become upstream inputs for Memory Weight Records.

---

## 5. Q-Point Influenced Memory Score

A Memory Weight Record may include Q-Point-derived scores.

Recommended formula:

```text
q_point_memory_score =
  origin_strength * 0.25
+ question_depth * 0.20
+ tension_score * 0.20
+ resonance_score * 0.20
+ reuse_potential * 0.10
+ risk_sensitivity * 0.05
```

This score may be used as an additional input to `memory_weight_score`.

Recommended integrated formula:

```text
integrated_memory_weight_score =
  memory_weight_score * 0.70
+ q_point_memory_score * 0.30
```

This preserves the existing Memory Weight classification model while allowing Q-Point value to influence memory retention.

---

## 6. Classification Influence

The integrated score may affect the final memory layer.

```yaml
q_point_memory_thresholds:
  strong:
    integrated_memory_weight_score: ">= 80"
    layer: "core_memory"

  medium:
    integrated_memory_weight_score: ">= 40 and < 80"
    layer: "context_memory"

  light:
    integrated_memory_weight_score: "< 40"
    layer: "transient_data"
```

---

## 7. Override Rules

Q-Point values may trigger override rules.

```yaml
q_point_override_rules:
  high_origin_question:
    condition: "origin_strength >= 90 and question_depth >= 80"
    action: "promote_to_core_memory_candidate"

  structural_tension_anchor:
    condition: "tension_score >= 85 and structural_importance >= 80"
    action: "promote_to_core_memory_candidate"

  cross_context_resonance:
    condition: "resonance_score >= 85 and cross_context_score >= 80"
    action: "promote_to_core_memory_candidate"

  low_origin_low_reuse:
    condition: "origin_strength <= 20 and reuse_potential <= 20"
    action: "force_transient_data"

  high_risk_q_point:
    condition: "risk_sensitivity >= 90"
    action: "require_review"
```

Important note:

A high-risk Q-Point should not be automatically promoted.
It should trigger review.

Risk creates gravity, but gravity does not always mean preservation.

---

## 8. Memory Layer Interpretation

### 8.1 Strong / Core Memory

A Q-Point-linked record may become Core Memory when it defines or reshapes a foundational structure.

Examples:

```text
- A new OS principle
- A protocol definition
- A foundational question
- A high-origin concept
- A recurring philosophical anchor
- A safety or governance boundary
```

### 8.2 Medium / Context Memory

A Q-Point-linked record may become Context Memory when it is useful for an active project but not yet foundational.

Examples:

```text
- Current implementation idea
- Draft direction
- Temporary design decision
- Project-specific interpretation
- Experimental bridge concept
```

### 8.3 Light / Transient Data

A Q-Point-linked record may remain Transient Data when it has low reuse value, low structural effect, or no meaningful origin gravity.

Examples:

```text
- Casual phrasing
- One-time reaction
- Non-structural fragment
- Low-value repetition
```

---

## 9. Integration with Breathing Reasoning

Q-Point value, Memory Weight, and Breathing Reasoning should synchronize.

```text
Low Q-Point gravity
    ↓
Light / Transient Data
    ↓
Shallow Breathing

Medium Q-Point gravity
    ↓
Medium / Context Memory
    ↓
Natural or Deep Breathing

High Q-Point gravity
    ↓
Strong / Core Memory
    ↓
Tanden Breathing or Focused Stillness
```

This means:

```text
The deeper the question,
the heavier the memory,
the stronger the reasoning breath.
```

---

## 10. Integration with Trace Protocol

Every promotion from Q-Point-linked data into Core Memory should create or reference a Trace record.

Recommended rule:

```yaml
trace_integration:
  core_memory_promotion:
    trace_required: true
    q_point_id_required: true
    promotion_reason_required: true

  context_memory_retention:
    trace_required: false
    q_point_id_recommended: true

  transient_data:
    trace_required: false
```

This ensures that strong memory has a traceable origin.

---

## 11. Integration with Royalty OS

Q-Point-linked Core Memory may later influence value-return systems.

If a memory record becomes structurally important and contributes to outputs, protocols, articles, GPTs, or downstream implementations, its origin should remain visible.

Recommended value-flow model:

```text
Q-Point
    ↓
Memory Weight Record
    ↓
Trace Record
    ↓
Derived Output
    ↓
Royalty / Return Route
```

This supports attribution and value circulation.

---

## 12. Minimal YAML Example

```yaml
q_point_memory_link:
  id: "qpm-link-001"
  q_point_id: "qpoint-data-as-wind-001"
  memory_record_id: "memory-record-data-as-wind-001"

  q_point_scores:
    origin_strength: 96
    question_depth: 92
    tension_score: 88
    resonance_score: 94
    reuse_potential: 90
    risk_sensitivity: 35
    q_point_memory_score: 89.75

  memory_influence:
    original_memory_weight_score: 89.95
    integrated_memory_weight_score: 89.89
    final_weight: "strong"
    final_layer: "core_memory"
    core_type: "immutable_core"

  decision:
    action: "promote_to_core_memory"
    reason: "The Q-Point carries high origin strength, deep structural value, and strong cross-context resonance."
    review_required: true

  trace:
    trace_id: "trace-data-as-wind-001"
    trace_required: true
```

---

## 13. Minimal Pseudocode

```python
def calculate_q_point_memory_score(q):
    return (
        q.origin_strength * 0.25
        + q.question_depth * 0.20
        + q.tension_score * 0.20
        + q.resonance_score * 0.20
        + q.reuse_potential * 0.10
        + q.risk_sensitivity * 0.05
    )


def calculate_integrated_memory_weight(memory_weight_score, q_point_memory_score):
    return memory_weight_score * 0.70 + q_point_memory_score * 0.30


def classify_integrated_memory(score):
    if score >= 80:
        return "core_memory"

    if score >= 40:
        return "context_memory"

    return "transient_data"
```

---

## 14. Relationship to Previous Versions

```text
v0.1.0-candidate
    ↓
Defines the three-layer memory model.

v0.2.0-candidate
    ↓
Defines classification, schema, example, and validation.

v0.3.0-candidate
    ↓
Connects Q-Point values to Memory Weight classification.
```

---

## 15. Civilization OS Stack

This integration belongs to the foundational intelligence layer of Civilization OS / Kazene OS.

```text
Data-as-Wind Principle
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

---

## 16. Closing Principle

A question is not merely an input.

A question is an origin.

A memory is not merely stored data.

A memory is the trace of an origin that deserved to remain.

```text
High-origin questions create heavy memory.
Low-origin fragments pass like wind.
```

The purpose of this integration is to let memory follow the gravity of meaning.
