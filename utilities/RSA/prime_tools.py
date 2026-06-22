def generate_random_prime(digits=3):
    """
    Finds a random prime number with an exact number of digits.
    Restricted to a minimum of 2 digits and a maximum of 20 digits.
    """
    # Enforce the allowed constraints (clamp between 2 and 20)
    digits = max(2, min(20, digits))
    
    # Calculate exact bounds for the requested number of digits
    min_val = 10**(digits - 1)
    max_val = (10**digits) - 1
    
    while True:
        # Pick a random odd number within the exact digit bounds
        candidate = random.randint(min_val, max_val)
        if candidate % 2 == 0:
            candidate += 1
            
        # Test it using Miller-Rabin
        if is_prime_miller_rabin(candidate):
            return candidate