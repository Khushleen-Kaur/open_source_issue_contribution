import pytest

from fixit import base64utils, cli


def test_encode_text():
    assert base64utils.encode_text("hello") == "aGVsbG8="


def test_decode_text():
    assert base64utils.decode_text("aGVsbG8=") == "hello"


def test_encode_unicode_text():
    text = "\u0928\u092e\u0938\u094d\u0924\u0947"
    assert base64utils.decode_text(base64utils.encode_text(text)) == text


def test_empty_text():
    assert base64utils.encode_text("") == ""
    assert base64utils.decode_text("") == ""


@pytest.mark.parametrize("value", ["%%%", "aGVsbG8", "////"])
def test_invalid_base64_or_non_utf8_text(value):
    with pytest.raises(ValueError, match="Invalid Base64 input"):
        base64utils.decode_text(value)


def test_cli_encode(capsys):
    assert cli.main(["base64", "encode", "hello"]) == 0
    assert capsys.readouterr().out == "aGVsbG8=\n"


def test_cli_decode(capsys):
    assert cli.main(["base64", "decode", "aGVsbG8="]) == 0
    assert capsys.readouterr().out == "hello\n"


def test_cli_invalid_base64(capsys):
    assert cli.main(["base64", "decode", "%%%"]) == 1
    captured = capsys.readouterr()
    assert "Invalid Base64 input" in captured.err
