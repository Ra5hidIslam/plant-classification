# 🌿 House‑Plant Classifier

A lightweight, end‑to‑end **AI micro‑service** that recognises common house plants from images and returns care information.  
Ideal for developers who want a no‑frills example of how to take a computer‑vision model built on kaggle  **all the way to a full‑stack Docker deployment**.

---

## ✨ Key Features

| Feature | Why it matters |
|---------|----------------|
| **Transfer‑learned EfficientNet‑B0 model** | High accuracy with modest compute |
| **Three‑service architecture** | Mirrors real‑world ML deployments while staying easy to reason about |
| **Fully dockerised** | One‑command spin‑up; works the same on any machine |
| **REST API** | Simple, language‑agnostic integration |

---

## 🛠️ Tech Stack

* **Model Training**  – Kaggle Notebook · TensorFlow · EfficientNet‑B0
* **Frontend**       - React
* **AI Service**     – Python 3 · Flask  
* **DB Service**     – MongoDB 
* **File Service**   – Python3 · Flask
* **Orchestration**  – Docker & Docker Compose

---

## 🏗️ Architecture Overview

* **AI Service** – Receives an image → returns predicted `plant_id`.
* **DB Service** – Given `plant_id` → returns JSON with image paths & description.
* **File Service** – Serves the images referenced in that JSON.

---

## 🚀 Quick Start

### 1. Clone & Configure

```bash
git clone https://github.com/<your‑handle>/house‑plant‑classifier.git
cd house‑plant‑classifier
cp .env.example .env            # fill in custom values if needed
```
* The data is not included here but can be downloaded from this link: https://www.kaggle.com/datasets/kacpergregorowicz/house-plant-species
* Please train the model by forking this Kaggle notebook : https://www.kaggle.com/code/rashid2048/house-plant-identifier-model-efficientnet

### 2. Build & Run Everything

```bash
docker compose up --build
```

---

## 📂 Repository Layout

```
.
├── ai_service/           # FastAPI app + saved model
├── db_service/           # MongoDB Dockerfile + seed script
├── file_service/         # NGINX conf & plant images
├── notebooks/            # Kaggle training + EDA
├── docker-compose.yml
└── README.md
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my‑idea`)
3. Commit your changes (`git commit -m "feat: add …"`)
4. Push and open a PR

Please lint with **ruff** & **black** before submitting.

---

## 📄 License

This project is licensed under the MIT License – see `LICENSE` for details.

---

> _Built with ☕ & plenty of plants_ 🌱

