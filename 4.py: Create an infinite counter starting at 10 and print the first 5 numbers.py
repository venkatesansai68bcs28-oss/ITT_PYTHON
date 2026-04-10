import itertools
counter = itertools.count(10)
for _ in range(5):
    print(next(counter))