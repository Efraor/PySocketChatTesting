"""
Pruebas unitarias para el cliente
- Conexión al servidor
- Envío de mensajes
- Validación de mensajes
"""

import pytest
from src.client import connect_to_server, send_message  # Todavía no implementado

def test_client_connects():
    """
    Verifica que el cliente puede conectarse al servidor.
    """
    client = connect_to_server('localhost', 5000)
    assert client is not None

def test_client_sends_message():
    """
    Verifica que el cliente puede enviar un mensaje al servidor.
    """
    client = connect_to_server('localhost', 5000)
    response = send_message(client, "Hola, mundo!")
    assert response == "Mensaje recibido"