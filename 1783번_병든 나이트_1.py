import sys

height, width = map(int, sys.stdin.readline().split())


# 결과
result = 0

# height가 3 이상인 경우
# width가 7 이상인 경우
if height >=3 and width >= 7:
    result = (width - 7) + 5
# 나이트가 움직일 수 없는 경우
elif height == 1 or width == 1:
    result = 1
# 나이트가 위로는 제한이 없지만 오른쪽으로 제한이 있어 한계가 있다.
elif height >= 3 and width < 4:
    result = width
# 나이트가 위로는 제한이 없지만 오른쪽으로 제한이 있어 한계가 있다.
elif height >= 3 and width < 7:
    result = 4
# 나이트가 위로 제한이 있고 오른쪽으로 제한이 없을 때
elif height < 3 and width >= 7:
    result = 4
# 나이트가 위로 제한이 있고 오른쪽으로도 제한이 있을 때
elif height < 3 and width < 7:
    result = ((width - 1) // 2) + 1




print(result)
