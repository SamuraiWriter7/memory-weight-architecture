# Memory Weight Architecture

## 記憶重層化アーキテクチャ Specification v0.1.0-candidate

## 1. Overview

**Memory Weight Architecture** is a layered data-governance model for Civilization OS / Kazene OS.

It classifies data not as a uniform mass, but as weighted flows according to their origin, persistence, risk, reuse value, and structural importance.

In this model, data is not treated as a static object to be stored indefinitely.
Data is treated as wind: it flows, gathers, disperses, returns, and sometimes becomes a structural seed.

The purpose of this architecture is to reduce unnecessary context accumulation, minimize retrieval and reasoning cost, and support energy-aware AI operation.

In Japanese:

> 記憶重層化アーキテクチャとは、すべてのデータを一律に保存するのではなく、震源性・永続性・危険性・再利用性・構造的重要度に応じて、記憶の重さを動的に振り分けるための設計である。

---

## 2. Core Principle

The core principle is simple:

```text
Not all data deserves the same memory weight.
```

AI systems should not treat casual fragments, temporary context, safety-critical rules, origin records, and long-term structural principles as equivalent.

A lightweight and intelligent system must distinguish between:

```text
What must remain.
What should remain for now.
What should pass through and disappear.
```

This leads to a three-layer memory model:

```text
Strong  → Core Memory
Medium  → Context Memory
Light   → Transient Data
```

---

## 3. The Three Memory Layers

```text
[ Strong ] Core Memory
    Role: structural skeleton
    Storage: persistent
    Access priority: highest

[ Medium ] Context Memory
    Role: working muscle
    Storage: temporary / project-based
    Access priority: adaptive

[ Light ] Transient Data
    Role: breath / passing wind
    Storage: volatile
    Access priority: lowest
```

---

## 4. Strong Layer: Core Memory

### 4.1 Definition

**Core Memory** is the structural skeleton of the system.

It contains data that must be preserved because it defines identity, safety, continuity, origin, or long-term strategic direction.

This layer should remain small, clear, and highly curated.

### 4.2 Typical Data

Core Memory may include:

```text
- Foundational principles
- Long-term project direction
- High-value Q-Point records
- Origin / epicenter data
- Safety-critical constraints
- Repeatedly referenced concepts
- Stable protocol definitions
- Key architectural decisions
```

### 4.3 Promotion Conditions

Data may be promoted to Core Memory when one or more of the following conditions are met:

```text
- It has high origin value.
- It is referenced repeatedly across different contexts.
- It affects long-term system behavior.
- It defines a protocol, rule, principle, or architecture.
- It is safety-critical.
- It serves as a recurring structural anchor.
```

### 4.4 Storage Policy

Core Memory should be:

```text
- Persistent
- Versioned
- Traceable
- Protected from noise
- Easy to retrieve
- Difficult to overwrite accidentally
```

Recommended storage examples:

```text
- GitHub repository
- Versioned specification documents
- Signed trace records
- Q-Point records
- Private knowledge base
- Stable memory index
```

---

## 5. Medium Layer: Context Memory

### 5.1 Definition

**Context Memory** is the working layer of intelligence.

It contains information necessary for an active task, current project, recent conversation, or ongoing reasoning process.

It is not necessarily permanent, but it is useful while the system is operating within a specific context.

### 5.2 Typical Data

Context Memory may include:

```text
- Current session context
- Project-specific notes
- Recent decisions
- Draft structure
- Temporary references
- Supporting arguments
- Active implementation details
- Near-term task state
```

### 5.3 Retention Policy

Context Memory should be retained while it remains useful.

When a project, session, or task reaches completion, Context Memory should be filtered.

The system should decide:

```text
- What should be compressed into Core Memory?
- What should remain as project history?
- What should be discarded?
```

### 5.4 Compression Rule

At the end of a task, Context Memory should not be preserved in raw form by default.

It should be compressed into:

```text
- Summary
- Decision record
- Trace record
- Protocol update
- Changelog entry
- Core principle
```

This prevents memory bloat.

---

## 6. Light Layer: Transient Data

### 6.1 Definition

**Transient Data** is passing wind.

It exists only for immediate response generation and has little or no long-term value.

It should not be promoted into long-term memory unless it unexpectedly gains structural significance.

### 6.2 Typical Data

Transient Data may include:

```text
- Casual reactions
- One-time phrasing
- Temporary noise
- Minor confirmations
- Low-value fragments
- Repetitive filler
- Non-essential surface details
```

### 6.3 Disposal Policy

Transient Data should be:

```text
- Used briefly
- Not indexed as core knowledge
- Not allowed to pollute Core Memory
- Discarded after use
```

The purpose is not to erase meaning, but to prevent unnecessary accumulation.

---

## 7. Synchronization with Breathing Reasoning

Memory Weight Architecture is designed to synchronize with the **Breathing Reasoning Model**.

Reasoning intensity and memory depth should move together.

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

The system should not invoke deep memory for every input.

Likewise, it should not answer a core-level question using only surface context.

---

## 8. Question Gravity and Memory Access

