"""verifast public API."""

from .email import is_valid_email
from .phone import is_valid_phone

__all__ = ["is_valid_email", "is_valid_phone"]
