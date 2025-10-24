from src.utils.logger import get_logger
logger = get_logger("Utils")

def validate_message(message):
    """
    Valida que el mensaje no esté vacío y sea una cadena.
    """
    if not message or not message.strip():
        logger.error("Mensaje vacío o inválido detectado")
        raise ValueError("El mensaje no puede estar vacío y debe ser una cadena.")
    logger.info("Mensaje validado: "+ message)
    return True