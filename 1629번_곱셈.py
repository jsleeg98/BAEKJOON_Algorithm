import sys

A, B, C = map(int, sys.stdin.readline().split())


def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2 == 1:
        return power(x, y - 1) * x
    else:
        tmp = power(x, y//2)
        return tmp ** 2 % C



print(power(A, B) % C)