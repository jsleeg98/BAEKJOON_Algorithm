import sys

# 줄의 개수 입력
N = int(sys.stdin.readline())

# 로프가 버틸 수 있는 중량 리스트
li = []

for i in range(N):
    li.append(int(sys.stdin.readline()))

# 내림차순 정렬
li.sort(reverse = True)

# 로프가 버틸 수 있는 중량 초기화
w = li[0]


for i in range(1, N):
    # 줄을 추가 했을 때 버틸 수 있는 중량
    temp = li[i] * (i + 1)
    # 추가하면 안되는 경우
    if temp < w:
        break
    else:
        w = temp
    

print(w)
