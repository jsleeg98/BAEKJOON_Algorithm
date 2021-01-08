import sys

# 회의 수 입력
N = int(sys.stdin.readline())

end = 0
count = 0

# 회의 시간 리스트
li = []
# 회의 시간 입력
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    li.append((a, b))

# 회의 시간 정렬
# 1. 회의가 끝나는 시간 오름차순 2. 회의가 시작하는 시간 오름차순
li.sort(key = lambda x : (x[1], x[0]))

for i in li:
    if end <= i[0]:
        end = i[1]
        count += 1

print(count)

#%%
li = []
li.append((1,3))
li
