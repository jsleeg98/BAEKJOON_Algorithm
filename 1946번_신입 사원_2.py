import sys

case = []

T = int(sys.stdin.readline())
for i in range(T):
    case.append([])
    N = int(sys.stdin.readline())
    for j in range(N):
        case[i].append(list(map(int, sys.stdin.readline().split())))
    case[i].sort() # 오름차순 정렬



for i in range(T):
    count = 0
    min_value = case[i][0][1] # 맨 앞 값을 가장 작은 값으로 초기화
    for k in range(len(case[i])):
        check = True # 선발 가능 여부 초기화
        if case[i][k][1] > min_value:
            check = False # 선발 불가 
        else:
           min_value = case[i][flag][1] # 가장 작은 값 갱신
        if check == True: # 선발 가능
            count += 1
    print(count)

