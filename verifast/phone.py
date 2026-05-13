from .utils import load_country_rules, normalize_phone


def is_valid_phone(phone: str, country: str = "us") -> bool:
    if not isinstance(phone, str) or not phone.strip():
        return False

    try:
        rules = load_country_rules(country)
    except FileNotFoundError:
        return False

    normalized = normalize_phone(phone)
    if not normalized:
        return False

    country_code = str(rules.get("country_code", ""))

    if normalized.startswith("+"):
        normalized = normalized[1:]
    elif normalized.startswith("00"):
        normalized = normalized[2:]

    if country_code and normalized.startswith(country_code):
        normalized = normalized[len(country_code) :]

    if not normalized.isdigit():
        return False

    min_length = int(rules.get("min_length", 7))
    max_length = int(rules.get("max_length", 15))
    return min_length <= len(normalized) <= max_length
