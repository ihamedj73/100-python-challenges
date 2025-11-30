def add(*args):
    total = 0
    for num in args:
        total += num

    return total


def calculator(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs["multiply"]
    print(n)


calculator(2, add=3, multiply=5)
