# utilities/RSA/prime_tools.py
import random

def is_prime_miller_rabin(n, k=5):
    """
    Uses the Miller-Rabin primality test.
    It is practically instantaneous for numbers with hundreds of digits.
    """
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Find r and d such that n - 1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop (runs k times for accuracy)
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_random_prime(min_digits=5, max_digits=20):
    """
    Finds a massive random prime number instantly.
    We now ask for the number of digits instead of value ranges!
    """
    min_val = 10**(min_digits - 1)
    max_val = (10**max_digits) - 1
    
    while True:
        # Pick a massive random odd number
        candidate = random.randint(min_val, max_val)
        if candidate % 2 == 0:
            candidate += 1
            
        # Test it using Miller-Rabin
        if is_prime_miller_rabin(candidate):
            return candidate