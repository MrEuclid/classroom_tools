# Inside utilities/rsa_tools.py

def modular_exponentiation(base, exponent, modulus):
    """
    Calculates (base^exponent) % modulus using the highly efficient 
    Square and Multiply algorithm.
    """
    try:
        # We ensure they are integers before running the math
        return pow(int(base), int(exponent), int(modulus))
    except ValueError:
        # Returns None if the user typed something invalid
        return None
    except ZeroDivisionError:
        # Modulo cannot be 0
        return "Error: Modulus cannot be zero."


def calculate_private_key(e, phi_n):
    """
    Calculates the modular multiplicative inverse to find the private key (d).
    Mathematically: (d * e) % phi_n = 1
    """
    try:
        # The -1 exponent tells Python to find the modular inverse!
        return pow(int(e), -1, int(phi_n))
    except ValueError:
        # Python throws a ValueError if the inverse doesn't exist 
        # (meaning 'e' and 'phi_n' share a common factor)
        return "Error: Your public key (e) shares a factor with phi(n). Choose a different e!"
    except Exception:
        return None
