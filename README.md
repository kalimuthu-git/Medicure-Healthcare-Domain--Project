# 🏥 Medicure Healthcare — DevOps Real-Time Project

![Project Status](https://img.shields.io/badge/Status-Live-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Jenkins](https://img.shields.io/badge/CI%2FCD-Jenkins-red)
![Python](https://img.shields.io/badge/Python-3.11-yellow)
![AWS](https://img.shields.io/badge/Cloud-AWS%20EC2-orange)

> A full-stack healthcare web application with a complete DevOps pipeline using **Flask + Docker + Jenkins + AWS EC2**.

---

## 🌐 Live Project URLs

| Service | URL |
|---------|-----|
| 🌍 Website | `http://43.205.211.204:9090` |
| 🔧 Jenkins | `http://43.205.211.204:8080` |
| 🐳 Docker Hub | `kalimuthudevops/medicure-healthcare-project:v1` |
| 📦 GitHub | `github.com/kalimuthu-git/Medicure-Healthcare-Domain--Project` |

---

## 📁 Project Structure

```
MEDICURE HEALTH CARE-PROJECT/
├── app.py                    # Flask backend — routes & API
├── requirements.txt          # Python dependencies
├── Dockerfile                # Multi-stage Docker image build
├── Jenkinsfile               # CI/CD Pipeline (all stages)
├── docker-compose.yml        # App + Nginx together
├── templates/
│   └── index.html            # Medicure frontend UI (HTML/CSS/JS)
├── nginx/
│   └── nginx.conf            # Nginx reverse proxy config
├── tests/
│   └── test_app.py           # Pytest unit tests (6 tests)
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python Flask |
| WSGI Server | Gunicorn |
| Reverse Proxy | Nginx |
| Containerization | Docker |
| CI/CD | Jenkins |
| Image Registry | Docker Hub |
| Cloud | AWS EC2 (c7i-flex.large) |
| Version Control | Git + GitHub |
| Testing | Pytest + pytest-flask |

---

## 🚀 Run Locally (Without Docker)

```bash
# 1. Clone the repo
git clone https://github.com/kalimuthu-git/Medicure-Healthcare-Domain--Project.git
cd Medicure-Healthcare-Domain--Project

# 2. Create virtual environment
python3 -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py

# 5. Open browser
# http://localhost:5000
```

---

## 🐳 Run With Docker

```bash
# Build the Docker image
docker build -t medicure-health-care:v1 .

# Run the container
docker run -d \
  --name medicure-container \
  -p 9090:5000 \
  medicure-health-care:v1

# Open browser
# http://localhost:9090

# Check running containers
docker ps

# Check logs
docker logs medicure-container
```

---

## 🐳 Run With Docker Compose (App + Nginx)

```bash
# Start all services
docker-compose up -d

# App  → http://localhost:5000
# Nginx → http://localhost:80

# Stop all services
docker-compose down
```

---

## 🧪 Run Tests

```bash
# Activate virtual environment
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

# Run all tests
pytest tests/ -v
```

### Test Results

```
tests/test_app.py::test_home_page          PASSED ✅
tests/test_app.py::test_health_check       PASSED ✅
tests/test_app.py::test_get_doctors        PASSED ✅
tests/test_app.py::test_get_departments    PASSED ✅
tests/test_app.py::test_contact_form       PASSED ✅
tests/test_app.py::test_404_not_found      PASSED ✅

6 passed in 0.09s
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page (HTML) |
| GET | `/health` | Health check → `{"status": "healthy"}` |
| GET | `/doctors` | List all doctors (JSON) |
| GET | `/departments` | List all departments (JSON) |
| POST | `/contact` | Submit appointment form |
| GET | `/about` | About page |

---

## 🔧 Jenkins CI/CD Pipeline Setup

### Prerequisites

- Jenkins installed and running on AWS EC2
- Docker installed on Jenkins server
- GitHub repository connected
- Docker Hub account

### Step 1 — Install Jenkins Plugins

- Git Plugin
- Pipeline Plugin
- Docker Pipeline
- GitHub Integration Plugin

### Step 2 — Add Credentials in Jenkins

Go to: **Manage Jenkins → Credentials → Global → Add Credentials**

| Credential | Kind | ID |
|-----------|------|----|
| GitHub token | Username with password | `123` |
| Docker Hub | Username with password | `dockerhub-creds` |

### Step 3 — Configure GitHub Webhook

In your GitHub repo → **Settings → Webhooks → Add webhook**

```
Payload URL : http://43.205.211.204:8080/github-webhook/
Content type: application/json
Event       : Just the push event
```

### Step 4 — Enable Jenkins Trigger

In Jenkins job → **Configure → Triggers**

☑️ **GitHub hook trigger for GITScm polling**

### Step 5 — Run the Pipeline!

---

## 🔄 Jenkins Pipeline Stages

```
📥 Git Checkout
      ↓
📦 Install Dependencies
      ↓
🧪 Run Tests (6 pytest tests)
      ↓
🐳 Build Docker Image
      ↓
🔐 Push to Docker Hub
      ↓
🚀 Deploy Container on EC2
      ↓
❤️  Health Check (/health endpoint)
```

### Complete Jenkinsfile

```groovy
pipeline {
    agent any

    stages {

        stage('Git Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: '123',
                    url: 'https://github.com/kalimuthu-git/Medicure-Healthcare-Domain--Project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    echo "✅ Dependencies installed"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ -v
                    echo "✅ All tests passed"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t medicure-health-care:v1 .
                    echo "✅ Docker image built"
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker tag medicure-health-care:v1 $DOCKER_USER/medicure-healthcare-project:v1
                        docker push $DOCKER_USER/medicure-healthcare-project:v1
                        echo "✅ Pushed to Docker Hub"
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker stop medicure-container || true
                    docker rm   medicure-container || true
                    docker pull kalimuthudevops/medicure-healthcare-project:v1
                    docker run -d \
                        -p 9090:5000 \
                        --name medicure-container \
                        kalimuthudevops/medicure-healthcare-project:v1
                    echo "✅ App deployed on port 9090"
                '''
            }
        }
    }

    post {
        success {
            echo "✅ PIPELINE SUCCESS — http://43.205.211.204:9090"
        }
        failure {
            echo "❌ PIPELINE FAILED — Check logs"
        }
    }
}
```

---

## ☁️ AWS EC2 Setup

| Setting | Value |
|---------|-------|
| Instance Name | Project-Medicure |
| Instance Type | c7i-flex.large |
| Region | ap-south-1 (Mumbai) |
| OS | Ubuntu |
| Security Group | Port 8080 (Jenkins), 9090 (App) |

### Security Group Inbound Rules

| Port | Protocol | Source | Purpose |
|------|----------|--------|---------|
| 22 | SSH | Your IP | Server access |
| 8080 | TCP | 0.0.0.0/0 | Jenkins UI |
| 9090 | TCP | 0.0.0.0/0 | Medicure App |
| 5000 | TCP | 0.0.0.0/0 | Flask (internal) |

---

## 🐳 Docker Hub

```
Repository : kalimuthudevops/medicure-healthcare-project
Tag        : v1
Size       : 56.8 MB
OS         : Linux
```

Pull and run from Docker Hub:

```bash
docker pull kalimuthudevops/medicure-healthcare-project:v1
docker run -d -p 9090:5000 --name medicure-container kalimuthudevops/medicure-healthcare-project:v1
```

---

## 👨‍💻 Complete DevOps Flow

```
Developer writes code
      ↓
git push → GitHub repo
      ↓
GitHub Webhook triggers Jenkins
      ↓
Jenkins Pipeline starts automatically
      ↓
Install deps → Run tests → Build Docker image
      ↓
Push image to Docker Hub
      ↓
Pull image on EC2 → Run container
      ↓
Medicure app live at http://43.205.211.204:9090 🌐
```

---

## 📸 Project Screenshots

| Stage | Description |
|-------|-------------|
| Git Checkout | Code pulled from GitHub successfully |
| Install & Test | 6/6 pytest tests passed |
| Docker Build | 17-step multi-stage build completed |
| Docker Hub Push | Image pushed — 56.8MB |
| Deploy | Container running healthy on EC2 |
| Live Website | Medicure running at port 9090 |
| Jenkins Trigger | GitHub webhook auto-trigger enabled |
| AWS EC2 | Instance running — 3/3 checks passed |

---

## 👤 Author

**Kalimuthu** — DevOps Engineer
- GitHub: [@kalimuthu-git](https://github.com/kalimuthu-git)
- Docker Hub: [kalimuthudevops](https://hub.docker.com/u/kalimuthudevops)

---

**Medicure Healthcare © 2026 — Built with ❤️ using DevOps**
