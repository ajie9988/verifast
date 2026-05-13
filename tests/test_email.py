from verifast.email import validate_email, normalize_email

def test_valid_emails():
    valid, result = validate_email("user@example.com")
    assert valid is True
    assert validate_email("user.name+tag@domain.co.id")[0] is True
    assert validate_email("test@gmail.com")[0] is True

def test_invalid_emails():
    valid, result = validate_email("invalid-email")
    assert valid is False
    assert validate_email("missing@dot")[0] is False
    assert validate_email("@missinglocal.com")[0] is False
    assert validate_email("")[0] is False

def test_normalize():
    assert normalize_email("  User@Example.COM  ") == "user@example.com"
    assert normalize_email("TEST@GMAIL.COM") == "test@gmail.com"