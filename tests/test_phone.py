from verifast.phone import validate_phone, normalize_phone, get_supported_countries

def test_id_phone():
    assert validate_phone("08123456789", "id")[0] is True
    assert validate_phone("+628123456789", "id")[0] is True
    assert validate_phone("628123456789", "id")[0] is True
    assert validate_phone("08123", "id")[0] is False  # too short
    assert validate_phone("0211234567", "id")[0] is True  # landline

def test_us_phone():
    assert validate_phone("+14155552671", "us")[0] is True
    assert validate_phone("4155552671", "us")[0] is True
    assert validate_phone("14155552671", "us")[0] is True
    assert validate_phone("1234567890", "us")[0] is False

def test_in_phone():
    assert validate_phone("+919876543210", "in")[0] is True
    assert validate_phone("9876543210", "in")[0] is True
    # Nomor India VALID: 10 digit setelah 0 atau +91
    assert validate_phone("09876543210", "in")[0] is True  # 0 + 10 digit
    # HAPUS baris yang pakai 0919876543210 karena terlalu panjang (11 digit setelah 09)

def test_normalize():
    assert normalize_phone("08123456789", "id") == "+628123456789"
    assert normalize_phone("628123456789", "id") == "+628123456789"
    assert normalize_phone("4155552671", "us") == "+14155552671"

def test_supported_countries():
    countries = get_supported_countries()
    assert "id" in countries
    assert "us" in countries
    assert "in" in countries