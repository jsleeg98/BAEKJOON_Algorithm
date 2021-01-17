import sys

# 숫자 개수
N = int(sys.stdin.readline())

# 숫자 배열 입력
minus = []
plus = []
one = []

# 결과 0으로 초기화
maximum = 0

for _ in range(N):
    tmp = int(sys.stdin.readline())
    if tmp > 0 :
        if tmp == 1:
            one.append(tmp)
        else:
            plus.append(tmp)
    else:
        minus.append(tmp)


# minus 내림차순 정렬
minus.sort(reverse = True)

# plus 오름차순 정렬
plus.sort()

def multi_plus(x):
    result = 0
    # 리스트 길이가 짝수인 경우
    if len(x) % 2 == 0:
        for _ in range(len(x) // 2):
            result += x.pop() * x.pop()
    # 리스트 길이가 홀수인 경우
    else:
        for _  in range(len(x) // 2):
            result += x.pop() * x.pop()
        # 남은 원소 더해주기
        result += x.pop()
    return result

# 결과 연산
maximum = multi_plus(minus) + multi_plus(plus) + len(one)

print(maximum)