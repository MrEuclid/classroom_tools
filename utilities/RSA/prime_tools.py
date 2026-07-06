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

def generate_random_prime(digits=3):
    """
    Finds a random prime number with an exact number of digits.
    Restricted to a minimum of 2 digits and a maximum of 20 digits.
    """
    # Enforce constraints and guarantee it is an integer
    digits = int(max(2, min(20, digits)))
    
    # Calculate exact bounds and force them to be integers
    min_val = int(10**(digits - 1))
    max_val = int((10**digits) - 1)
    
    while True:
        # Pick a random odd number within the exact digit bounds
        candidate = random.randint(min_val, max_val)
        if candidate % 2 == 0:
            candidate += 1
            
        # Test it using Miller-Rabin
        if is_prime_miller_rabin(candidate):
            return candidate

import math
import random

def crack_rsa_modulus(n):
    """
    Uses Pollard's rho algorithm to rapidly factor a semi-prime n.
    Includes a randomized polynomial to prevent infinite loops on specific composites like 703.
    """
    if n % 2 == 0:
        return 2, n // 2
    
    # Run the algorithm, changing the 'c' offset if it fails
    for attempt in range(5): 
        # Pick a random constant for the polynomial to avoid fixed-point traps
        c = random.randint(1, n - 1)
        
        def f(x):
            return (x**2 + c) % n
            
        x = 2
        y = 2
        d = 1
        
        max_steps = 2000000 
        steps = 0
        
        while d == 1 and steps < max_steps:
            x = f(x)           # Tortoise moves 1 step
            y = f(f(y))        # Hare moves 2 steps
            
            d = math.gcd(abs(x - y), n)
            steps += 1
            
        # Solved! We found a prime factor.
        if d != n and d != 1:
            return d, n // d 
            
    # If it fails after 5 random attempts, it is highly likely prime
    return None, None

def get_prime_factors(n):
    """Returns a set of unique prime factors for a given number n."""
    factors = set()
    # Check for divisibility by 2
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    
    # Check for odd prime factors up to the square root of n
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 2
        
    # If n is still greater than 2, it is a prime factor itself
    if n > 2:
        factors.add(n)
        
    return factors

def find_primitive_roots(p, max_results=10):
    """Finds up to 'max_results' primitive roots modulo a prime p."""
    if not is_prime(p): 
        return []
        
    if p == 2:
        return [1]
        
    phi = p - 1
    factors = get_prime_factors(phi)
    
    roots = []
    
    for g in range(2, p):
        is_primitive = True
        for q in factors:
            if pow(g, phi // q, p) == 1:
                is_primitive = False
                break
                
        if is_primitive:
            roots.append(g)
            # Stop once we have enough examples for the students
            if len(roots) >= max_results:
                break
                
    return roots