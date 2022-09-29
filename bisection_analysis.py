from math import e

def f(c, m=68.1, v=40, t=10):
    g = 9.8
    return v - g * m / c * (1 - e ** (-(c / m)*t))

c = 1
eps = 1e-10

a = 1
b = 1000

while b - a > eps:
    c = (a + b) / 2
    if f(a) * f(c) < 0: b = c
    else: a = c

print(c)