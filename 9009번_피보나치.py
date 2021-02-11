import sys

def solve(x):
    result = []
    a = [0, 1]

    # 피보나치 수열 생성
    while a[-1] < x:
        a.append(a[-1] + a[-2])
    
    # 입력 값보다 작거나 같은 피보나치 수열 중 가장 큰 값 빼고 결과 리스트에 추가
    for i in range(1, len(a)):
        if a[-i] <= x:
            x -= a[-i]
            result.append(a[-i])
            if x == 0:
                break
        
    
    # 결과 리스트 반환
    return(result)

# 횟수 입력
N = int(sys.stdin.readline())

# 정답 리스트 생성
answer = []

# 정답 리스트에 결과 리스트 계산하여 추가
for _ in range(N):
    answer.append(solve(int(sys.stdin.readline())))

# 결과 리스트 거꾸로 출력
for j in range(N):
    for i in range(1, len(answer[j]) + 1):
        print(answer[j][-i], end=' ')
    print()

    
    