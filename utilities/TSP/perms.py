import itertools

def get_permutations(codes):
    # If the input is a single string from a text box (e.g., "PNH, BKK, SIN"), 
    # split it into a list and clean up any extra spaces.
    if isinstance(codes, str):
        codes = [code.strip().upper() for code in codes.split(',')]
        
    # Generate all possible permutations of the list items
    # Join them with an arrow to represent a travel route
    perm_list = [' -> '.join(p) for p in itertools.permutations(codes)]
    
    return perm_list

# --- Example Usage ---
# You can pass a string:
# routes = get_permutations("PNH, BKK, SIN")

# Or you can pass a list directly:
# routes = get_permutations(['PNH', 'BKK', 'SIN', 'NRT'])

# print(routes)