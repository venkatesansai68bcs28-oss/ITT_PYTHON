import itertools
items = ['a', 'b']
cyclic_gen = itertools.cycle(items)
sliced = list(itertools.islice(cyclic_gen, 6))
print(sliced)