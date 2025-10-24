import pytest
from src.utils.utils import validate_message
from unittest.mock import patch

def test_validate_message_ok():
    """Mensaje válido no lanza error y retorna True"""
    result = validate_message("Hola mundo")
    assert result is True

def test_validate_message_empty():
    """Mensaje vacío lanza ValueError"""
    with pytest.raises(ValueError):
        validate_message("")

def test_validate_message_spaces():
    """Mensaje solo con espacios lanza ValueError"""
    with pytest.raises(ValueError):
        validate_message("     ")

def test_logger_called_for_valid_message():
    """Verifica que se llame al logger cuando el mensaje es válido"""
    with patch("src.utils.message_utils.logging.info") as mock_log:
        validate_message("Test logger")
        mock_log.assert_called_with("Mensaje validado: Test logger")