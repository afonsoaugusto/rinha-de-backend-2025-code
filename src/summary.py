from pydantic import BaseModel
from typing import Optional
import logging

logger = logging.getLogger("api")


class PaymentsSummaryResponse(BaseModel):
    default: dict
    fallback: dict


def payments_summary(
    from_: Optional[str],
    to: Optional[str]
):
    logger.info(f"/payments-summary endpoint called. from={from_}, to={to}")
    # Aqui você pode adicionar lógica para buscar os dados reais
    response = {
        "default": {
            "totalRequests": 43236,
            "totalAmount": 415542345.98
        },
        "fallback": {
            "totalRequests": 423545,
            "totalAmount": 329347.34
        }
    }
    return response
