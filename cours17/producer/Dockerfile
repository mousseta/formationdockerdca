FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd -m appuser && chown -R appuser /app
USER appuser
ENTRYPOINT ["python", "producer_car.py"]

