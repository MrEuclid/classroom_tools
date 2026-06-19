import itertools

letters = ['A', 'B', 'C', 'D']

for r in range(1, len(letters) + 1):
    combs = [''.join(p) for p in itertools.combinations(letters, r)]
    print(f"Groups of {r}: {combs}")

