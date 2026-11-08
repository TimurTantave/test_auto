import re


def is_valid_user_name(name: str) -> bool:
    return re.fullmatch(r"name: user\d+", name) is not None