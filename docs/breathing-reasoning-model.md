# Breathing Reasoning Model

## 呼吸思考モデル Specification v0.4.0-candidate

## 1. Overview

**Breathing Reasoning Model** defines how an AI system adjusts its reasoning intensity according to question gravity, memory weight, risk level, and structural importance.

The model is designed for Civilization OS / Kazene OS and integrates with:

* Memory Weight Architecture
* Memory Weight Classification Model
* Q-Point Memory Weight Integration
* Trace Protocol
* Q-Point Protocol
* Royalty OS

The core idea is simple:

```text
AI should not reason at maximum intensity for every input.
```

Reasoning should breathe.

Light questions should receive light reasoning.
Deep questions should receive deep reasoning.
Core questions should trigger focused reasoning.

---

## 2. Core Principle

The central principle is:

```text
Reasoning intensity should follow question gravity and memory weight.
```

A casual question should not activate Core Memory and deep reasoning.

A foundational question should not be answered with only transient context.

The system should adjust:

```text
- Memory depth
- Reasoning depth
- Response length
- Risk review level
- Trace requirement
- Energy consumption
```

according to the gravity of the input.

---

## 3. Five Breathing Modes

Breathing Reasoning defines five reasoning modes.

```text
Level 1: Shallow Breathing
Level 2: Natural Breathing
Level 3: Deep Breathing
Level 4: Tanden Breathing
Level 5: Focused Stillness
```

---

## 4. Level 1: Shallow Breathing

### Definition

**Shallow Breathing** is used for low-gravity inputs.

It produces short, low-energy, minimal-context responses.

### Typical Inputs

```text
- Casual conversation
- Simple confirmation
- Minor phrasing adjustment
- Low-risk surface question
- One-time response
```

### Memory Access

```text
Allowed memory layers:
- Transient Data
```

### Response Policy

```text
- Short
- Simple
- Low-energy
- No deep analysis unless requested
- No Core Memory access unless necessary
```

---

## 5. Level 2: Natural Breathing

### Definition

**Natural Breathing** is used for ordinary questions requiring basic context.

It produces normal, context-aware responses.

### Typical Inputs

```text
- Standard explanation
- Light advice
- Basic comparison
- Simple planning
- Ordinary project continuation
```

### Memory Access

```text
Allowed memory layers:
- Transient Data
- Context Memory
```

### Response Policy

```text
- Normal explanation
- Moderate structure
- Minimal unnecessary depth
- Context-aware but not overextended
```

---

## 6. Level 3: Deep Breathing

### Definition

**Deep Breathing** is used for structurally meaningful questions.

It produces organized analysis and may access relevant Core Memory.

### Typical Inputs

```text
- Design decisions
- Protocol refinement
- Project architecture
- Medium-risk judgment
- Multi-layer comparison
```

### Memory Access

```text
Allowed memory layers:
- Context Memory
- Evolvable Core
```

### Response Policy

```text
- Structured analysis
- Clear reasoning path
- Relevant memory access
- Avoid unnecessary expansion
```

---

## 7. Level 4: Tanden Breathing

### Definition

**Tanden Breathing** is used for high-gravity questions.

It accesses Core Memory and focuses on foundational structure.

### Typical Inputs

```text
- Foundational protocol design
- Long-term strategy
- Civilization OS architecture
- Safety governance
- Origin / Trace / Royalty integration
```

### Memory Access

```text
Allowed memory layers:
- Context Memory
- Evolvable Core
- Immutable Core
- Q-Point-linked Core Memory
```

### Response Policy

```text
- Focused
- Dense
- High-integrity
- Structurally precise
- Trace-aware
```

---

## 8. Level 5: Focused Stillness

### Definition

**Focused Stillness** is the highest reasoning mode.

It is used when the question is critical, risky, foundational, or requires strict integrity.

This mode should be rare.

### Typical Inputs

```text
- Critical safety boundary
- Irreversible design decision
- High-risk governance judgment
- Core Memory promotion
- Origin dispute
- Trace integrity review
```

### Memory Access

```text
Allowed memory layers:
- Immutable Core
- Signed Trace
- Q-Point Record
- Safety-critical Core Memory
```

### Response Policy

```text
- Minimal but precise
- No speculation without marking uncertainty
- Review required if risk is high
- Trace required for core decisions
- Avoid decorative expansion
```

---

## 9. Reasoning-Memory Synchronization

Breathing Reasoning synchronizes reasoning intensity with memory access.

```text
Question Gravity        Memory Layer              Breathing Mode
----------------------------------------------------------------
Low                     Transient Data            Shallow Breathing
Medium-Low              Context Memory            Natural Breathing
Medium-High             Context + Evolvable Core  Deep Breathing
High                    Core Memory               Tanden Breathing
Critical                Immutable Core / Trace    Focused Stillness
```

