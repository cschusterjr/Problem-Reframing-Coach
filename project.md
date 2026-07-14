Version: 0.4.0 (Architecture Complete)

Current Phase: AI Cognitive Coach

# Problem Reframing Coach

## Product Vision

Build an AI-powered cognitive coaching platform that teaches learners how to identify assumptions, reframe problems, and apply transferable thinking strategies across education and the workplace.

Unlike traditional AI assistants that primarily generate answers, this project explores AI as a thinking coach.

---

# Product Philosophy

The objective is not to solve problems for learners.

The objective is to improve the learner's thinking process.

Every feature should reinforce this principle.

---

# Core Learning Model

Every scenario follows the same instructional pattern:

```
Understand

↓

Think

↓

Respond

↓

Receive Coaching

↓

Revise

↓

Reflect

↓

Transfer Learning
```

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
        ┌──────────────┴──────────────┐
        │                             │
 MockAIProvider            OpenAIProvider
```

---

# Development Milestones

## ✅ Milestone 1

Backend MVP

Completed

- FastAPI
- Scenario Repository
- Coaching Endpoint
- Feedback Endpoint

---

## ✅ Milestone 2

Interactive Learning Experience

Completed

- Streamlit UI
- Multi-step workflow
- Reflection report
- Scenario selection

---

## ✅ Milestone 3

Learning Experience Design

Completed

Added:

- Cognitive Skill
- Why It Matters
- Reflection Prompt
- Key Takeaway
- Real-World Applications

---

## ✅ Milestone 4

Software Architecture

Completed

Refactored coaching into:

```
CognitiveCoach
```

Added:

```
AI Provider Layer
```

Current providers:

- MockAIProvider
- OpenAIProvider (placeholder)

---

## 🚧 Milestone 5

AI Cognitive Coach

Current focus

Planned work:

- OpenAI integration
- Prompt engineering
- Personalized coaching
- AI-generated reflection

---

# Future Product Roadmap

## Intelligent Assessment

Evaluate learners across multiple cognitive dimensions.

---

## Learning Analytics

Track learner growth over time.

---

## Cognitive Skills Curriculum

Expand beyond problem reframing into:

- Systems Thinking
- First-Principles Thinking
- Tradeoff Analysis
- Root Cause Analysis
- Decision Making

---

## Product Experience

Add:

- Progress tracking
- Daily challenges
- Achievement badges
- User profiles
- Learning history

---

# Guiding Principle

Every new feature should answer one question:

> Does this help the learner become a better thinker?

If the answer is no, the feature should be reconsidered.

---

# Long-Term Vision

Evolve Problem Reframing Coach into a broader AI-powered cognitive coaching platform capable of supporting:

- Students
- Teachers
- Workforce learners
- Leadership development
- Professional learning

The ultimate goal is to demonstrate that AI can be used not only to answer questions, but to improve human reasoning.