# 🏥 Medicure Healthcare — DevOps Real-Time Project

A full-stack healthcare web application with a complete DevOps pipeline using **Flask + Docker + Jenkins**.

---

## 📁 Project Structure

```
medicure/
├── app.py                  # Flask application (backend)
├── requirements.txt        # Python dependencies
├── Dockerfile              # Multi-stage Docker build
├── docker-compose.yml      # Docker Compose (App + Nginx)
├── Jenkinsfile             # CI/CD Pipeline
├── templates/
│   └── index.html          # Medicure frontend (HTML/CSS/JS)
├── nginx/
│   └── nginx.conf          # Nginx reverse proxy config
├── tests/
│   └── test_app.py         # Pytest unit tests
└── README.md
```

---

## 🚀 Run Locally (Without Docker)

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/medicure.git
cd medicure

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

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
# Build image
docker build -t medicure-healthcare .

# Run container
docker run -d -p 5000:5000 --name medicure-app medicure-healthcare

# Open browser
# http://localhost:5000
```

---

## 🐳 Run With Docker Compose (App + Nginx)

```bash
docker-compose up -d

# App runs on: http://localhost:5000
# Nginx proxy:  http://localhost:80
```

---

## 🧪 Run Tests

```bash
source venv/bin/activate
pytest tests/ -v
```

---

## 🔧 Jenkins CI/CD Pipeline Setup

### Prerequisites
- Jenkins installed and running
- Docker installed on Jenkins agent
- GitHub repo connected

### Steps

1. **Install Jenkins Plugins:**
   - Git Plugin
   - Docker Pipeline
   - Pipeline Plugin

2. **Add Credentials in Jenkins:**
   - `dockerhub-username` → Your Docker Hub username
   - `dockerhub-password` → Your Docker Hub password

3. **Create Jenkins Pipeline Job:**
   - New Item → Pipeline
   - Pipeline script from SCM → Git
   - Repository URL: your GitHub repo
   - Script Path: `Jenkinsfile`

4. **Run the Pipeline!**

### Pipeline Stages
```
📥 Checkout → 🔍 Code Quality → 📦 Install → 🧪 Tests → 
🐳 Build Image → 🔐 Push to Hub → 🚀 Deploy → ❤️ Health Check → 🧹 Cleanup
```

---

## 🌐 API Endpoints

| Method | Endpoint        | Description              |
|--------|-----------------|--------------------------|
| GET    | `/`             | Home page (HTML)         |
| GET    | `/health`       | Health check (JSON)      |
| GET    | `/doctors`      | List all doctors (JSON)  |
| GET    | `/departments`  | List departments (JSON)  |
| POST   | `/contact`      | Submit appointment form  |

---

## 🛠️ Tech Stack

| Layer      | Technology         |
|------------|--------------------|
| Frontend   | HTML5, CSS3, JS    |
| Backend    | Python Flask       |
| Server     | Gunicorn + Nginx   |
| Container  | Docker             |
| CI/CD      | Jenkins            |
| Registry   | Docker Hub         |

---

## 👨‍💻 DevOps Flow

```
Developer → GitHub Push → Jenkins Trigger →
Build & Test → Docker Build → Push to Hub → Deploy → Health Check
```

---

**Medicure Healthcare © 2024**
