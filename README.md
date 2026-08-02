# Automated CI/CD Pipeline for Flask Application 🚀

## Overview

This project demonstrates an end-to-end CI/CD pipeline for a Flask application using Jenkins, Docker, Docker Hub, and AWS EC2.

The pipeline automatically builds, tests, containerizes, pushes the Docker image, and deploys the application whenever code is pushed to GitHub.

---

## Architecture

```text
Developer
    |
    | Git Push
    ↓
GitHub Repository
    |
    | Webhook Trigger
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

Tech Stack
Tool	Purpose
AWS EC2	Cloud server hosting
Jenkins	CI/CD automation
GitHub	Source code management
GitHub Webhook	Automatic build trigger
Docker	Application containerization
Docker Hub	Docker image registry
Flask	Web application
CI/CD Workflow
Developer pushes application code to GitHub.
GitHub Webhook automatically triggers Jenkins.
Jenkins executes the complete pipeline:
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
Jenkins Pipeline Stages
1. Checkout

Jenkins pulls the latest source code from the GitHub repository.

2. Install Dependencies

Installs required Python packages:

pip3 install -r requirements.txt
3. Run Tests

Validates that the Flask application loads successfully:

python3 -c "import app; print('Flask app import successful')"
4. Build Docker Image

Jenkins creates a Docker image from the application:

docker build -t project5-flask-app .
5. Push Docker Image

Jenkins securely authenticates with Docker Hub using stored credentials and pushes the image.

Docker image format:

ayeshairam/project5-flask-app:<build-number>

Example:

ayeshairam/project5-flask-app:11
6. Deploy Flask Container

Jenkins automatically removes the previous container and deploys the latest Docker image on AWS EC2.

docker stop project5-flask-container || true

docker rm project5-flask-container || true

docker run -d \
--name project5-flask-container \
-p 5000:5000 \
project5-flask-app
GitHub Webhook Automation

The pipeline does not require manual execution.

Whenever code is pushed:

Developer Push
       |
       ↓
GitHub Webhook
       |
       ↓
Jenkins Pipeline Starts Automatically
       |
       ↓
Application Deployment
Docker Hub Integration

Docker images are automatically pushed to Docker Hub.

Repository:
ayeshairam/project5-flask-app

Each Jenkins build creates a new version tag:

Build 10
Build 11
AWS EC2 Deployment

The Flask application runs inside a Docker container on an AWS EC2 instance.

Running container verification:

docker ps

Application URL:

http://<EC2-Public-IP>:5000
