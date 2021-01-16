import sys

# 결과 리스트
result = []

# 반복
while(1):
    # L, P, V 입력 받기
    # P : 연속하는 P일 중
    # L : L일 동안만 사용할 수 있다
    # V : 휴가기간은 V일
    L, P, V = map(int, sys.stdin.readline().split())
    if(L == 0 & P == 0 & V == 0):
        # 종료 명령
        break
    else:
        # 결과에 추가
        # V % P 가 L보다 큰 경우가 있기 때문에 이를 고려
        result.append((V // P) * L + min(V % P, L))

# 결과 출력    
for index, value in enumerate(result):
    print('Case %d: %d' %(index + 1, value))
