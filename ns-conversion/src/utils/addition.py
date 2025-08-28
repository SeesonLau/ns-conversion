def add_numbers(num1, base1, num2, base2):
    """Add two numbers with different bases"""
    try:
        # Convert both numbers to decimal
        decimal1 = int(num1, base1)
        decimal2 = int(num2, base2)
        
        # Calculate sum in decimal
        decimal_sum = decimal1 + decimal2
        
        # Convert to different bases
        binary = bin(decimal_sum)[2:]
        octal = oct(decimal_sum)[2:]
        hexadecimal = hex(decimal_sum)[2:].upper()
        
        return decimal_sum, binary, octal, hexadecimal
    except (ValueError, TypeError):
        raise ValueError(f"Invalid numbers for the specified bases")
        