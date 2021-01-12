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
    flag = 0
    for k in range(len(case[i])):
        check = True
        for j in range(0, flag):
            if case[i][j][1] < case[i][flag][1]:
                check = False
                break
        flag += 1
        if check == True:
            count += 1
    print(count)


