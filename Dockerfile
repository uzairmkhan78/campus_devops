FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app1.py app2.py app3.py app4.py ./

EXPOSE 5001 5002 5003 5004

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app1:app"]