The depth of memory access should be determined by question gravity.

### 8.1 Low Gravity Question

Examples:

```text
- Casual chat
- Simple confirmation
- Light preference
- One-off surface question
```

Recommended memory access:

```text
- Transient Data
- Minimal Context Memory
- No Core Memory unless needed
```

### 8.2 Medium Gravity Question

Examples:

```text
- Project continuation
- Draft refinement
- Technical adjustment
- Strategic comparison
```

Recommended memory access:

```text
- Context Memory
- Selective Core Memory
- Relevant recent traces
```

### 8.3 High Gravity Question

Examples:

```text
- Foundational protocol design
- Long-term strategy
- Safety architecture
- Origin / royalty / trace governance
- Major philosophical or structural decision
```

Recommended memory access:

```text
- Core Memory
- Q-Point records
- Trace Protocol records
- Architecture documents
- Relevant Context Memory
```

---

## 9. Data Classification Matrix

| Weight | Layer          | Role     | Retention  | Access Priority | Example                |
| ------ | -------------- | -------- | ---------- | --------------- | ---------------------- |
| Strong | Core Memory    | Skeleton | Long-term  | Highest         | Protocol principles    |
| Medium | Context Memory | Muscle   | Task-based | Adaptive        | Active project context |
| Light  | Transient Data | Breath   | Temporary  | Lowest          | Casual fragments       |

---

## 10. Promotion and Demotion

Data weight is not fixed.

Data may move between layers.

### 10.1 Promotion

Light or Medium data may be promoted when:

```text
- It becomes repeatedly useful.
- It reveals a new structural principle.
- It becomes part of a protocol.
- It carries high origin value.
- It affects long-term system behavior.
```

### 10.2 Demotion

Core or Context data may be demoted when:

```text
- It becomes obsolete.
- It is superseded by a newer specification.
- It is no longer referenced.
- It no longer affects system behavior.
- It creates more noise than value.
```

Demotion should be traceable, especially for Core Memory.

---

## 11. Energy-Aware Operation

Memory Weight Architecture supports energy-aware AI operation.

The system reduces unnecessary computational load by avoiding uniform treatment of all data.

Instead of searching everything every time, it asks:

```text
Which memory layer is required for this question?
How deep should reasoning go?
What can be ignored safely?
What must be preserved?
```

This enables:

```text
- Lower retrieval cost
- Lower reasoning cost
- Reduced context bloat
- Cleaner inference
- Faster response
- Better long-term maintainability
```

---

## 12. Architectural Benefits

### 12.1 Cleaner Intelligence

By preventing low-value data from entering Core Memory, the system reduces noise and helps preserve reasoning clarity.

### 12.2 Lower Cognitive and Computational Load

The system does not need to activate all memory layers for every input.

This supports lightweight and efficient operation.

### 12.3 Stronger Traceability

Important data can be connected to origin records, Q-Point records, and Trace Protocol entries.

### 12.4 Better Safety

Safety-critical data can be placed in Core Memory, while unstable or low-value data can be prevented from contaminating core structures.

### 12.5 Better Adaptability

Because memory weight is dynamic, the system can adapt to different tasks, users, projects, and risk levels.

---

## 13. Minimal Implementation Model

A minimal implementation may classify each data item using the following fields:

```yaml
memory_record:
  id: "memory-record-example-001"
  title: "Example Memory Record"
  weight: "strong" # strong | medium | light
  layer: "core_memory" # core_memory | context_memory | transient_data

  origin:
    source_type: "human_question"
    q_point_id: "qpoint-example-001"
    trace_id: "trace-example-001"

  classification:
    origin_value: "high" # low | medium | high
    persistence: "long_term" # transient | task_based | long_term
    reuse_value: "high" # low | medium | high
    risk_level: "medium" # low | medium | high
    structural_importance: "high" # low | medium | high

  retention_policy:
    mode: "persistent" # volatile | task_based | persistent
    review_required: true
    demotion_allowed: true

  access_policy:
    priority: "highest" # low | adaptive | highest
    reasoning_depth_required: "deep" # shallow | standard | deep | focused
```

---

## 14. Relationship to Civilization OS

Memory Weight Architecture belongs to the foundational layer of Civilization OS / Kazene OS.

Recommended stack:

```text
Data-as-Wind Principle
    ↓
Data View Layer
    ↓
Question Gravity Layer
    ↓
Memory Weight Architecture
    ↓
Breathing Reasoning Model
    ↓
Trace Protocol
    ↓
Q-Point Protocol
    ↓
Royalty OS
```

This stack allows AI to:

```text
- See data as wind
- Read the gravity of questions
- Select memory depth
- Adjust reasoning intensity
- Preserve origin
- Trace value
- Return value to its source
```

---

## 15. Closing Principle

Memory should not be a warehouse.

Memory should be a living tide.

```text
Strong memory remains as skeleton.
Medium memory moves as muscle.
Light memory passes as breath.
```

The goal is not to remember everything.

The goal is to remember what allows intelligence to remain clear, adaptive, traceable, and alive.

> From giant warehouses to the mind of a master.
