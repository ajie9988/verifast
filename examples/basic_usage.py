from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from verifast import is_valid_email, is_valid_phone

print(is_valid_email("hello@example.com"))
print(is_valid_phone("+1 202-555-0199", "us"))
