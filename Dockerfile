
FROM python:3.9-slim

WORKDIR /app


COPY requirements.txt .
RUN pip install -r requirements.txt

# kalan tum dosyalari iceri kopyaliyorum
COPY . .


EXPOSE 5000

# Uygulamayi baslat
CMD ["python", "app.py"]