# Verifast 🚀

**Verifast** is a lightweight, extensible Python library for cross-country phone number and email validation.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

[![Tests](https://github.com/ajie9988/verifast/actions/workflows/test.yml/badge.svg)](https://github.com/ajie9988/verifast/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## ✨ Features

- **Phone Validation**: Validate and normalize phone numbers for multiple countries.
- **Email Validation**: RFC-compliant validation with optional disposable domain blocking.
- **Extensible**: Add new country rules via simple JSON files.
- **Clean API**: Consistent return types `(is_valid, result)`.

```markdown
## ⚠️ Limitations

- Phone validation checks **format only**, not whether the number actually exists
- Email validation does not verify if the inbox exists (no SMTP check)
- Country codes must be specified explicitly (auto-detection coming soon)

## 📖 Documentation

- [English Documentation (README)](#usage)
- [**Panduan Bahasa Indonesia (GUIDE.md)**](GUIDE.md)

## 🚀 Quick Start

### Installation

```bash
pip install .
```

### Basic Usage

```python
from verifast import validate_phone, validate_email

# Phone Validation
is_valid, result = validate_phone("08123456789", "id")
# returns (True, "+628123456789")

# Email Validation
is_valid, result = validate_email("hello@verifast.io")
# returns (True, "hello@verifast.io")
```

## 🌍 Supported Countries

Currently supports: `ID`, `US`, `IN`, `CN`, `DE`.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
