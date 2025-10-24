import pytest
from src.utils.utils import validate_message

def test_message_not_empty():
    """
    El mensaje no puede estar vacío.
    """
    invalid_message1 = ""
    invalid_message2 = "   "

    with pytest.raises(ValueError):
        validate_message(invalid_message1)

    with pytest.raises(ValueError):
        validate_message(invalid_message2)

    # Mensaje que no es string -> ValueError
    with pytest.raises(ValueError):
        validate_message(None)

def test_message_valid():
    """
    El mensaje debe ser válido.
    """
    valid_message = "Hola, este es un mensaje válido."

    assert validate_message(valid_message) is True