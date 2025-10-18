"""
Servidor principal del chat Sock-It-To-Me
- Acepta conexiones de clientes
- Recibe y difunde mensajes
"""

# def start_server():
#     """
#     Servidor mínimo que simplemente devuelve True para pasar la prueba.
#     Más adelante implementaremos sockets reales.
#     """
#     # Lógica para iniciar el servidor
#     return True

import socket
import threading
import logging
from src.utils.message_utils import validate_message

logging.basicConfig(level=logging.INFO)

HOST = '127.0.0.1'
PORT = 5000

clients = []

def start_server():
    """Inicia el servidor y espera conexiones."""

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        logging.info(f"Servidor iniciado en {HOST}:{PORT}")
        threading.Thread(target=accept_clients, args=(server_socket,), daemon=True).start()
        return True
    except Exception as e:
        logging.error(f"Error al iniciar el servidor: {e}")
        return False
    
def accept_clients(server_socket):
    """Acepta conexiones de clientes."""
    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        logging.info(f"Cliente conectado desde {addr}")
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()  

def handle_client(client_socket):
    """Maneja la comunicación con un cliente."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not validate_message(message):
                continue
            broadcast_message(message, client_socket)
        except Exception as e:
            logging.warning(f"Error en la comunicación con el cliente: {e}")
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast_message(message, sender_socket):
    """Difunde un mensaje a todos los clientes excepto al remitente."""
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message.encode('utf-8'))
            except Exception as e:
                logging.error(f"Error al enviar mensaje a un cliente: {e}") 

