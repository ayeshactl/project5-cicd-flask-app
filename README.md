# Automated CI/CD Pipeline for Flask Application 🚀

## Overview

This project demonstrates an end-to-end CI/CD pipeline for a Flask application using Jenkins, Docker, Docker Hub, and AWS EC2.

The pipeline automatically builds, tests, containerizes, pushes the Docker image, and deploys the application whenever code is pushed to GitHub.

---

# Architecture
Developer
|
| Git Push
↓
GitHub Repository
|
| GitHub Webhook Trigger
↓
Jenkins CI/CD Server (AWS EC2)
|
|---- Checkout Code
|---- Install Dependencies
|---- Run Tests
|---- Build Docker Image
|---- Push Image
↓
Docker Hub Registry
|
↓
AWS EC2 Docker Container
|
↓
Flask Application


---

# Tech Stack

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

1. Developer pushes application code to GitHub.

2. GitHub Webhook automatically triggers Jenkins.

3. Jenkins executes the complete pipeline:
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

## 1. Checkout

Jenkins pulls the latest application code from the GitHub repository.

---

## 2. Install Dependencies

Jenkins installs required Python packages.

Command:

```bash
pip3 install -r requirements.txt
```
3. Run Tests

The pipeline validates that the Flask application loads successfully.

Command:

```bash
python3 -c "import app; print('Flask app import successful')"
```
Expected output:

Flask app import successful

4. Build Docker Image

Jenkins creates a Docker image from the Flask application.

Command:
```bash
docker build -t project5-flask-app .
```
5. Push Docker Image

Jenkins securely authenticates with Docker Hub using stored Jenkins credentials.

Docker image format:

ayeshairam/project5-flask-app:<build-number>

Example:

ayeshairam/project5-flask-app:11

6. Deploy Flask Container

Jenkins automatically removes the previous container and deploys the latest Docker image on AWS EC2.

Command:
docker stop project5-flask-container || true

docker rm project5-flask-container || true

docker run -d \
--name project5-flask-container \
-p 5000:5000 \
project5-flask-app

GitHub Webhook Automation

The pipeline runs automatically whenever code is pushed to GitHub.

Workflow:
Developer Push
        |
        ↓
GitHub Webhook
        |
        ↓
Jenkins Pipeline Starts
        |
        ↓
Docker Image Build
        |
        ↓
Application Deployment

Docker Hub Integration

Docker images are automatically pushed to Docker Hub.

Repository:
ayeshairam/project5-flask-app

Each Jenkins build creates a unique image tag.

Example:

Build 10
Build 11
Build 12

AWS EC2 Deployment

The Flask application runs inside a Docker container on an AWS EC2 instance.

Container verification:

docker ps

Running application:

http://<EC2-Public-IP>:5000

Screenshots & Proofs
Jenkins Pipeline Success

GitHub Webhook Trigger

Docker Hub Image

Running Container on EC2

Flask Application Running

How to Run Locally

Clone repository:

git clone https://github.com/ayeshactl/project5-cicd-flask-app.git

Navigate to project:

cd project5-cicd-flask-app

Build Docker image:

docker build -t flask-app .

Run container:

docker run -p 5000:5000 flask-app

Open:

http://localhost:5000
Future Improvements
Add automated unit testing using PyTest
Deploy application using Kubernetes
Add monitoring using Prometheus and Grafana
Use AWS ECR instead of Docker Hub