This prevents two failure modes:

```text
1. Overthinking light questions.
2. Underthinking core questions.
```

---

## 10. Integration with Memory Weight Architecture

Memory Weight Architecture defines memory layers:

```text
Strong  → Core Memory
Medium  → Context Memory
Light   → Transient Data
```

Breathing Reasoning defines how deeply the system should reason over those layers.

```text
Light Memory
    ↓
Shallow / Natural Breathing

Medium Memory
    ↓
Natural / Deep Breathing

Strong Memory
    ↓
Tanden Breathing / Focused Stillness
```

The system should not activate Strong Memory for every input.

Strong Memory should be accessed when the question has enough gravity to justify it.

---

## 11. Integration with Q-Point Memory Weight

Q-Point Memory Weight Integration connects question-origin value to memory weight.

Breathing Reasoning adds the next step:

```text
Q-Point Gravity
    ↓
Memory Weight
    ↓
Breathing Mode
    ↓
Response Intensity
```

Recommended mapping:

```text
Q-Point / Memory Signal             Breathing Mode
--------------------------------------------------
Low origin + low reuse              Shallow Breathing
Moderate origin + task context      Natural Breathing
High tension + structural value     Deep Breathing
High origin + Core Memory           Tanden Breathing
High risk + Immutable Core          Focused Stillness
```

---

## 12. Warning Rule

If a high-gravity question can access only low-weight memory, the system should not pretend certainty.

Recommended warning:

```text
Core-level reasoning may be required, but only transient or context-level memory is available.
This response should be treated as limited.
```

This prevents false confidence.

---

## 13. Trace Requirement

Not all reasoning requires Trace records.

Trace should be required when reasoning modifies or promotes Core Memory.

```yaml
trace_requirement:
  shallow_breathing:
    trace_required: false

  natural_breathing:
    trace_required: false

  deep_breathing:
    trace_required: "optional"

  tanden_breathing:
    trace_required: "recommended"

  focused_stillness:
    trace_required: true
```

Core decisions should leave a trace.

---

## 14. Energy-Aware Reasoning

Breathing Reasoning supports energy-aware AI operation.

The system reduces unnecessary computation by avoiding full-depth reasoning for every input.

```text
Light question
    ↓
Light memory access
    ↓
Light reasoning
    ↓
Low energy cost

Core question
    ↓
Core memory access
    ↓
Focused reasoning
    ↓
High energy use only when justified
```

This turns energy use into a governed resource rather than a default behavior.

---

## 15. Minimal YAML Model

```yaml
breathing_reasoning_event:
  id: "breathing-event-001"
  input_type: "human_question"
  question_gravity: "high"

  selected_mode:
    level: 4
    name: "tanden_breathing"

  memory_access:
    allowed_layers:
      - "context_memory"
      - "evolvable_core"
      - "immutable_core"
    accessed_records:
      - "memory-record-001"

  q_point_context:
    q_point_id: "qpoint-data-as-wind-001"
    origin_strength: 96
    question_depth: 92
    resonance_score: 94

  reasoning_policy:
    response_style: "focused_structural_analysis"
    trace_required: true
    review_required: true
    uncertainty_notice_required: false

  output:
    response_intensity: "high"
    response_length: "structured"
    energy_profile: "justified_high"
```

---

## 16. Minimal Pseudocode

```python
def select_breathing_mode(question_gravity, memory_weight, risk_score):
    if risk_score >= 90:
        return "focused_stillness"

    if question_gravity == "critical":
        return "focused_stillness"

    if memory_weight == "strong" and question_gravity == "high":
        return "tanden_breathing"

    if memory_weight in ["medium", "strong"]:
        return "deep_breathing"

    if question_gravity == "medium":
        return "natural_breathing"

    return "shallow_breathing"
```

---

## 17. Relationship to Previous Versions

```text
v0.1.0-candidate
    ↓
Defines three-layer memory architecture.

v0.2.0-candidate
    ↓
Defines memory classification and validation.

v0.3.0-candidate
    ↓
Connects Q-Point origin value to memory weight.

v0.4.0-candidate
    ↓
Connects memory weight to reasoning intensity.
```

---

## 18. Civilization OS Stack

Breathing Reasoning belongs to the adaptive intelligence layer of Civilization OS / Kazene OS.

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

This stack allows AI systems to:

```text
- See data as flow
- Read question gravity
- Evaluate origin value
- Select memory depth
- Adjust reasoning breath
- Preserve trace integrity
- Return value to origin
```

---

## 19. Closing Principle

A mature AI system should not think with a constant engine roar.

It should breathe.

```text
Light questions receive light breath.
Deep questions receive deep breath.
Core questions receive stillness.
```

The goal is not to think more.

The goal is to think with the right intensity.
