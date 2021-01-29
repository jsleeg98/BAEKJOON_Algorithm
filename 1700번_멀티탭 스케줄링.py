import sys

# 구멍 개수 N, 사용 횟수 K
N, K = map(int, sys.stdin.readline().split())

# 사용 순서 uses
uses = list(map(int, sys.stdin.readline().split()))

# 사용 중인 상태 using
using = []

# 플러그를 뽑은 횟수 count
count = 0

# 사용 순서 동안
for i in range(K):
    # 구멍이 남아 있다면
    if len(using) < N:
        # 이미 사용중인지 확인 
        check_1 = False
        for j in range(len(using)):
            # 이미 사용중인 경우
            if using[j] == uses[i]:
                check_1 = True
                break
        # 사용 중이면 다음으로 패스
        if check_1 == True:
            continue
        # 사용 중이 아니면 사용중에 추가
        else:    
            using.append(uses[i])

    # 꽉 찼을 경우
    elif len(using) == N:
        # 이미 사용중인지 확인
        check_1 = False
        for j in range(len(using)):
            if using[j] == uses[i]:
                check_1 = True
                break
        # 사용 중이면 다음으로 패스
        if check_1 == True:
            continue
        # 사용 중이 아니면 가장 나중에 사용하는 것의 코드를 뽑고 새로운 것 꽂기
        else:
            # 뽑을 코드 선택을 위한 임시 리스트
            tmp = []
            for j in range(N):
                # 우선순위 0으로 초기화
                priority = 0
                for k in range(i + 1, K):
                    if using[j] == uses[k]:
                        break
                    # 같지 않으면 우선순위 + 1
                    priority += 1
                tmp.append(priority)
            # 가장 우선순위가 낮은 것 삭제
            del using[tmp.index(max(tmp))]
            # 코드 뽑은 횟수 1 더하기
            count += 1
            # 사용 중으로 추가
            using.append(uses[i])

print(count)