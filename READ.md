# Cortex

A personal knowledge base with AI. Save notes and links, get automatic summaries and tags, and search by meaning instead of exact keywords.

> Status: in development (started September 2026).

## Planned features

- User registration and login (JWT)
- CRUD for notes and tags
- AI-generated summaries and tags
- Semantic search with pgvector
- Chat with your own notes (RAG)

## Stack

- **Backend:** Python 3.12, FastAPI, SQLAlchemy, Alembic, Pydantic
- **Database:** PostgreSQL 16 + pgvector
- **Infra:** Docker, Docker Compose
- **Frontend:** Next.js + TypeScript (planned)
- **AI:** LLM API + embeddings (planned)

## Running locally

### 1. Clone and configure

```bash
git clone git@github.com:jonatha-guzzo-dev/cortex.git
cd cortex
cp .env.example .env
```

### 2. Start the database

```bash
docker compose up -d
```

### 3. Start the API

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
fastapi dev app/main.py
```

- API: http://localhost:8000
- Swagger docs: http://localhost:8000/docs

## Project structure

```
cortex/
├── backend/
│   └── app/
│       ├── core/       # config, security
│       ├── models/     # SQLAlchemy tables
│       ├── schemas/    # Pydantic schemas
│       ├── routers/    # API routes
│       └── services/   # business logic
├── frontend/
├── docker-compose.yml
└── .env.example
```

## Roadmap

- [x] Week 1: setup, FastAPI hello world, Postgres with Docker
- [ ] Week 2: SQLAlchemy models, Alembic migrations, Dockerized API
- [ ] Weeks 3 to 5: CRUD, JWT, tags, tests
- [ ] Weeks 6 to 9: frontend and basic AI
- [ ] Weeks 10 to 13: pgvector, deploy, polish
