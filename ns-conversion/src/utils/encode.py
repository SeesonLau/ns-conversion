def encode_message(message, key):
    """Encode message by adding key to each character's ASCII value"""
    if not message:
        raise ValueError("Message cannot be empty")
    
    try:
        key_int = int(key)
    except ValueError:
        raise ValueError("Key must be a valid integer")
    
    decimal_values = []
    hex_values = []
    
    for char in message:
        ascii_val = ord(char)
        encoded_val = ascii_val + key_int
        decimal_values.append(str(encoded_val))
        hex_values.append(hex(encoded_val)[2:].upper().zfill(2))
    
    return decimal_values, hex_values
    