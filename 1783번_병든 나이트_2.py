import sys

height, width = map(int, sys.stdin.readline().split())


# 결과
result = 0

if height == 1:
    result = 1
elif height == 2:
    result = min(4, width+1//2)
elif width < 7:
    result = min(4, width)
else:
    result = (width - 7) + 5



print(result)
