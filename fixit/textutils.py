"""Small text helpers."""


def is_palindrome(text: str) -> bool:
    """Check whether text reads the same forwards and backwards.

    Example:
        is_palindrome("madam") returns True.
        is_palindrome("hello") returns False.
    """

    cleaned = "".join(
        ch.lower()
        for ch in text
        if ch.isalnum()
    )
    return cleaned == cleaned[::-1]


def reverse_words(text: str) -> str:
    """Reverse the order of words in text.

    Example:
        reverse_words("hello world") returns "world hello".
    """
    return " ".join(reversed(text.split()))
