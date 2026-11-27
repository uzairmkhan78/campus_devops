FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app1.py app2.py app3.py app4.py start.py ./

EXPOSE 5000 5001 5003 5004

CMD ["python", "start.py"]
