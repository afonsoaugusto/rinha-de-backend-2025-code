from fastapi import FastAPI
from fastapi.responses import Response
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api")

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    logger.info("API started.")


@app.get("/health")
def health():
    logger.info("/health endpoint called.")
    return Response(status_code=200)
