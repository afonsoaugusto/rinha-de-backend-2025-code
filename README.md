# rinha-de-backend-2025-code

rinha-de-backend-2025-code

## setup

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.12
uv python list

uv venv venv --python 3.12
source venv/bin/activate

uvicorn src.main:app --host 0.0.0.0 --port 8000

dockebuild -t fastapi-app src/
docker run -it --rm -p 8000:8000 fastapi-app
``` 