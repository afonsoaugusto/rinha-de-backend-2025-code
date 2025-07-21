FROM python:3.12-slim
RUN pip install fastapi uvicorn

WORKDIR /app
COPY . /app

ENV PYTHONUNBUFFERED=1

EXPOSE 9999
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9999", "--log-level", "debug"]
