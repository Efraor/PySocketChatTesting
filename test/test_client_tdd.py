from src.client import send_message

def test_send_empty_message_is_rejected():
    result = send_message(None, "")
    assert result is False
