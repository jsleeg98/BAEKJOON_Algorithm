import sys

n, m = map(int, sys.stdin.readline().split())

# 분자
a = 1

# 분모
b = 1

for i in range(m):
    a *= (n - i)

for i in range(m):
    b *= (i + 1)



print(a//b) 

 