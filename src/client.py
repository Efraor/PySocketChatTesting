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
    """Envía un mensaje al servidor."""
    try:
        validate_message(message)
        client_socket.sendall(message.encode('utf-8'))
        logger.info(f"Mensaje enviado: {message}")
        response = client_socket.recv(1024).decode('utf-8')
        logger.info(f"Respuesta del servidor: {response}")
        return response
    except ValueError:
        logger.error("Intento de enviar un mensaje vacío.")
        return False
    except Exception as e:
        logger.error(f"Error al enviar el mensaje: {e}")
        return False

