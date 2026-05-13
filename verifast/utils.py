import json
from pathlib import Path
from typing import Dict, Any

def export_country_data(country_code: str, filepath: str = None) -> Dict[str, Any]:
    """Load and return country data as dict."""
    path = Path(__file__).parent / "data" / f"{country_code}.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)