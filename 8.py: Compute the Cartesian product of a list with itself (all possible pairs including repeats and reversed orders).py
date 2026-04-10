import itertools
colors = ['red', 'green', 'blue']
products = list(itertools.product(colors, repeat=2))
print(products)