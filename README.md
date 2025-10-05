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


🌿 Step-by-Step: Create a new branch & raise a Pull Request (PR)
🧩 1️⃣ Check current branch
git branch

🌿 2️⃣ Create a new branch
git checkout -b feature/update-readme

🔹 feature/update-readme ek example branch name hai.
Aap apna context-specific naam rakh sakte ho — jaise feature/docker-fix ya bugfix/k8s-service.

📝 3️⃣ Add and commit changes
git add .
git commit -m "Updated README and Dockerfile setup for FastAPI"

🚀 4️⃣ Push the new branch to GitHub
git push -u origin feature/update-readme

🌐 5️⃣ Go to GitHub repository
Ab GitHub par jao →
Aapko ek banner milega:
“Compare & pull request”

Click that button ✅
🔄 6️⃣ Create Pull Request (PR)
Add a title (example: Update README and Docker setup)
Add a small description
Base branch: main
Compare branch: feature/update-readme
Click Create Pull Request

🧠 7️⃣ (Optional) Review & Merge
PR review hone ke baad, click Merge Pull Request
Finally, delete the feature branch if you want.

⚙️ Summary
Step	Command / Action	Description
1	git checkout -b feature/update-readme	Create new branch
2	git add . & git commit -m "message"	Save local changes
3	git push -u origin feature/update-readme	Push branch
4	Create Pull Request on GitHub	Merge changes into main