FROM python:3.12-slim
RUN pip install fastapi uvicorn

WORKDIR /app
COPY . /app

ENV PYTHONUNBUFFERED=1

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug"]
