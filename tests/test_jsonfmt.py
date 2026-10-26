import pytest

from fixit.jsonfmt import format_json


def test_format_json():
    assert format_json('{"a":1}') == '{\n  "a": 1\n}'


def test_invalid_json_friendly_error():
    with pytest.raises(ValueError, match="Invalid JSON"):
        format_json("{not json")


def test_format_json_sort_keys():
    raw = '{"b": 1, "a": 2}'
    assert format_json(raw, sort_keys=True) == '{\n  "a": 2,\n  "b": 1\n}'
    assert format_json(raw, sort_keys=False) == '{\n  "b": 1,\n  "a": 2\n}'

