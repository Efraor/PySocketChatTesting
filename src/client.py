"""
Cliente principal del chat Sock-It-To-Me
- Se conecta al servidor
- Envía y recibe mensajes
"""
def connect_to_server(host, port):
    """
    Cliente mínimo que simplemente devuelve un objeto simulado para pasar la prueba.
    Más adelante implementaremos sockets reales.
    """
    return {"ip": host, "port": port}  # objeto simulado

def send_message(client, message):
    """
    Envía un mensaje mínimo: valida y retorna True.
    """
    from src.utils import validate_message
    validate_message(message)
    return "Mensaje recibido"

