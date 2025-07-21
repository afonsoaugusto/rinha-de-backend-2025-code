# rinha-de-backend-2025-code

rinha-de-backend-2025-code

## setup

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.12
uv python list

uv venv venv --python 3.12
source venv/bin/activate

cd src
uvicorn main:app --host 0.0.0.0 --port 9999

docker build -t fastapi-app src/
docker run -it --rm -p 9999:9999 fastapi-app
```

```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
set Path=C:\Users\Dell\.local\bin;%Path%   (cmd)
$env:Path = "C:\Users\Dell\.local\bin;$env:Path"   (powershell)
```

## rinha

```sh
cd rinha-de-backend-2025/payment-processor/
docker-compose up --build
docker-compose -f docker-compose.yml down
docker system prune -f
sudo chmod 644 init.sql
```

## Test endpoints with curl

### Health check

```sh
curl -i http://localhost:9999/health
```

### Payments POST

```sh
curl.exe -i -X POST http://localhost:9999/payments -H "Content-Type: application/json" -d '{\"correlationId\": \"b7156fc2-e594-4121-a984-4c37345c7941\", \"amount\": 12.45}'

curl.exe -i -X POST http://localhost:8002/payments -H "Content-Type: application/json" -d '{\"correlationId\": \"b7156fc2-e594-4121-a984-4c37345c7941\", \"amount\": 12.45, \"requestedAt\": \"2025-07-21T12:34:56.000Z\"}'

curl.exe -i -H "X-Rinha-Token: 123" "http://localhost:8002/admin/payments-summary?from=2025-07-20T12:34:56.000Z&to=2025-07-22T12:35:56.000Z"

curl.exe -i http://localhost:8001/payments/service-health
curl.exe -i http://localhost:8002/payments/service-health
```

# Payments summary

```sh
curl -i "http://localhost:9999/payments-summary?from=2020-07-10T12:34:56.000Z&to=2020-07-10T12:35:56.000Z"
```
