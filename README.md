[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

# 🦾 PhysiDigital™ — Open-Source Physiotherapy Data Intelligence System

**Objective**  
Develop an open-source system for physiotherapy data analytics, motion tracking, and rehabilitation prediction using AI — promoting smarter and safer digital health experiences.

This repository is portfolio-grade evidence of applied AI and data analytics for the EB2-NIW portfolio.

---

## 🚀 Features
- Real-time posture tracking and motion capture (OpenPose + MediaPipe)
- AI-driven injury prediction and recovery timeline estimation
- Secure storage (AES-256) for anonymized patient data
- REST API with FastAPI + Docker + CI
- CSV data ingestion and analytics dashboard (Plotly/Dash)

---

## 🧠 Tech Stack
Python 3.11 • FastAPI • TensorFlow • scikit-learn • MediaPipe • Plotly • Docker • GitHub Actions

---

## ▶️ Quickstart
```bash
git clone https://github.com/paulobiao/PhysiDigital.git
cd PhysiDigital
pip install -r requirements.txt
uvicorn src.main:app --reload

docker build -t physidigital:0.1.0 .
docker run -p 8080:8080 physidigital:0.1.0

🔒 Security & Compliance Notes
	•	Example-only dataset; no real PHI.
	•	Demonstrates HIPAA principles: confidentiality, integrity, and accountability.
	•	Encryption keys are generated locally for testing and education purposes.

⸻

🧩 EB2-NIW Mapping (How this supports your petition)
	•	National Importance: strengthens U.S. healthcare cybersecurity and privacy compliance.
	•	Well Positioned: demonstrates applied knowledge in encryption, RBAC, and auditing.
	•	On Balance: contributes open-source resources to improve data protection in healthcare.

⸻

📌 Next Steps (good for portfolio)
	•	Add JWT authentication and key rotation.
	•	Integrate FHIR schema validation for health data.
	•	Publish Grafana dashboards for audit event visualization.
---

## 🏙️ PHYSIDIGITAL™ — Copie tudo abaixo e cole no README.md do repositório *PhysiDigital*

```markdown
# PhysiDigital™ – Infrastructure & IoT Threat Monitoring System (Open Source)

**Objective:** Monitor IoT and OT (Operational Technology) environments to detect physical and digital anomalies through AI-driven analytics, strengthening cybersecurity in critical infrastructure sectors.

> This repository is designed as **portfolio-grade evidence** of infrastructure security expertise for **EB2-NIW**. It demonstrates anomaly detection, IoT telemetry analysis, and secure data pipelines for industrial systems.

---

## ✨ Features
- **IoT/OT telemetry collection** using FastAPI and MQTT integration
- **AI-based anomaly detection** (scikit-learn model demo)
- **Secure logging** and event correlation system
- **Dockerized** for easy deployment across edge or cloud systems
- **Continuous Integration** with GitHub Actions CI
- MIT License

---

## 🏗️ Architecture

```mermaid
flowchart LR
A[Sensors / IoT Devices] -->|MQTT / HTTPS| B[PhysiDigital Collector]
B --> C[AI Anomaly Engine (scikit-learn)]
B --> D[(PostgreSQL / InfluxDB)]
B --> E[Monitoring Dashboard]
🚀 Quick Start

Using Docker (recommended)
docker compose up --build
# API at http://localhost:8080/docs

Local (Python 3.11+)
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
uvicorn physidigital.main:app --reload --port 8080

uvicorn physidigital.main:app --reload --port 8080

🧪 Tests
pytest -q

📁 Project Layout
src/
  physidigital/
    main.py         # FastAPI app
    sensors.py      # IoT data ingestion
    analytics.py    # AI anomaly detection
    models.py       # data schemas
  tests/
    test_sensors.py
    test_analytics.py
data/
  sample_signals.csv
docs/
  system_topology.md
.github/workflows/ci.yml
Dockerfile
docker-compose.yml
requirements.txt
LICENSE
README.md
