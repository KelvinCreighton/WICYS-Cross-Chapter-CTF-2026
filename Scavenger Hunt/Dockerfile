FROM python:3.11-slim

WORKDIR /app
COPY app.py ./
COPY style.css ./
COPY script.js ./
COPY templates ./templates

RUN pip install flask

EXPOSE 5000
CMD ["python", "app.py"]