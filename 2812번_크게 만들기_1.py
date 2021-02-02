import sys

N, K = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().strip()))

result = []
K_save = K

for i in range(N):
    # 지울 개수 0 초과 and 결과 리스트 길이 0이상 and 결과 마지막 인덱스 값 < 입력 값
    while K > 0 and len(result) > 0 and result[-1] < num[i]:
        # 결과 마지막 인덱스 값 삭제
        del result[-1]
        # 지울 개수 1 감소
        K -= 1

    # 입력 값 결과 리스트에 추가    
    result.append(num[i])

# 결과 리스트 출력
# N-k만큼만 출력
for j in range(N-K_save):
    print(result[j], end='')


