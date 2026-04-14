# 🛡️ AI Moderation Pipeline

An AI-powered, event-driven system for monitoring and moderating comments across multiple platforms (Instagram, YouTube, Google Reviews, etc.).

Built as a real-world DevOps + backend project to demonstrate:

* event-driven architecture
* async processing with queues
* AI integration for classification
* scalable system design

---

## 🚀 Overview

Managing comments and reviews across multiple platforms is time-consuming and error-prone. This project automates:

1. **Ingesting comments** from external platforms
2. **Classifying content** using AI (spam, toxic, neutral)
3. **Applying moderation rules**
4. **Triggering alerts** for human review
5. **Storing results** for future analysis

---

## 🧱 Architecture

```
[Webhook / Polling]
        ↓
   FastAPI API
        ↓
     Redis Queue
        ↓
     Worker Service
        ↓
   AI Classification
        ↓
    Rules Engine
        ↓
   Actions (Slack Alerts)
        ↓
     PostgreSQL
```

---

## ⚙️ Tech Stack

| Layer            | Technology     |
| ---------------- | -------------- |
| API              | FastAPI        |
| Queue            | Redis          |
| Worker           | Python         |
| AI               | OpenAI API     |
| Database         | PostgreSQL     |
| Alerts           | Slack Webhooks |
| Containerization | Docker         |

---

## ✅ Current Features (MVP)

* 🔌 Webhook endpoint for incoming comments
* 📬 Queue-based processing (Redis)
* 🤖 AI classification:

  * Spam
  * Toxic
  * Neutral
* ⚖️ Rule-based decision engine
* 🔔 Slack alerts for flagged comments
* 🗄️ Persistent storage in PostgreSQL
* 🐳 Fully containerized with Docker Compose

---

## 🧪 Example Flow

1. A comment is received via webhook:

```json
{
  "platform": "instagram",
  "text": "This product is garbage and a scam"
}
```

2. The system:

   * pushes it to a queue
   * classifies it using AI
   * evaluates rules
   * sends a Slack alert if needed
   * stores the result in the database

---

## ▶️ Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/ai-moderation-pipeline.git
cd ai-moderation-pipeline
```

---

### 2. Set environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_key
SLACK_WEBHOOK_URL=your_webhook
DATABASE_URL=postgresql://postgres:postgres@db:5432/moderation
REDIS_URL=redis://redis:6379
```

---

### 3. Run the project

```bash
docker-compose up --build
```

---

### 4. Test the webhook

```bash
curl -X POST http://localhost:8000/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "instagram",
    "text": "This product is garbage and a scam"
  }'
```

---

## 📁 Project Structure

```
app/
├── main.py          # FastAPI entrypoint
├── queue.py         # Redis queue logic
├── worker.py        # Background processing loop
├── classifier.py    # AI moderation logic
├── rules.py         # Rule evaluation
├── actions.py       # Alerts (Slack)
└── db.py            # Database models & persistence
```

---

## 🧭 Roadmap (Planned Features)

### 🔌 Platform Integrations

* [ ] Meta (Instagram/Facebook) Webhooks
* [ ] YouTube polling service
* [ ] Google Reviews ingestion

---

### 🤖 Smarter AI Moderation

* [ ] Multi-label classification (spam, hate, complaint, etc.)
* [ ] Sentiment scoring
* [ ] Language detection + auto-translation
* [ ] Confidence calibration / threshold tuning

---

### ⚙️ Automation & Actions

* [ ] Auto-hide/delete comments via APIs
* [ ] Auto-reply to customer complaints
* [ ] Escalation workflows (high-risk alerts)

---

### 📊 Dashboard & Analytics

* [ ] Web UI for reviewing comments
* [ ] Filtering (platform, sentiment, date)
* [ ] Trends (negative sentiment over time)
* [ ] Response time tracking

---

### ☁️ DevOps & Production

* [ ] Terraform infrastructure (AWS)
* [ ] CI/CD pipeline (GitHub Actions)
* [ ] Distributed workers (horizontal scaling)
* [ ] Observability (logs, metrics, tracing)

---

## 💡 Future Vision

This project is evolving toward a **real-time Trust & Safety platform**, capable of:

* monitoring brand reputation across platforms
* detecting harmful or high-risk content
* enabling rapid human response
* providing actionable insights from user feedback

---

## 📚 Documentation

- [Project Context](docs/PROJECT_CONTEXT.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Tasks & Roadmap](docs/TASKS.md)

---

## 🤝 Contributing

This is currently a personal/portfolio project, but contributions and ideas are welcome.

---

## 📄 License

MIT License
