# 🏥 Medicure Healthcare — DevOps Real-Time Project

![Project Status](https://img.shields.io/badge/Status-Live-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Jenkins](https://img.shields.io/badge/CI%2FCD-Jenkins-red)
![Kubernetes](https://img.shields.io/badge/Kubernetes-v1.30.14-326CE5)
![Python](https://img.shields.io/badge/Python-3.11-yellow)
![AWS](https://img.shields.io/badge/Cloud-AWS%20EC2-orange)
![GitHub Webhook](https://img.shields.io/badge/Webhook-Enabled-success)

> A full-stack healthcare web application with a complete DevOps pipeline using
> **Flask + Docker + Jenkins + Kubernetes + AWS EC2 + GitHub Webhook**

---

## 🌐 Live Project URLs

| Service | URL |
|---------|-----|
| 🌍 Website | `http://43.205.211.204:9090` |
| 🔧 Jenkins | `http://13.232.71.59:8080` |
| 🐳 Docker Hub | `kalimuthudevops/medicure-healthcare-project:12` |
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
├── deployment.yaml           # K8s Deployment — 2 pods
├── service.yaml              # K8s Service — NodePort
├── templates/
│   └── index.html            # Medicure frontend UI
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
| Container Orchestration | Kubernetes v1.30.14 |
| CI/CD | Jenkins |
| Image Registry | Docker Hub |
| Cloud | AWS EC2 (c7i-flex.large) |
| Version Control | Git + GitHub |
| Auto Trigger | GitHub Webhook |
| Testing | Pytest + pytest-flask |

---

## 🚀 Run Locally (Without Docker)

```bash
# 1. Clone the repo
git clone https://github.com/kalimuthu-git/Medicure-Healthcare-Domain--Project.git
cd Medicure-Healthcare-Domain--Project

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py

# 5. Open browser → http://localhost:5000
```

---

## 🐳 Run With Docker

```bash
# Build image
docker build -t medicure-healthcare-project:v1 .

# Run container
docker run -d \
  --name medicure-container \
  -p 9090:5000 \
  medicure-healthcare-project:v1

# Open browser → http://localhost:9090

# Check container
docker ps

# View logs
docker logs medicure-container
```

---

## ☸️ Deploy With Kubernetes

```bash
# Apply Deployment (creates 2 pods)
kubectl apply -f deployment.yaml

# Apply Service (exposes app)
kubectl apply -f service.yaml

# Check pods status
kubectl get pods

# Check services
kubectl get svc

# Check deployments
kubectl get deployments

# View pod logs
kubectl logs -l app=medicure

# Scale pods
kubectl scale deployment medicure-app --replicas=3

# Update image
kubectl set image deployment/medicure-app \
  medicure-container=kalimuthudevops/medicure-healthcare-project:13
```

### Kubernetes Pods — Running ✅

```
NAME                                READY   STATUS    RESTARTS   AGE
medicure-app-57b4b46bd7-np5zs      1/1     Running   0          29s
medicure-app-57b4b46bd7-pwz82      1/1     Running   0          31s
```

---

## 📄 Kubernetes Files

### deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: medicure-app
  labels:
    app: medicure
spec:
  replicas: 2
  selector:
    matchLabels:
      app: medicure
  template:
    metadata:
      labels:
        app: medicure
    spec:
      containers:
        - name: medicure-container
          image: kalimuthudevops/medicure-healthcare-project:12
          ports:
            - containerPort: 5000
          resources:
            requests:
              memory: "128Mi"
              cpu: "250m"
            limits:
              memory: "256Mi"
              cpu: "500m"
```

### service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: medicure-service
spec:
  type: NodePort
  selector:
    app: medicure
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
      nodePort: 30080
```

---

## 🧪 Run Tests

```bash
source venv/bin/activate
pytest tests/ -v
```

### Test Results ✅

```
tests/test_app.py::test_home_page          PASSED ✅  [ 16%]
tests/test_app.py::test_health_check       PASSED ✅  [ 33%]
tests/test_app.py::test_get_doctors        PASSED ✅  [ 50%]
tests/test_app.py::test_get_departments    PASSED ✅  [ 66%]
tests/test_app.py::test_contact_form       PASSED ✅  [ 83%]
tests/test_app.py::test_404_not_found      PASSED ✅  [100%]

============================== 6 passed in 0.10s ==============================
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

---

## 🔗 GitHub Webhook Setup

Webhook automatically triggers Jenkins pipeline on every `git push`.

### Steps to Configure

1. Go to GitHub repo → **Settings → Webhooks → Add webhook**
2. Fill in:

```
Payload URL  : http://13.232.71.59:8080/github-webhook/
Content type : application/json
Event        : Just the push event ✅
Active       : ✅ Enabled
```

3. Click **Add webhook**

✅ **Status:** `"Okay, that hook was successfully created!"`

### How it Works

```
git push → GitHub detects push
        → sends POST to Jenkins webhook URL
        → Jenkins pipeline triggers automatically
        → All stages run without manual intervention
```

---

## 🔄 Jenkins CI/CD Pipeline

### Complete Jenkinsfile

```groovy
pipeline {
    agent any

    environment {
        IMAGE_NAME = "medicure-healthcare-project"
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {

        stage('Git Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: '12',
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
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: '123',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker tag $IMAGE_NAME:$IMAGE_TAG $DOCKER_USER/$IMAGE_NAME:$IMAGE_TAG
                        docker push $DOCKER_USER/$IMAGE_NAME:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl apply -f deployment.yaml
                    kubectl apply -f service.yaml
                '''
            }
        }
    }

    post {
        success {
            echo "✅ PIPELINE SUCCESS — Medicure is live on Kubernetes!"
        }
        failure {
            echo "❌ PIPELINE FAILED — Check logs above"
        }
    }
}
```

---

## ✅ Pipeline Stages — All Completed

```
📥 Git Checkout              ✅  Code pulled from GitHub
📦 Install Dependencies      ✅  Flask, Gunicorn, Pytest installed
🧪 Run Tests                 ✅  6/6 tests passed in 0.10s
🐳 Build Docker Image        ✅  medicure-healthcare-project:12 (17 steps)
🔐 Push to Docker Hub        ✅  kalimuthudevops/medicure-healthcare-project:12
☸️  Deploy to Kubernetes      ✅  deployment.apps/medicure-app created
                                  service/medicure-service created
                                  2 pods Running ✅
```

---

## ☁️ AWS EC2 Setup

| Setting | Value |
|---------|-------|
| Instance Name | Project-Medicure |
| Instance Type | c7i-flex.large |
| Region | ap-south-1 (Mumbai) |
| OS | Ubuntu |

### Security Group Inbound Rules

| Port | Protocol | Purpose |
|------|----------|---------|
| 22 | SSH | Server access |
| 8080 | TCP | Jenkins UI |
| 9090 | TCP | Medicure App |
| 30080 | TCP | Kubernetes NodePort |

---

## 🐳 Docker Hub

```
Repository : kalimuthudevops/medicure-healthcare-project
Tag        : 12
Size       : 56.8 MB
OS         : Linux
Pushed     : ✅ Successfully
```

Pull and run directly:

```bash
docker pull kalimuthudevops/medicure-healthcare-project:12
docker run -d -p 9090:5000 \
  --name medicure-container \
  kalimuthudevops/medicure-healthcare-project:12
```

---

## 🔧 kubectl Installation (on EC2)

```bash
# Install kubectl
sudo apt update
sudo apt install -y kubectl

# Verify
kubectl version --client
# Client Version: v1.30.14
# Kustomize Version: v5.0.4
```

---

## 👨‍💻 Complete DevOps Flow

```
Developer writes code on local machine
          ↓
git push → GitHub repository
          ↓
GitHub Webhook (push event)
          ↓  POST → http://13.232.71.59:8080/github-webhook/
Jenkins Pipeline triggers automatically
          ↓
  ┌───────────────────────────┐
  │  Install Dependencies     │
  │  Run Pytest (6/6 ✅)      │
  │  Build Docker Image       │
  │  Push to Docker Hub       │
  │  kubectl apply            │
  └───────────────────────────┘
          ↓
Kubernetes Cluster (AWS EC2)
  ┌──────────────────────────────────────┐
  │  Pod 1: medicure-app-...-np5zs  ✅  │
  │  Pod 2: medicure-app-...-pwz82  ✅  │
  └──────────────────────────────────────┘
          ↓
  Medicure Website LIVE 🌐
  http://43.205.211.204:9090
```

---

## 📸 Project Achievements

| Component | Status |
|-----------|--------|
| GitHub Repo | ✅ Created & pushed |
| GitHub Webhook | ✅ Successfully created |
| Jenkins Pipeline | ✅ All 6 stages passed |
| Docker Image Built | ✅ 17-step multi-stage build |
| Docker Hub Push | ✅ Image live (56.8MB) |
| kubectl installed | ✅ v1.30.14 |
| K8s Deployment | ✅ medicure-app created |
| K8s Service | ✅ medicure-service created |
| K8s Pods | ✅ 2/2 Running |
| Website Live | ✅ Accessible on port 9090 |

---

## 👤 Author

**Kalimuthu** — DevOps Engineer
- GitHub: [@kalimuthu-git](https://github.com/kalimuthu-git)
- Docker Hub: [kalimuthudevops](https://hub.docker.com/u/kalimuthudevops)

---

**Medicure Healthcare © 2026**
**Built with ❤️ using Flask + Docker + Jenkins + Kubernetes + AWS EC2 + GitHub Webhook**
