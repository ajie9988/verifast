from verifast import validate_phone, validate_email, get_supported_countries

print("Supported countries:", get_supported_countries())

# Phone examples
for number, country in [("08123456789", "id"), ("+14155552671", "us"), ("9876543210", "in")]:
    valid, result = validate_phone(number, country)
    print(f"Phone {number} ({country}): {'Valid' if valid else 'Invalid'} -> {result}")

# Email examples
emails = ["user@example.com", "invalid-email", "test@gmail.com"]
for email in emails:
    valid, msg = validate_email(email)
    print(f"Email {email}: {'Valid' if valid else 'Invalid'} -> {msg}")