import sys
input = sys.stdin.readline

n = int(input())
group_word = 0

for _ in range(n):
    word = input().rstrip()
    checking = 0
    for i in range(len(word)-1):
        if word[i] != word[i + 1]:
            new_word = word[i + 1:]  # 남은 부분 새로운 단어
            if new_word.count(word[i]) > 0:  # 지금 단어 들어잇으면 에러
                checking += 1
    if checking == 0:
        group_word += 1

print(group_word)
