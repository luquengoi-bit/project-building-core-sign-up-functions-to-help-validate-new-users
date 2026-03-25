"""
Simple validation utilities for names and email addresses.
"""

# Preloaded data for validating email domain.
TOP_LEVEL_DOMAINS = [
    ".org",
    ".net",
    ".edu",
    ".ac",
    ".gov",
    ".com",
    ".io",
]


def validate_name(name):
    """
    Validate that the input name is a string
    and has more than 2 characters.

    :param name: str
    :return: bool
    """
    if not isinstance(name, str):
        return False

    if len(name) <= 2:
        return False

    return True


def validate_email(email):
    """
    Validate that the email has a basic correct format:
    - contains '@'
    - contains a valid top-level domain

    :param email: str
    :return: bool
    """
    if not isinstance(email, str):
        return False

    if "@" not in email:
        return False

    for domain in TOP_LEVEL_DOMAINS:
        if domain in email:
            return True

    return False
