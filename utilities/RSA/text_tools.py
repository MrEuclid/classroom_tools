# utilities/RSA/text_tools.py

def text_to_number(text, encoding='ascii'):
    """
    Converts a string of text into a single large integer.
    Encoding can be changed to 'utf-8' for Khmer characters.
    """
    try:
        # 1. Convert the text into bytes
        byte_data = text.encode(encoding)
        # 2. Glue the bytes together into an integer
        message_int = int.from_bytes(byte_data, byteorder='big')
        return message_int
    except Exception:
        return None

def number_to_text(message_int, encoding='ascii'):
    """
    Converts a large integer back into readable text.
    """
    try:
        # 1. Calculate how many bytes long the number is
        byte_length = (message_int.bit_length() + 7) // 8
        # 2. Convert integer back to bytes
        byte_data = message_int.to_bytes(byte_length, byteorder='big')
        # 3. Decode the bytes back to text
        return byte_data.decode(encoding)
    except Exception:
        return "Error: Could not decode this number. Check your key and encoding."