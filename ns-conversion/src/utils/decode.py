def decode_message(encoded_values, key, is_hex=False):
    """Decode message by subtracting key from encoded values"""
    if not encoded_values:
        raise ValueError("Encoded values cannot be empty")
    
    try:
        key_int = int(key)
    except ValueError:
        raise ValueError("Key must be a valid integer")
    
    decoded_chars = []
    
    if is_hex:
        # Handle hex input (comma-separated values)
        hex_values = [val.strip() for val in encoded_values.split(',')]
        for hex_val in hex_values:
            if hex_val:
                decimal_val = int(hex_val, 16)
                decoded_val = decimal_val - key_int
                decoded_chars.append(chr(decoded_val))
    else:
        # Handle decimal input (comma-separated values)
        decimal_values = [val.strip() for val in encoded_values.split(',')]
        for decimal_val in decimal_values:
            if decimal_val:
                decoded_val = int(decimal_val) - key_int
                decoded_chars.append(chr(decoded_val))
    
    return ''.join(decoded_chars)
    