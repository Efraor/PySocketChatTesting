import logging

logging.basicConfig(level=logging.INFO)

def validate_message(message):
    """
    Valida que el mensaje no esté vacío y sea una cadena.
    """
    if not message or not message.strip():
        logging.error("Mensaje vacío o inválido detectado")
        raise ValueError("El mensaje no puede estar vacío y debe ser una cadena.")
    logging.info("Mensaje validado: "+ message)
    return True