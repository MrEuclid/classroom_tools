import itertools

letters = ['A', 'B', 'C']
perms = [''.join(p) for p in itertools.permutations(letters)]

print(perms)
