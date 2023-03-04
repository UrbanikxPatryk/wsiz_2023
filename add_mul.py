def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def calculate(fn, a, b):
    return fn(a, b)

print(calculate(add, 2, 3))

print(calculate(mul, 2, 3))