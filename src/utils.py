"""
Funciones auxiliares para servidor y cliente
- encode/decode de mensajes
- validaciones
- logging
"""

def validate_message(message):
    """
    Valida que el mensaje no esté vacío y sea una cadena.
    """
    if not message.strip():
        raise ValueError("El mensaje no puede estar vacío.")
    return True

