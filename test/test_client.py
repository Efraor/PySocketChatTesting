import pytest
from unittest.mock import patch, MagicMock
from src.client import connect_to_server, send_message  # Todavía no implementado

def test_client_connects():
    """Prueba que el cliente pueda conectarse correctamente."""
    with patch("socket.socket") as mock_socket:
        mock_instance = MagicMock()
        mock_socket.return_value = mock_instance

        client = connect_to_server('127.0.0.1', 5000)
        assert client is not None
        mock_instance.connect.assert_called_once_with(("127.0.0.1", 5000))

def test_client_sends_message():
    """Prueba que el cliente envía un mensaje correctamente."""
    mock_socket = MagicMock()
    mock_socket.recv.return_value = b"OK"

    response = send_message(mock_socket, "Hola servidor")
    assert response == "OK"
    mock_socket.sendall.assert_called_once_with(b"Hola servidor")

def test_send_message_empty():
    """Prueba que no se puede enviar un mensaje vacío."""
    mock_socket = MagicMock()
    result = send_message(mock_socket, "")
    assert result is False
    mock_socket.sendall.assert_not_called()