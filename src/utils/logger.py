import logging
import sys

def get_logger(name: str) -> logging.Logger:
    """
    Configura y devuelve un logger con formato uniforme.
    Evita duplicar handlers si el logger ya fue creado.
    """
    logger = logging.getLogger(name)
    # Evitar que se agreguen múltiples handlers si se llama varias veces
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(name)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    
    return logger