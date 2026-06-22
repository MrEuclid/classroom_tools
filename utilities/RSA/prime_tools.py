# utilities/RSA/prime_tools.py
import random
import math

def is_prime(n):
    """
    Checks if a number is prime using trial division.
    Perfectly fast for numbers up to a few million.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    # Eliminate even numbers and multiples of 3 instantly
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check odd numbers up to the square root of n
    limit = int(math.sqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
            
    return True

def generate_random_prime(min_val=10000, max_val=50000):
    """
    Finds a random prime number within a specific range.
    """
    while True:
        # Pick a random odd number
        candidate = random.randint(min_val, max_val)
        if candidate % 2 == 0:
            candidate += 1
            
        # Check if it's prime. If it is, return it. If not, the loop repeats.
        if is_prime(candidate):
            return candidate