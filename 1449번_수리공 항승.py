import sys

# 새는 곳 수와 테이프 길이 입력
N, K = map(int, sys.stdin.readline().split())

# 새는 곳 리스트
leak = list(map(int, sys.stdin.readline().split()))

# 새는 곳 오름차순 정렬
leak.sort()

# 테이프 개수 초기화
count = 0

# 테이프 시작 지점 초기화
start = leak[0]
# 테이프 1개 사용으로 시작
count += 1

for i in range(1, N):
    if start + K - 1 < leak[i]: # 새 테이프가 필요한 경우
        count += 1 # 테이프 개수 더하기
        start = leak[i] # 테이프 시작 지점 갱신
    
# 결과 출력
print(count)