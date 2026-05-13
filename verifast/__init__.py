from .phone import validate_phone, normalize_phone, get_supported_countries
from .email import validate_email, normalize_email

__version__ = "0.1.0"
__all__ = [
    "validate_phone",
    "normalize_phone",
    "get_supported_countries",
    "validate_email",
    "normalize_email",
]
