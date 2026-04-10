#Instalación de cosas 
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user-- -r requirements.txt

#Creación de la imagen final
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV path=/root/.local/bin:$PATH
COPY app.py .
CMD ["python", "app.py"]
