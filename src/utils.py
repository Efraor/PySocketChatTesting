
# @Funciones de utilidad para el chat

def validate_message(message):
    """"
    verifica si el mensaje es válido (no vacío y no solo espacios)
    Demasiado largo: 256 caracteres
    """
    if not message:
        return False
    
    if message.strip():
        return False

    if len(message) > 256:
        return False
    return True



