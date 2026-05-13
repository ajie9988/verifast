from verifast.phone import is_valid_phone


def test_valid_us_phone():
    assert is_valid_phone("+1 202-555-0199", "us")


def test_valid_id_phone():
    assert is_valid_phone("+62 81234567890", "id")


def test_invalid_phone_too_short():
    assert not is_valid_phone("12345", "us")


def test_invalid_unknown_country():
    assert not is_valid_phone("2025550199", "zz")


def test_valid_us_phone_with_00_prefix():
    assert is_valid_phone("0012025550199", "us")
