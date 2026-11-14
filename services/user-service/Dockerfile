FROM python:3.14-slim

WORKDIR /app

RUN pip install --no-cache-dir Flask==3.1.3

COPY app.py .

EXPOSE 5001

CMD ["python", "app.py"]
