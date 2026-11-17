
# AWS Microservices CI/CD Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI-green)
![Tests](https://img.shields.io/badge/API_Tests-4_Passed-brightgreen)

## Project Overview

A hands-on DevOps project demonstrating the development, containerization, testing, and continuous integration of Python-based microservices using Docker, Docker Compose, GitHub Actions, and Pytest.

The project automates building containers, starting services, verifying API health, and running automated tests.

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend microservices |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| GitHub Actions | CI automation |
| Pytest | Automated API testing |
| Requests | HTTP API testing |
| Git & GitHub | Version control |

## Project Architecture

```text
               Developer
                   |
                Git Push
                   |
            GitHub Repository
                   |
             GitHub Actions
                   |
             CI/CD Workflow
                   |
             Docker Build
                   |
             Docker Compose
                   |
          ---------------------
          |                   |
     User Service       Product Service
       Port 5001           Port 5002
          |                   |
       /health              /health
          |                   |
          ---------------------
                   |
             Pytest Suite
                   |
            Pass / Fail
```

## Microservices

### User Service

Runs on port `5001`.

Health endpoint:

`http://127.0.0.1:5001/health`

Example response:

```json
{
  "service": "user-service",
  "status": "healthy"
}
```

### Product Service

Runs on port `5002`.

Health endpoint:

`http://127.0.0.1:5002/health`

Example response:

```json
{
  "service": "product-service",
  "status": "healthy"
}
```

## Project Structure

```text
aws-microservices-final/
|
|-- .github/
|   |-- workflows/
|
|-- services/
|   |-- user-service/
|   |-- product-service/
|
|-- tests/
|   |-- test_apis.py
|
|-- compose.yaml
|-- .gitignore
|-- README.md
```

## Getting Started

### Prerequisites

Install:

- Python 3
- Docker Desktop
- Git

### Clone Repository

```bash
git clone https://github.com/sherafganzafar/aws-microservices-cicd.git
cd aws-microservices-cicd
```

### Build and Start Containers

```bash
docker compose up -d --build
```

### Check Running Containers

```bash
docker ps
```

### Verify API Health

Open these URLs in your browser:

User Service:

http://127.0.0.1:5001/health

Product Service:

http://127.0.0.1:5002/health

Both services should return a healthy status.

## Automated API Testing

Install test dependencies:

```bash
python -m pip install pytest requests
```

Run automated tests:

```bash
python -m pytest tests/ -v
```

### Test Cases

| Test | Observed Result |
|------|-----------------|
| User Service Health | PASSED |
| Users API | PASSED |
| Product Service Health | PASSED |
| Products API | PASSED |

Latest observed local test execution:

**4 passed in 3.52 seconds**

## GitHub Actions CI Pipeline

The project uses GitHub Actions to automate continuous integration.

### Pipeline Steps

1. Checkout source code
2. Prepare the build environment
3. Build Docker images
4. Start microservices
5. Wait for healthy API responses
6. Execute automated API tests
7. Clean up containers
8. Report workflow status

### CI Status

A GitHub Actions workflow run was successfully completed.

View the workflow:

https://github.com/sherafganzafar/aws-microservices-cicd/actions

## Stop Containers

```bash
docker compose down
```

## Future Improvements

- Deploy microservices to AWS EC2 or ECS
- Push Docker images to Amazon ECR
- Integrate vulnerability scanning
- Add monitoring with Prometheus and Grafana
- Implement continuous deployment
- Add infrastructure automation with Terraform

## Learning Outcomes

This project demonstrates practical experience with:

- Docker containerization
- Microservices architecture
- CI pipeline configuration
- Automated API testing
- GitHub Actions workflows
- Troubleshooting container environments
- Git-based development workflows

## Author

**Sherafgan Zafar**

BS Information Technology — University of the Punjab (2025)

Career Focus: DevOps | DevSecOps | Cloud Engineering | Cloud Security

GitHub: https://github.com/sherafganzafar

---

**Project Status:** Local Docker services and automated tests verified successfully. Continuous integration verified through GitHub Actions. AWS deployment is planned as a future enhancement.
