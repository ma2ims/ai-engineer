# AI Engineer Learning Roadmap

This roadmap is designed to help learners move from basic software engineering foundations into practical AI engineering.

---

## Level 1 — Foundation

Goal: understand the basic technical skills needed before building AI applications.

Topics:

- Python basic
- JSON basic
- API basic
- Git basic
- Database basic
- Linux command
- Docker basic

Main project:

```txt
projects/daily-report-api
```

Expected outcome:

- create a simple FastAPI backend
- accept JSON request body
- return JSON response
- save data to SQLite
- run with Docker Compose
- version code with Git

---

## Level 2 — LLM Application

Goal: build applications that use LLM APIs in a controlled way.

Topics:

- LLM API request and response
- prompt template
- system prompt
- structured output
- chat history
- streaming response
- error handling
- token and cost logging

Example project:

```txt
projects/llm-chat-api
```

---

## Level 3 — RAG System

Goal: build AI applications that answer based on documents or knowledge base.

Topics:

- document ingestion
- chunking
- embeddings
- vector database
- semantic search
- retrieval
- citation/source reference
- answer generation with context

Example project:

```txt
projects/rag-knowledge-api
```

---

## Level 4 — AI Agent and Workflow

Goal: build AI systems that can use tools and execute multi-step workflows.

Topics:

- tool calling
- function calling
- workflow orchestration
- agent memory
- approval flow
- task execution
- error recovery

Example project:

```txt
projects/ai-agent-workflow
```

---

## Level 5 — Production AI System

Goal: prepare AI systems for real usage.

Topics:

- deployment
- CI/CD
- monitoring
- logging
- evaluation
- prompt versioning
- fallback model
- cost control
- security

Example project:

```txt
projects/production-ai-assistant
```

---

## Suggested Learning Rhythm

```txt
30% concept
70% practice
```

Daily routine:

```txt
1. Read one concept
2. Type the example manually
3. Run the code
4. Modify the code
5. Fix errors
6. Commit the result
7. Write a short learning note
```

---

## Completion Rule

A level is considered complete when:

- the project runs locally
- the project runs with Docker
- the README is clear
- the code is committed to Git
- the learner can explain what each file does
