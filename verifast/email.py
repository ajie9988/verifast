import re

_EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def is_valid_email(email: str) -> bool:
    if not isinstance(email, str) or not email.strip():
        return False
    if ".." in email:
        return False
    if not _EMAIL_RE.fullmatch(email):
        return False

    local, domain = email.rsplit("@", 1)
    if len(local) > 64 or len(domain) > 255:
        return False

    labels = domain.split(".")
    return all(label and not label.startswith("-") and not label.endswith("-") for label in labels)
