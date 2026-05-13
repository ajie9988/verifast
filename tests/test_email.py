from verifast.email import is_valid_email


def test_valid_email():
    assert is_valid_email("user.name+tag@example.com")


def test_invalid_email_missing_at():
    assert not is_valid_email("user.example.com")


def test_invalid_email_double_dot():
    assert not is_valid_email("user..name@example.com")


def test_invalid_email_domain_hyphen_edges():
    assert not is_valid_email("user@-example.com")
