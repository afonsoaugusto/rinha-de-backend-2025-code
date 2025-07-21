import logging

logger = logging.getLogger("api")


def create_payment(correlationId, amount):
    logger.info(
        f"/payments POST called. correlationId={correlationId}, amount={amount}")
    # Aqui você pode adicionar lógica para processar o pagamento
    return {"correlationId": str(correlationId), "amount": float(amount)}
