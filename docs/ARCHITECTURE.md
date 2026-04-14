# Architecture

Flow:
Webhook → Queue → Worker → AI → Rules → Actions → DB

Components:
- FastAPI: ingestion
- Redis: queue
- Worker: processing loop
- Classifier: AI logic
- Rules: decision engine
- Actions: Slack alerts
- DB: persistence

Important:
- All components are loosely coupled
- Queue is the central buffer