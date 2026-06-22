def decode_rsa_number(decrypted_number):
    """Converts a massive integer back into a UTF-8 string."""
    try:
        # Figure out exactly how many bytes the number takes up
        num_bytes = (decrypted_number.bit_length() + 7) // 8
        
        if num_bytes == 0:
            return ""
            
        # Convert the integer back into raw bytes (using big-endian)
        recovered_bytes = decrypted_number.to_bytes(num_bytes, 'big')
        
        # Decode the raw bytes into a human-readable string
        return recovered_bytes.decode('utf-8')
        
    except UnicodeDecodeError:
        return "[Error: Decrypted bytes do not form valid text. Check the math or private key!]"
    except Exception as e:
        return f"[Error: {e}]"