import socket
import threading
from src.utils.message_utils import validate_message
from src.utils.logger import get_logger

HOST = '127.0.0.1'
PORT = 5000
clients = []
logger = get_logger("Server")

def start_server():
    """Inicia el servidor y espera conexiones."""
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        logger.info(f"Servidor iniciado en {HOST}:{PORT}")
        threading.Thread(target=accept_clients, args=(server_socket,), daemon=True).start()
        return True
    except Exception as e:
        logger.error(f"Error al iniciar el servidor: {e}")
        return False
    
def accept_clients(server_socket):
    """Acepta conexiones de clientes."""
    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        logger.info(f"Cliente conectado desde {addr}")
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()  

def handle_client(client_socket):
    """Maneja la comunicación con un cliente."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break # Cliente cerró la conexión
            if validate_message(message):
                logger.info(f"Mensaje recibido de un cliente: {message}")
                broadcast_message(message, client_socket)
        except Exception as e:
            logger.warning(f"Error en la comunicación con el cliente: {e}")
            break
    if client_socket in clients:
        clients.remove(client_socket)
    client_socket.close()


def broadcast_message(message, sender_socket):
    """Difunde un mensaje a todos los clientes excepto al remitente."""
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message.encode('utf-8'))
            except Exception as e:
                logger.error(f"Error al enviar mensaje a un cliente: {e}") 

if __name__ == "__main__":
    start_server()
    # Mantener el servidor en ejecución
    threading.Event().wait()