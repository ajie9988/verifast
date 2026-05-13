import json
from importlib import resources


def load_country_rules(country: str) -> dict:
    code = country.lower()
    with resources.files("verifast.data").joinpath(f"{code}.json").open("r", encoding="utf-8") as f:
        return json.load(f)


def normalize_phone(value: str) -> str:
    return "".join(ch for ch in value if ch.isdigit() or ch == "+")
