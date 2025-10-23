"""
    Crea un logger configurado con formato estándar.
    
    Args:
        name (str): Nombre del logger (normalmente __name__ del módulo)
    
    Returns:
        logging.Logger: Logger configurado
"""

import logging
import sys


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Evitar que se agreguen múltiples handlers si se llama varias veces
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        #Handler a consola
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    return logger