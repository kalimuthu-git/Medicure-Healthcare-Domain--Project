# ── Stage 1: Build ──────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ── Stage 2: Production ──────────────────────────────────────
FROM python:3.11-slim

LABEL maintainer="Medicure DevOps Team"
LABEL version="1.0.0"
LABEL description="Medicure Healthcare Web Application"

# Create non-root user for security
RUN groupadd -r medicure && useradd -r -g medicure medicure

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY --chown=medicure:medicure . .

# Switch to non-root user
USER medicure

# Expose application port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

# Run with Gunicorn in production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "--timeout", "120", "app:app"]
