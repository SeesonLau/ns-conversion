def decimal_to_all_bases(decimal_value):
    """Convert decimal to binary, octal, and hexadecimal"""
    try:
        decimal_int = int(decimal_value)
        binary = bin(decimal_int)[2:]
        octal = oct(decimal_int)[2:]
        hexadecimal = hex(decimal_int)[2:].upper()
        return binary, octal, hexadecimal
    except (ValueError, TypeError):
        raise ValueError("Invalid decimal number")
        