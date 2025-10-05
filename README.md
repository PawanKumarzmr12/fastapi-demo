🐍 FastAPI Demo — Docker + Kubernetes Setup

✨ Author
   Pawan Kumar
📧 pawanzmr15@gmail.com
📘 Overview

This project is a FastAPI application containerized using Docker and deployable on Kubernetes (Minikube or Cloud K8s).
It demonstrates how to build, run, and deploy a simple API service using modern DevOps practices

⚙️ Tech Stack
    Python 3.12
    FastAPI
    Poetry (for dependency management)
    Docker
    Kubernetes / Minikube

📁 Project Structure

    fastapi-demo/
├── app/
│   ├── main.py
│   └── __init__.py
├── pyproject.toml
├── poetry.lock
├── Dockerfile
├── k8s/
│   ├── fastapi-deployment.yaml
│   └── fastapi-service.yaml
└── README.md

🚀 1. Run Locally (without Docker)
# Install dependencies
poetry install

# Run FastAPI app
poetry run uvicorn app.main:app --reload

Open in browser:
👉 http://localhost:8000

🐳 2. Run with Docker
# Build Docker image
docker build -t fastapi-demo .

# Run container
docker run -d --name fastapi-demo-container -p 8000:8000 fastapi-demo

# Check container logs:
docker logs fastapi-demo-container

