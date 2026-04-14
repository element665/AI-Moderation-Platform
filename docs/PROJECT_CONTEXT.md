# Project Context

## 📚 Documentation

- [Project Context](docs/PROJECT_CONTEXT.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Tasks & Roadmap](docs/TASKS.md)

## What this project does
AI moderation pipeline for social media comments:
- ingestion → queue → AI classification → rules → alerts → DB

## Current status (MVP)
- FastAPI webhook working
- Redis queue working
- Worker processes comments
- OpenAI classification integrated
- Slack alerts working
- PostgreSQL storage working

## Key design decisions
- Event-driven architecture
- Modular monolith (not microservices yet)
- Rules-based moderation (not hardcoded)

## Constraints
- Keep things simple (no overengineering)
- Avoid breaking working pipeline
- Prefer small, incremental changes

## Known issues
- JSON parsing implemented but needs validation and edge case handling
- no retry logic
- minimal logging
