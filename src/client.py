"""
Cliente principal del chat Sock-It-To-Me
- Se conecta al servidor
- Envía y recibe mensajes
"""

# def connect_to_server(host, port):
#     """
#     Cliente mínimo que simplemente devuelve un objeto simulado para pasar la prueba.
#     Más adelante implementaremos sockets reales.
#     """
#     return {"ip": host, "port": port}  # objeto simulado

# def send_message(client, message):
#     """
#     Envía un mensaje mínimo: valida y retorna True.
#     """
#     from utils.utils import validate_message
#     validate_message(message)
#     return "Mensaje recibido"

import socket
import logging
from src.utils.message_utils import validate_message

logging.basicConfig(level=logging.INFO)

def connect_to_server(host, port):
    """Conecta al servidor en la dirección y puerto especificados."""

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        logging.info(f"Conectado al servidor en {host}:{port}")
        return client_socket
    except Exception as e:
        logging.error(f"Error al conectar al servidor: {e}")
        return None
    
def send_message(client_socket, message: str)-> bool:
    """Envía un mensaje al servidor."""

    try:
        validate_message(message)
        client_socket.sendall(message.encode('utf-8'))
        logging.info(f"Mensaje enviado: {message}")
        return "Mensaje recibido" 

    except ValueError:
        logging.error("Intento de enviar un mensaje vacío.")
        return False
    except Exception as e:
        logging.error(f"Error al enviar el mensaje: {e}")
        return False

