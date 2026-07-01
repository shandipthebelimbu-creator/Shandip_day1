"""
Data validation functions.
"""
def validate_isbn(isbn):
    # Remove hyphens
    isbn = isbn.replace("-", "")

    # Must be exactly 13 digits
    if len(isbn) != 13:
        return False

    # Must contain only digits
    if not isbn.isdigit():
        return False

    # Calculate check digit from first 12 digits
    total = 0
    for i in range(12):
        digit = int(isbn[i])

        if i % 2 == 0:
            total += digit

        else:
            total += digit * 3

    check_digit = (10 - (total % 10)) % 10

    return check_digit == int(isbn[12])