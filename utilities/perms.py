import itertools

def get_permutations(text):
    # Generates all possible permutations of the full input string
    perm_list = [''.join(p) for p in itertools.permutations(text)]
    return perm_list
