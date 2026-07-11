# AI Full Stack Monorepo

[![Backend CI](https://github.com/debraj-ghosh/ai-fullstack-monorepo/actions/workflows/backend-ci.yml/badge.svg)](https://github.com/debraj-ghosh/ai-fullstack-monorepo/actions/workflows/backend-ci.yml)

A production-ready Full Stack AI application built using modern technologies including **React, FastAPI, PostgreSQL, Redis, Docker, Kubernetes, GitHub Actions, and AWS**.


## Build Status

[![Backend CI](https://github.com/debraj-ghosh/ai-fullstack-monorepo/actions/workflows/backend-ci.yml/badge.svg)](https://github.com/debraj-ghosh/ai-fullstack-monorepo/actions/workflows/backend-ci.yml)

[![Frontend CI](https://github.com/debraj-ghosh/ai-fullstack-monorepo/actions/workflows/frontend-ci.yml/badge.svg)](https://github.com/debraj-ghosh/ai-fullstack-monorepo/actions/workflows/frontend-ci.yml)

[![Docker Build](https://github.com/debraj-ghosh/ai-fullstack-monorepo/actions/workflows/docker-build.yml/badge.svg)](https://github.com/debraj-ghosh/ai-fullstack-monorepo/actions/workflows/docker-build.yml)

[![Security Scan](https://github.com/debraj-ghosh/ai-fullstack-monorepo/actions/workflows/security-scan.yml/badge.svg)](https://github.com/debraj-ghosh/ai-fullstack-monorepo/actions/workflows/security-scan.yml)

---

# Project Overview

This project is designed as a real-world enterprise-grade Full Stack AI application.

The objective is to learn and implement modern software engineering practices while building an application that is scalable, maintainable, cloud-ready, and AI-enabled.

The project follows a Monorepo architecture containing:

- React Frontend
- FastAPI Backend
- PostgreSQL Database
- Redis Cache
- Docker Containers
- Kubernetes Deployment
- GitHub Actions CI/CD
- AWS Deployment
- AI Features (Upcoming)

---

# Architecture

```
                    React + Vite
                          │
                       Axios API
                          │
                    FastAPI Backend
                          │
          ┌───────────────┴───────────────┐
          │                               │
      Redis Cache                  PostgreSQL
          │                               │
          └───────────────┬───────────────┘
                          │
                    SQLAlchemy ORM
                          │
                     Alembic Migrations
```

---

# Tech Stack

| Category | Technology |
|-----------|------------|
| Frontend | React 19 + Vite |
| Backend | Python 3.13 + FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Database Migrations | Alembic |
| Cache | Redis |
| Authentication | JWT |
| Containerization | Docker |
| Container Orchestration | Kubernetes |
| CI/CD | GitHub Actions |
| Cloud | AWS (Upcoming) |
| AI | LangChain, LangGraph, MCP, OpenAI (Upcoming) |

---

# Repository Structure

```
ai-fullstack-monorepo/

├── apps/
│   ├── frontend/
│   └── backend/
│
├── .github/
│   └── workflows/
│       ├── backend-ci.yml
│       ├── frontend-ci.yml
│       ├── docker-build.yml
│       ├── security-scan.yml
│       ├── deploy-dev.yml
│       └── deploy-prod.yml
│
├── docker-compose.yml
├── docker-compose.dev.yml
├── docker-compose.prod.yml
│
└── README.md
```

---

# Features Implemented

- Monorepo Architecture
- React Frontend
- FastAPI Backend
- REST APIs
- PostgreSQL Integration
- SQLAlchemy ORM
- Alembic Database Migrations
- Redis Caching
- JWT Authentication
- Docker Containerization
- Docker Compose
- GitHub Actions CI

---

# Project Setup

## Clone Repository

```bash
git clone https://github.com/debraj-ghosh/ai-fullstack-monorepo.git

cd ai-fullstack-monorepo
```

---

## Start the Project

Development

```bash
docker compose -f docker-compose.dev.yml up --build
```

Production

```bash
docker compose -f docker-compose.prod.yml up --build
```

---

# Database Migrations

Generate Migration

```bash
docker compose exec backend alembic revision --autogenerate -m "Description"
```

Apply Migration

```bash
docker compose exec backend alembic upgrade head
```

Current Version

```bash
docker compose exec backend alembic current
```

Migration History

```bash
docker compose exec backend alembic history
```

Rollback One Migration

```bash
docker compose exec backend alembic downgrade -1
```

Rollback to Base

```bash
docker compose exec backend alembic downgrade base
```

---

# Docker Commands

Build Containers

```bash
docker compose build
```

Start Containers

```bash
docker compose up -d
```

Stop Containers

```bash
docker compose down
```

View Logs

```bash
docker compose logs -f
```

Open Backend Shell

```bash
docker compose exec backend bash
```

Open PostgreSQL

```bash
docker compose exec postgres psql -U postgres
```

Open Redis CLI

```bash
docker compose exec redis redis-cli
```

---

# GitHub Actions

The project includes GitHub Actions workflows for:

- Backend CI
- Frontend CI
- Docker Image Build
- Security Scanning
- Development Deployment (Planned)
- Production Deployment (Planned)

---

# Roadmap

## Completed

- Monorepo
- React
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Redis
- JWT Authentication
- Docker
- GitHub Actions

---

## In Progress

- Kubernetes
- Observability
- AWS Deployment

---

## Planned

- File Uploads
- Automated Testing
- LangChain
- LangGraph
- MCP Server
- AI Agents
- OpenAI Integration
- Production Hardening

---

# Learning Goals

This repository is being developed as a hands-on learning project covering:

- Enterprise Software Architecture
- Full Stack Development
- Backend API Development
- Database Design
- Cloud Native Applications
- Kubernetes
- CI/CD
- AI Engineering
- Agentic AI
- Production Deployment

---

# Author

**Debraj Ghosh**

Software Engineer | AI Enthusiast | Full Stack Developer

GitHub: https://github.com/debraj-ghosh

---

# License

This project is licensed under the MIT License.