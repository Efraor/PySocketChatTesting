"""
Pruebas unitarias para el servidor
- Inicialización
- Conexión de clientes
- Recepción de mensajes
"""

import pytest
from src.server import start_server  # Todavía no implementado

def test_server_starts():
    """
    Verifica que el servidor puede iniciar sin errores.
    """
    assert start_server() is True
