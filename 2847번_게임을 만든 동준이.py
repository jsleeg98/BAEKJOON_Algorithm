import sys

# 문제 개수 입력 받기
N = int(sys.stdin.readline())

# 문제 점수 입력 받기
scores = []

for _ in range(N):
    scores.append(int(sys.stdin.readline()))

# 문제 접수 리스트 뒤집기
scores.reverse()

# 조정한 횟수 0으로 초기화
count = 0

# 조정한 횟수 계산
for i in range(N - 1):
    if scores[i] <= scores[i + 1]:
        count += scores[i + 1] - scores[i] + 1 # 점수 차이에서 1 더 빼주어야하기 때문에 횟수 차이에 1 추가
        scores[i + 1] = scores[i + 1] - (scores[i + 1] - scores[i] + 1) # 점수는 횟수 차이에 1을 더 빼주어야 최소 조정 값
        
# 결과 출력
print(count)