import sys

N, K = map(int, sys.stdin.readline().split())

# 문자열을 바로 리스트로 저장
num = list(sys.stdin.readline().strip())

result = []
K_save = K

for i in range(N):
    # 지울 개수 0 초과 and 결과 리스트 길이 0이상 and 결과 마지막 인덱스 값 < 입력 값
    while K and result and result[-1] < num[i]:
        # 결과 마지막 인덱스 값 삭제
        result.pop()
        # 지울 개수 1 감소
        K -= 1

    # 입력 값 결과 리스트에 추가    
    result.append(num[i])

# 결과 리스트 출력
# 리스트를 문자열로 출력
print(''.join(result[:N-K_save]))