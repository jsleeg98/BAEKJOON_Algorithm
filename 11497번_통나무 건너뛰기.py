import sys

N = int(sys.stdin.readline())

result_list = []

for _ in range(N):
    M = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    # 오름차순 정렬
    heights.sort()
    result = 0
    # 짝수 인덱스 비교
    for i in range(0, M - 2, 2):
        tmp = heights[i + 2] - heights[i]
        if(tmp > result):
            result = tmp
    # 홀수 인덱스 비교
    for i in range(1, M - 2, 2):
        tmp = heights[i + 2] - heights[i]
        if(tmp > result):
            result = tmp
    
    # 결과 리스트에 추가
    result_list.append(result)

# 결과 출력
for i in result_list:
    print(i)

