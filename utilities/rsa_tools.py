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