# Automated CI/CD Pipeline for Flask Application 🚀

## Overview

This project demonstrates an end-to-end CI/CD pipeline for a Flask application using Jenkins, Docker, Docker Hub, and AWS EC2.

The pipeline automatically builds, tests, containerizes, pushes the Docker image, and deploys the application whenever code is pushed to GitHub.

---

## Architecture
Developer
|
| Git Push
↓
GitHub Repository
|
| Webhook Trigger
↓
Jenkins CI/CD Server
|
|---- Checkout Code
|---- Install Dependencies
|---- Run Tests
|---- Build Docker Image
|---- Push Image
↓
Docker Hub
|
↓
AWS EC2 Docker Container
|
↓
Flask Application



---

## Tech Stack

| Tool | Purpose |
|---|---|
| AWS EC2 | Cloud server hosting |
| Jenkins | CI/CD automation |
| GitHub | Source code management |
| GitHub Webhook | Automatic build trigger |
| Docker | Application containerization |
| Docker Hub | Docker image registry |
| Flask | Web application |

---

# CI/CD Workflow

1. Developer pushes code to GitHub

2. GitHub webhook automatically triggers Jenkins

3. Jenkins executes pipeline:
Checkout
↓
Install Dependencies
↓
Run Tests
↓
Build Docker Image
↓
Push Image to Docker Hub
↓
Deploy Container on EC2


---

# Jenkins Pipeline Stages

### Checkout
Pulls the latest application code from GitHub.

### Install Dependencies
Installs Python packages:

```bash
pip3 install -r requirements.txt

Testing

Verifies Flask application:
python3 -c "import app"

Docker Build

Creates Docker image:
docker build -t project5-flask-app .

Docker Hub Push

Jenkins securely logs into Docker Hub and pushes versioned images:

ayeshairam/project5-flask-app:<build-number>
Deployment

Jenkins automatically replaces the old container with the latest version:

docker run -d \
--name project5-flask-container \
-p 5000:5000 \
project5-flask-app
