import sys

# 초기 숫자 A, 바꿀 숫자 B
A, B = sys.stdin.readline().split()

# 바꾼 횟수
count = 0

# 바꿀 숫자가 더 큰 동안 반복
while int(A) < int(B):
    # 마지막 수가 1이면 1 지우기
    if B[-1] == str(1):
        tmp = list(B)
        del tmp[-1]
        B = str(''.join(tmp))
    # 짝수이면 2로 나누기
    elif int(B) % 2 == 0:
        B = str(int(int(B) / 2))
    # 둘다 아니면 멈춤
    else:
        break

    # 계속 바꾼 횟수 추가
    count += 1

# 결과가 같다면 바꾼횟수에 1 추가한 값 출력
if B == A:
    print(count + 1)
# 같지 않다면 -1 출력
else:
    print(-1)

