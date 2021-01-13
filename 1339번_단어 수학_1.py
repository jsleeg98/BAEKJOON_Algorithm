import sys

# 단어 개수 입력
N = int(sys.stdin.readline())

# 입력 단어 저장 리스트 생성
words = []

# 단어 리스트에 저장
for i in range(N):
    words.append(sys.stdin.readline())

# 숫자 배열 초기화
numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 알파벳 숫자 매칭 딕셔너리 생성
match = {}

# 결과 0 초기화
result = 0

# 단어 개수 만큼 반복
for i in range(N):
    # 단어 구성 알파벳 만큼 반복
    for j in range(len(words[i]) - 1):
        # 알파벳 숫자 매칭에 알파벳 키가 있는 경우
        if words[i][j] in match:
            match[words[i][j]] += 10**((len(words[i]) - 1) - 1 - j)
        # 알파벳 숫자 매칭에 알파벳 키가 없는 경우 
        else:  
            match[words[i][j]] = 10**((len(words[i]) - 1) - 1 - j)

# 매칭 딕셔너리를 값에 따라 정렬
match_sort = sorted(match.items(), reverse=True, key = lambda item : item[1])


# 값 매칭
for i in range(len(match)):
    match[match_sort[i][0]] = numbers[i]

# 합계 계산
for i in range(N):
    for j in range(len(words[i]) - 1):
        result += match[words[i][j]] * (10 ** ((len(words[i]) - 1) - 1 - j))

print(result)