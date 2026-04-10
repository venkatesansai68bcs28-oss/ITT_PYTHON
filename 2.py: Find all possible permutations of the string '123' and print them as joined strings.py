import itertools
perms = list(itertools.permutations('123'))
for p in perms:
    print(''.join(p))