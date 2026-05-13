import json
import re
from pathlib import Path
from typing import Dict, Optional, Tuple, List

_DATA_CACHE: Dict[str, Dict] = {}
_DATA_DIR = Path(__file__).parent / "data"

def get_supported_countries() -> List[str]:
    """Return list of supported country codes (e.g., ['id', 'us', 'in'])"""
    return [p.stem for p in _DATA_DIR.glob("*.json")]

def _load_country_data(country_code: str) -> Dict:
    country_code = country_code.lower()
    if country_code in _DATA_CACHE:
        return _DATA_CACHE[country_code]
    
    path = _DATA_DIR / f"{country_code}.json"
    if not path.exists():
        raise ValueError(f"Country '{country_code}' not supported. Supported: {get_supported_countries()}")
    
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    _DATA_CACHE[country_code] = data
    return data

def normalize_phone(number: str, country_code: str = "id") -> str:
    """
    Convert phone number to international format (e.g., +628123456789)
    """
    rules = _load_country_data(country_code)
    cc = rules["country_code"]
    
    # Remove all non-digit except leading '+'
    cleaned = re.sub(r"[^\d+]", "", number.strip())
    
    # If already starts with +<cc>, return as-is
    if cleaned.startswith(f"+{cc}"):
        return cleaned
    
    # If starts with 00<cc>, replace with +
    if cleaned.startswith(f"00{cc}"):
        return f"+{cc}{cleaned[2+len(cc):]}"
    
    # If starts with <cc> (without + or 00)
    if cleaned.startswith(cc) and not cleaned.startswith("0"):
        return f"+{cleaned}"
    
    # If starts with 0 (local dialing)
    if cleaned.startswith("0"):
        return f"+{cc}{cleaned[1:]}"
    
    # Otherwise, assume missing country code (add it)
    return f"+{cc}{cleaned}"

def validate_phone(number: str, country_code: str = "id") -> Tuple[bool, Optional[str]]:
    """
    Validate phone number.
    Returns (is_valid, normalized_or_error_message)
    """
    if not number or not isinstance(number, str):
        return False, "Phone number must be a non-empty string"
    
    try:
        rules = _load_country_data(country_code)
    except ValueError as e:
        return False, str(e)
    
    # Try to normalize first
    try:
        normalized = normalize_phone(number, country_code)
    except Exception:
        return False, "Failed to normalize number"
    
    # Extract digits after country code
    if not normalized.startswith(f"+{rules['country_code']}"):
        return False, f"Number must have country code +{rules['country_code']}"
    
    local_part = normalized[len(rules['country_code'])+1:]  # after +62
    
    # Check length constraints
    if not (rules["min_length"] <= len(local_part) <= rules["max_length"]):
        return False, f"Length must be between {rules['min_length']} and {rules['max_length']} digits"
    
    # Check pattern
    # Build full pattern with optional + and country code
    pattern = rules["phone_pattern"]
    # Re-pattern allows +, 00, or 0 prefix
    full_pattern = f"^(\\+{rules['country_code']}|{rules['country_code']}|0){local_part}$"
    
    # Simpler: just check the normalized form
    if not re.match(rules["phone_pattern"], normalized):
        return False, f"Number does not match {rules['country_name']} format"
    
    return True, normalized