import socket
from src.utils.message_utils import validate_message
from src.utils.logger import get_logger

logger = get_logger("Client")

def connect_to_server(host, port):
    """Conecta al servidor en la dirección y puerto especificados."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        logger.info(f"Conectado al servidor en {host}:{port}")
        return client_socket
    except Exception as e:
        logger.error(f"Error al conectar al servidor: {e}")
        return None

def send_message(client_socket, message: str)-> bool:
    """Valida y envía el mensaje; retorna la respuesta decodificada o False en error."""
    if client_socket is None:
        logger.error("Socket inexistente")
        return False
    try:
        validate_message(message)
    except ValueError:
        logger.error("Intento de enviar un mensaje vacío.")
        return False
    try:
        client_socket.sendall(message.encode('utf-8'))
        resp = client_socket.recv(4096)
        if resp is None:
            return None
        return resp.decode('utf-8')
    except Exception as e:
        logger.error(f"Error al enviar/recibir mensaje: {e}")
        return False

