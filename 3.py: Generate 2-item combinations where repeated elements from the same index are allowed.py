import itertools
items = [1, 2]
comb_rep = list(itertools.combinations_with_replacement(items, 2))
print(comb_rep)