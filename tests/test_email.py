from verifast.email import is_valid_email


def test_valid_email():
    assert is_valid_email("user.name+tag@example.com")


def test_invalid_email_missing_at():
    assert not is_valid_email("user.example.com")


def test_invalid_email_double_dot():
    assert not is_valid_email("user..name@example.com")


def test_invalid_email_domain_hyphen_edges():
    assert not is_valid_email("user@-example.com")


def test_invalid_email_domain_hyphen_end():
    assert not is_valid_email("user@example-.com")


def test_invalid_email_local_part_dot_edges():
    assert not is_valid_email("user.@example.com")
    assert not is_valid_email(".user@example.com")


def test_invalid_email_length_limits():
    assert not is_valid_email(f"{'a' * 65}@example.com")
    long_domain = f"user@{('a' * 64 + '.') * 4}com"
    assert not is_valid_email(long_domain)
