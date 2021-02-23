import sys

# A, B, C 입력받기
A, B, C = map(int, sys.stdin.readline().split())


def power(x, y):
    # 지수가 0이면 1 리턴
    if y == 0:
        return 1
    # 지수가 1이면 밑 그래도 리턴
    elif y == 1:
        return x % C
    # 지수가 홀수이면 지수 - 1 계산 값에 밑 곱하기
    elif y % 2 == 1:
        return (power(x, y - 1) * x) % C
    # 지수가 짝수이면
    else:
        # 절반을 구한다.
        tmp = power(x, y//2)
        # 절반을 제곱한다. 이때 나머지를 구하면 계산 횟수가 더 줄어든다.
        return tmp ** 2 % C


# 나머지를 출력
print(power(A, B) % C)