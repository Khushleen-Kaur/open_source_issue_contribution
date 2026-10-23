from fixit.wordcount import count_chars, count_lines, count_words


def test_count_words_simple():
    assert count_words("hello world") == 2


def test_count_words_extra_spaces():
    assert count_words("hello    world") == 2


def test_count_words_empty():
    assert count_words("") == 0


def test_count_lines_trailing_newline():
    assert count_lines("a\nb\n") == 2


def test_count_lines_empty():
    assert count_lines("") == 0


def test_count_words_whitespace_only():
    assert count_words(" \t\n ") == 0


def test_count_chars():
    assert count_chars("abc") == 3
