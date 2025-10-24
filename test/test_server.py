import pytest
from unittest.mock import patch, MagicMock
from src.server import start_server, accept_clients, handle_client, broadcast_message
from src.utils import message_utils

HOST, PORT = '127.0.0.1', 5000

def test_server_starts():
    """Server starts without raising exceptions."""
    with patch("socket.socket") as mock_socket:
        mock_instance = MagicMock()
        mock_socket.return_value = mock_instance

        result = start_server(HOST, PORT)
        assert result is True
        mock_instance.bind.assert_called_once()
        mock_instance.listen.assert_called_once()

def test_handle_client_receives_message():
    """Server handles a single client message correctly."""
    mock_client = MagicMock()
    mock_client.recv.side_effect = [b"Hello Server", b""]

    with patch("src.server.validate_message", return_value=True) as mock_validate:
        handle_client(mock_client, ("127.0.0.1", 5000))
        mock_validate.assert_called_once_with("Hello Server")
        mock_client.sendall.assert_called_once_with(b"Mensaje recibido.")
        mock_client.close.assert_called_once()

def test_broadcast_message():
    """Server sends a message to all clients except sender."""
    sender = MagicMock()
    client1 = MagicMock()
    client2 = MagicMock()

    from src import server
    server.clients = [sender, client1, client2]

    broadcast_message("Broadcast Test", sender)

    client1.sendall.assert_called_once_with(b"Broadcast Test")
    client2.sendall.assert_called_once_with(b"Broadcast Test")
    sender.sendall.assert_not_called()

    # Cleanup
    server.clients = []
