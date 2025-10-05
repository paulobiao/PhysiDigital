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
