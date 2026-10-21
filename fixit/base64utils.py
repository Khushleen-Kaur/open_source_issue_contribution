"""Base64 text encoding and decoding utilities."""

import base64
import binascii


def encode_text(text: str) -> str:
    """Encode UTF-8 text as a Base64 string."""
    encoded = base64.b64encode(text.encode("utf-8"))
    return encoded.decode("ascii")


def decode_text(text: str) -> str:
    """Decode a Base64 string into UTF-8 text."""
    try:
        encoded = text.encode("ascii")
        decoded = base64.b64decode(encoded, validate=True)
        return decoded.decode("utf-8")
    except (binascii.Error, UnicodeEncodeError, UnicodeDecodeError) as exc:
        raise ValueError("Invalid Base64 input.") from exc
