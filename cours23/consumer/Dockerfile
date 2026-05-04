# =========================
# STAGE 1 : BUILDER
# =========================
FROM python:3.10-slim AS builder
WORKDIR /app
COPY requirements.txt .
# Installation des dépendances dans un dossier custom
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
# =========================
# STAGE 2 : RUNTIME
# =========================
FROM python:3.10-slim
WORKDIR /app
# Créer utilisateur non-root
RUN mkdir -p /home/appuser
# Copier uniquement les dépendances depuis builder
COPY --from=builder /install /usr/local
# Copier l'application
COPY consumer_ml.py .
# Sécurité : permissions
RUN chown -R 1000:1000 /app /home/appuser
# Utilisateur non-root
USER 1000
ENTRYPOINT ["python", "consumer_ml.py"]



