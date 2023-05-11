FROM python:3.9

WORKDIR /app

ARG APP_SERVICE_DATA_PORT

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE ${APP_SERVICE_DATA_PORT}

CMD ["python", "app.py"]
