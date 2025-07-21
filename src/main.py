

import logging
from typing import Optional
from fastapi import FastAPI, Response, Body, Query
from pydantic import UUID4, condecimal
from post import create_payment
from summary import payments_summary

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


@app.post("/payments")
def post_payments(
    correlationId: UUID4 = Body(..., embed=True),
    amount: condecimal(gt=0) = Body(..., embed=True)
):
    return create_payment(correlationId, amount)


@app.get("/payments-summary")
def get_payments_summary(
    from_: Optional[str] = Query(None, alias="from"),
    to: Optional[str] = Query(None)
):
    return payments_summary(from_, to)
