FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY producer_car.py .
RUN useradd -m appuser && chown -R appuser /app
USER appuser
CMD ["python", "producer_car.py"]




