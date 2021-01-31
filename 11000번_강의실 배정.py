import sys
import heapq

# 수업 개수
N = int(sys.stdin.readline())

# 강의실 리스트
room = []
# 수업 리스트
lecture = []

# 수업 리스트에 추가
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    lecture.append([start, end])

# 수업 리스트를 시작 시각 기준 오름차순 정렬
lecture.sort(key = lambda x: x[0])

# 첫번째 수업을 강의실에 추가
heapq.heappush(room, lecture[0][1])

# 다음 수업부터 강의실의 마침시각을 기준으로 판단하여 추가
for i in range(1, N):    
    if room[0] <= lecture[i][0]:
        heapq.heappop(room)
        heapq.heappush(room, lecture[i][1])   
    else:
        heapq.heappush(room, lecture[i][1])
            
# 강의실 리스트 크기가 강의실 사용 개수
print(len(room))
