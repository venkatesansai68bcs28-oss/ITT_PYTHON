import itertools
colors = [5, 10, 15]
cycler = itertools.cycle(colors)
for _ in range(3):
    print(next(cycler))