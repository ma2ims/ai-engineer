# AI Engineer Learning Roadmap

A structured learning repository for building practical AI Engineering foundations.

This repo is designed for learners who want to understand AI Engineering from the ground up: programming, APIs, JSON, Git, databases, Linux, Docker, LLM applications, RAG systems, AI agents, and production-ready AI workflows.

> Current focus: **Level 1 — Foundation**

---

## Learning Goal

The goal of this repository is not only to learn theory, but to build real, runnable projects step by step.

By following this repo, learners should be able to:

- write basic Python programs
- build simple backend APIs
- work with JSON request/response data
- use Git and GitHub for version control
- store data in a database
- use Linux terminal commands
- run applications with Docker
- prepare for LLM application development

---

## Repository Structure

```txt
ai-engineer/
├── docs/                       # General learning documentation
│   ├── ROADMAP.md
│   ├── VERSIONING.md
│   ├── GIT_WORKFLOW.md
│   └── DOCKER_GUIDE.md
│
├── modules/                    # Learning modules by level
│   └── level-01-foundation/
│       ├── README.md
│       ├── 01-python-basic.md
│       ├── 02-json-basic.md
│       ├── 03-api-basic.md
│       ├── 04-git-basic.md
│       ├── 05-database-basic.md
│       ├── 06-linux-command.md
│       └── 07-docker-basic.md
│
├── projects/                   # Hands-on learning projects
│   └── daily-report-api/
│       ├── app/
│       │   ├── __init__.py
│       │   ├── main.py
│       │   ├── database.py
│       │   └── models.py
│       ├── README.md
│       ├── requirements.txt
│       ├── Dockerfile
│       ├── docker-compose.yml
│       └── .env.example
│
├── scripts/                    # Utility scripts
│   └── check.sh
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .gitignore
├── Makefile
└── README.md
```

---

## Learning Levels

### Level 1 — Foundation

Core skills before building AI applications:

- Python basic
- API basic
- Git
- JSON
- Database basic
- Linux command
- Docker basic

Project:

```txt
Daily Report API
```

A simple FastAPI backend for recording daily operational reports using JSON, SQLite, Git, and Docker.

---

### Level 2 — LLM Application

Coming next:

- LLM API integration
- prompt templates
- structured output
- chat history
- error handling
- token and cost logging

---

### Level 3 — RAG System

Coming next:

- document ingestion
- chunking
- embeddings
- vector database
- retrieval
- source-based answer generation

---

### Level 4 — AI Agent and Workflow

Coming next:

- tool calling
- workflow orchestration
- memory
- task execution
- human approval flow

---

### Level 5 — Production AI System

Coming next:

- deployment
- monitoring
- evaluation
- logging
- fallback model
- CI/CD
- LLMOps

---

## Quick Start

Clone the repository:

```bash
git clone https://github.com/ma2ims/ai-engineer.git
cd ai-engineer
```

Open the Level 1 module:

```bash
cd modules/level-01-foundation
```

Run the first project:

```bash
cd ../../projects/daily-report-api
docker compose up --build
```

Open API docs:

```txt
http://localhost:8000/docs
```

---

## Recommended Learning Flow

```txt
1. Read docs/ROADMAP.md
2. Study modules/level-01-foundation/README.md
3. Learn each topic one by one
4. Run projects/daily-report-api
5. Modify the project
6. Commit changes with Git
7. Push to your own GitHub repo
```

---

## How to Use This Repo as a Learner

Fork or clone this repository, then create your own learning branch:

```bash
git checkout -b learning/my-progress
```

After finishing a topic:

```bash
git add .
git commit -m "Learn Python basic"
git push origin learning/my-progress
```

---

## Project Philosophy

This repository follows a practical learning principle:

```txt
Understand the concept → type the code → run it → break it → fix it → document it
```

AI Engineering is not only about using AI tools. It is about building reliable systems around AI.

---

## Main Project in This Level

### Daily Report API

A simple API project that teaches:

- Python project structure
- FastAPI
- JSON request and response
- SQLite database
- Dockerfile
- Docker Compose
- Git workflow
- basic CI workflow

Open:

```txt
projects/daily-report-api/README.md
```

---

## Status

```txt
Level 1 Foundation: In progress
Level 2 LLM Application: Planned
Level 3 RAG System: Planned
Level 4 AI Agent: Planned
Level 5 Production AI System: Planned
```

---

## License

This repository is intended for personal and public learning. Add a formal license later if needed.
