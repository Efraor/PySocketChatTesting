import pytest
from src.utils import validate_message

def test_message_not_empty():
    """
    El mensaje no puede estar vacío.
    """
    invalid_message = ""

    with pytest.raises(ValueError):
        validate_message(invalid_message)

def test_message_valid():
    """
    El mensaje debe ser válido.
    """
    valid_message = "Hola, este es un mensaje válido."

    assert validate_message(valid_message) is True