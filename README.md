# 🧠 Problem Reframing Coach

An AI-powered cognitive coaching platform that helps learners improve **how they think**, not just **what they know**.

Instead of providing answers, the application guides learners through identifying hidden assumptions, reframing problems, and developing transferable thinking skills through structured coaching.

---

# Project Vision

Most AI applications are designed to answer questions.

This project explores a different question:

> **What if AI could help people become better thinkers instead of simply providing answers?**

The long-term vision is an AI-powered coach that helps students, educators, and workforce learners develop cognitive flexibility through guided reflection and practice.

---

# The Problem

People often solve the problem they believe they have instead of the problem they actually have.

Real-world examples include:

- Removing a television from its box so it fits into an elevator instead of using a crane.
- Deflating a truck's tires so it can pass under a bridge instead of dismantling the truck or lifting the bridge.

These examples illustrate **functional fixedness**—the tendency to accept hidden assumptions without questioning them.

This project teaches learners how to recognize and overcome those thinking patterns.

---

# Learning Objectives

The platform helps learners practice:

- Questioning assumptions
- Problem reframing
- Challenging constraints
- Simplification before complexity
- First-principles thinking
- Reflection and transfer of learning

Each scenario focuses on developing one specific cognitive skill.

---

# Current Features

## Interactive Learning Experience

- Welcome experience
- Scenario selection
- Guided coaching workflow
- Reflection report
- Multi-step learning process

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
- Reflection Prompt
- Real-World Applications
- Key Takeaway

## Cognitive Coaching

Learners:

1. Read a scenario.
2. Submit an initial response.
3. Receive coaching questions.
4. Revise their thinking.
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
                       ▼
                 AI Provider
                       │
          ┌────────────┴────────────┐
          │                         │
   MockAIProvider          OpenAIProvider (planned)
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
- Service Layer Architecture
- Modular UI Components
- AI Provider Abstraction

---

# Project Structure

```
backend/
│
├── app/
│   ├── data/
│   ├── services/
│   │   ├── ai_provider.py
│   │   ├── cognitive_coach.py
│   │   ├── mock_provider.py
│   │   └── openai_provider.py
│   │
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

Cognitive Coaching

↓

Revised Response

↓

Cognitive Flexibility Report

↓

Reflection
```

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

Next milestone:

Integrate OpenAI to generate personalized coaching while preserving the instructional philosophy of guided thinking rather than answer generation.

---

# Future Roadmap

## AI Coaching

Replace static coaching with personalized AI coaching.

## Intelligent Assessment

Evaluate learner responses across multiple cognitive dimensions including:

- Assumption Detection
- Problem Framing
- Constraint Awareness
- Reflection
- First-Principles Thinking

## Learning Analytics

Track learner improvement over time.

## Cognitive Skills Curriculum

Expand into a full curriculum covering:

- Systems Thinking
- Tradeoff Analysis
- Decision Making
- Root Cause Analysis
- Transfer of Learning

---

# About This Project

This project combines software engineering, AI engineering, product management, and learning science to explore one central question:

> **How can AI help people become better thinkers?**

Rather than replacing human reasoning, the goal is to build AI that strengthens it.