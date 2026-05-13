import re
from typing import Tuple, Optional

# RFC 5322 inspired but practical
EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)

# Common typos or disposable domains (can be extended)
COMMON_DOMAINS = {"gmail.com", "yahoo.com", "outlook.com", "protonmail.com"}
DISPOSABLE_DOMAINS = {"tempmail.com", "throwaway.com", "mailinator.com"}  # example

def validate_email(email: str, block_disposable: bool = False) -> Tuple[bool, Optional[str]]:
    """
    Validate email format. Optionally block disposable email domains.
    Returns (is_valid, error_message_or_normalized_email)
    """
    if not email or not isinstance(email, str):
        return False, "Email must be a non-empty string"
    
    email = email.strip().lower()
    
    if not EMAIL_PATTERN.match(email):
        return False, "Invalid email format (missing @, dot, or invalid characters)"
    
    # Optional: block disposable domains
    if block_disposable:
        domain = email.split("@")[-1]
        if domain in DISPOSABLE_DOMAINS:
            return False, f"Disposable email domain '{domain}' is not allowed"
    
    return True, email

def normalize_email(email: str) -> str:
    """Return normalized email (lowercase, stripped)"""
    return email.strip().lower()