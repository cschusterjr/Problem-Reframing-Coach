# 🧠 Problem Reframing Coach

An AI-powered cognitive coaching platform that helps learners improve **how they think**, not just **what they know**.

Instead of providing answers, the application guides learners through identifying hidden assumptions, reframing problems, and developing transferable thinking skills.

---

# Why This Project?

Most AI applications are designed to answer questions.

This project explores a different idea:

> **What if AI could help people become better thinkers instead of simply providing answers?**

The inspiration came from real-world examples where experienced professionals overlooked simple solutions because they unconsciously accepted hidden assumptions.

Examples include:

- Removing a television from its box so it fits in an elevator instead of using a crane.
- Deflating a truck's tires so it can pass under a bridge instead of dismantling the truck or lifting the bridge.

The goal of this project is to teach learners how to recognize these thinking patterns through guided practice.

---

# Learning Objectives

The application helps learners practice several cognitive skills including:

- Questioning assumptions
- Problem reframing
- First-principles thinking
- Challenging constraints
- Simplification before complexity
- Reflection and transfer of learning

Each scenario is designed to reinforce one specific cognitive skill.

---

# Current Features

## Interactive Learning Experience

- Welcome screen
- Multi-step coaching workflow
- Scenario selection
- Reflection report

## Scenario Library

Current scenarios include:

- The Large TV Problem
- The Truck Under the Bridge
- The Overloaded Calendar
- The Distracted Classroom
- The Feature Request

Each scenario includes:

- Cognitive Skill
- Why It Matters
- Guided Reflection
- Real-World Applications
- Key Takeaway

## Cognitive Coaching

Learners:

1. Read a scenario.
2. Submit an initial solution.
3. Receive coaching questions.
4. Revise their response.
5. Review a Cognitive Flexibility Report.

---

# Current Architecture

```
                 Streamlit UI
                       │
                       ▼
                 FastAPI Backend
                       │
                       ▼
               CognitiveCoach
                       │
          ┌────────────┴────────────┐
          │                         │
   Scenario Repository      Learning Logic
```

---

# Technical Stack

## Backend

- Python
- FastAPI
- Pydantic

## Frontend

- Streamlit

## Data

- JSON Scenario Repository

## Architecture

- REST APIs
- Service Layer
- Modular UI Components

---

# Project Structure

```
backend/
│
├── app/
│   ├── data/
│   ├── services/
│   ├── coach.py
│   ├── main.py
│   ├── models.py
│   └── scenarios.py
│
├── ui/
│   ├── coaching.py
│   ├── feedback.py
│   ├── scenario.py
│   ├── styles.py
│   └── welcome.py
│
└── streamlit_app.py
```

---

# Example Learning Flow

```
Welcome

↓

Choose Scenario

↓

Understand the Problem

↓

Initial Response

↓

AI Coaching

↓

Revised Response

↓

Cognitive Flexibility Report

↓

Reflection
```

---

# Product Vision

This project explores how AI can act as a **cognitive coach** rather than an answer engine.

Instead of solving problems for learners, the system encourages them to:

- Pause before solving.
- Identify hidden assumptions.
- Reframe the problem.
- Discover simpler solutions.
- Transfer those thinking strategies to future situations.

---

# Future Roadmap

## AI Cognitive Coach

Replace static coaching questions with personalized AI coaching powered by large language models.

## Intelligent Assessment

Evaluate learner responses across multiple cognitive dimensions including:

- Assumption Detection
- Problem Framing
- Constraint Awareness
- Reflection
- First-Principles Thinking

## Learning Analytics

Track:

- Improvement over time
- Cognitive skill development
- Reflection quality
- Coaching effectiveness

## Curriculum Expansion

Build additional learning modules covering:

- Systems Thinking
- Tradeoff Analysis
- Decision Making
- Root Cause Analysis
- Transfer of Learning

---

# Educational Foundations

This project draws inspiration from research in:

- Cognitive Flexibility
- Functional Fixedness
- Metacognition
- First-Principles Thinking
- Reflection-Based Learning
- Transfer of Learning

---

# Current Status

🚧 Active Development

Current milestone:

**Phase 5 — AI Cognitive Coach**

Next step:

Integrate OpenAI to generate personalized coaching while preserving the instructional design principles of the Cognitive Coach.

---

# Author

Developed as an exploration of how AI can support better thinking within education and workforce learning.

# About This Project

This project combines software engineering, AI engineering, product management, and learning science to explore a simple question:

> How can AI help people become better thinkers?

The long-term vision is an AI-powered cognitive coaching platform that helps learners develop transferable thinking skills through guided reflection and practice.