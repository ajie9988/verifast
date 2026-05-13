from verifast import validate_phone, normalize_phone, validate_email, get_supported_countries

# 1. Check Supported Countries
print(f"Supported countries: {get_supported_countries()}")

# 2. Validate & Normalize Phone Numbers
phones = [
    ("08123456789", "id"),
    ("4155552671", "us"),
    ("9876543210", "in"),
    ("invalid", "id"),
]

print("\n--- Phone Validation ---")
for num, country in phones:
    is_valid, result = validate_phone(num, country)
    if is_valid:
        print(f"✅ {num} ({country}) -> Normalized: {result}")
    else:
        print(f"❌ {num} ({country}) -> Error: {result}")

# 3. Validate & Normalize Emails
emails = [
    "hello@verifast.io",
    "  USER@example.COM  ",
    "invalid-email",
]

print("\n--- Email Validation ---")
for email in emails:
    is_valid, result = validate_email(email)
    if is_valid:
        print(f"✅ {email} -> Normalized: {result}")
    else:
        print(f"❌ {email} -> Error: {result}")
