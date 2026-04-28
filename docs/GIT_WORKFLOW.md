# Git Workflow Guide

This document explains the recommended Git workflow for this learning repository.

---

## Clone Repository

```bash
git clone https://github.com/ma2ims/ai-engineer.git
cd ai-engineer
```

---

## Basic Daily Workflow

Check status:

```bash
git status
```

Create or edit files, then stage changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Learn Python basic"
```

Push changes:

```bash
git push origin main
```

---

## Recommended Branch Workflow

Create a learning branch:

```bash
git checkout -b learning/level-01-foundation
```

Work on the branch, then commit:

```bash
git add .
git commit -m "Complete Level 1 daily report API"
```

Push the branch:

```bash
git push origin learning/level-01-foundation
```

---

## Commit Message Pattern

Use clear commit messages.

Recommended format:

```txt
<type>: <short description>
```

Examples:

```txt
docs: add Python basic notes
feat: add daily report create endpoint
fix: handle missing report id
chore: add docker compose setup
refactor: split database logic
```

Common types:

```txt
docs     = documentation changes
feat     = new feature
fix      = bug fix
chore    = maintenance/config
refactor = code improvement without changing behavior
test     = testing changes
```

---

## Pull Latest Changes

Before working:

```bash
git pull origin main
```

---

## View History

```bash
git log --oneline
```

---

## Undo Local Changes Carefully

Discard changes in one file:

```bash
git checkout -- path/to/file
```

Reset staged file:

```bash
git reset path/to/file
```

Avoid using destructive commands unless you understand them:

```bash
git reset --hard
git clean -fd
```

---

## Learning Rule

Commit small progress often.

Good:

```txt
feat: add health check endpoint
feat: add create report endpoint
feat: save report to sqlite
```

Not ideal:

```txt
final update
many changes
fix all
```
