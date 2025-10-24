import threading
import time
from src import server
from src.client import connect_to_server, send_message

HOST, PORT = '127.0.0.1', 5000


def client_thread_func(host, port, send_messages, received_list, idx, ready_event=None):
    """Cliente que envía y recibe mensajes."""
    s = connect_to_server(host, port)
    if ready_event:
        ready_event.set()  # indicar que el cliente receptor está listo

    for m in send_messages:
        send_message(s, m)
        # esperar respuesta del servidor
        try:
            data = s.recv(4096)
            if data:
                received_list.append((idx, data.decode('utf-8')))
        except Exception:
            pass

    # Mantener abierto para recibir broadcast
    end_time = time.time() + 0.5
    while time.time() < end_time:
        try:
            data = s.recv(4096)
            if data:
                received_list.append((idx, data.decode('utf-8')))
        except Exception:
            break

    s.close()


def test_multiple_clients_broadcast_and_disconnect():
    """Test de múltiples clientes, broadcast y desconexión abrupta."""

    # 1️⃣ Iniciar servidor en hilo
    server_thread = threading.Thread(target=server.start_server, args=(HOST, PORT), daemon=True)
    server_thread.start()
    time.sleep(0.2)  # tiempo a hilo aceptador

    received = []
    ready_event = threading.Event()

    # 2️⃣ Cliente receptor
    t1 = threading.Thread(
        target=client_thread_func,
        args=(HOST, PORT, [], received, 1, ready_event),
        daemon=True
    )
    t1.start()
    ready_event.wait()  # esperar que se conecte

    # 3️⃣ Cliente emisor
    t0 = threading.Thread(
        target=client_thread_func,
        args=(HOST, PORT, ["m1", "m2"], received, 0),
        daemon=True
    )
    t0.start()

    # Esperar a que terminen
    t0.join(timeout=2)
    t1.join(timeout=2)

    # 4️⃣ Verificar que los mensajes fueron recibidos
    assert any("m1" in msg or "m2" in msg for _, msg in received), "Ningún mensaje de broadcast recibido"
    print("Mensajes recibidos:", received)

    # 5️⃣ Desconexión abrupta
    s2 = connect_to_server(HOST, PORT)
    s2.close()
    time.sleep(0.1)

    # 6️⃣ Otro cliente tras desconexión
    s3 = connect_to_server(HOST, PORT)
    assert s3 is not None
    send_message(s3, "post-disconnect")
    s3.close()
