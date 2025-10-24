import socket
import threading
from src.utils.message_utils import validate_message
from src.utils.logger import get_logger

HOST = '127.0.0.1'
PORT = 5000
clients = []
logger = get_logger("Server")

def start_server(HOST, PORT):
    """Inicia el servidor y espera conexiones."""
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        logger.info(f"Servidor iniciado en {HOST}:{PORT}")
        # hilo aceptador
        t = threading.Thread(target=accept_clients, args=(server_socket,), daemon=True)
        t.start()
        return True
    except Exception as e:
        logger.error(f"Error al iniciar el servidor: {e}")
        return False
    
def accept_clients(server_socket):
    """Acepta conexiones de clientes."""
    while True:
        try:
            client_socket, addr = server_socket.accept()
            clients.append(client_socket)
            logger.info(f"Cliente conectado desde {addr}")
            th = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
            th.start()
        except Exception as e:
            logger.error(f"Error aceptando clientes: {e}")
            break

def handle_client(client_socket, addr):
    """Maneja la comunicación con un cliente."""
    try:
        while True:
            data = client_socket.recv(4096)
            if not data:
                logger.info(f"Cliente {addr} desconectado")
                break
            try:
                message = data.decode('utf-8')
            except Exception as e:
                logger.error("Error decodificando mensaje")
                continue
            try:
                if validate_message(message):
                    client_socket.sendall(b"Mensaje recibido.")
            except ValueError as e:
                logger.error("Error en validar mensaje")
                try:
                    client_socket.sendall("ERROR: mensaje inválido")
                except Exception:
                        logger.error("Error en el mensaje")
                continue

            broadcast_message(message, client_socket)
    except Exception as e:
        logger.error(f"Error manejando cliente {addr}: {e}")
    finally:
        # limpiar lista de clientes
        if client_socket in clients:
            try:
                clients.remove(client_socket)
            except ValueError:
                logger.error("Error en remover al cliente")
        try:
            client_socket.close()
        except Exception:
            logger.error("Error en cerrar el socket")
        logger.info(f"Conexión con {addr} cerrada")


def broadcast_message(message, sender_socket):
    """Difunde un mensaje a todos los clientes excepto al remitente."""
    if isinstance(message, str):
        payload = message.encode('utf-8')
    else:
        payload = message
    for client in clients.copy():
        if client != sender_socket:
            try:
                 client.sendall(payload)
            except Exception as e:
                logger.error(f"Error al enviar mensaje a un cliente: {e}") 
                # si falla, quitar cliente
                try:
                    clients.remove(client)
                    client.close()
                except Exception:
                    logger.error(f"Error al remover al cliente") 

if __name__ == "__main__":
    start_server(HOST,PORT)
    threading.Event().wait()