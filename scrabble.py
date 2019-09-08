import sys
import math

# 파이썬에선 해시맵을 딕셔너리라고 부릅니다.
# 해시맵생성 방법 변수이름 = {key1 : value1, key2 : value2, key3 : value3}

n = int(input())
dictionary = []
for i in range(n):
    word = input()
    dictionary.append(word)
letters = input()
max_score = 0
max_score_word = ""

def is_word_fessible(word, letters):
    for char in word:
        # 단어에 쓰인 각 글자의 개수가 알파벳 꾸러미의 글자 개수보다 많은 경우
        # 단어를 조합할 수 없습니다.
        if word.count(char) > letters.count(char):
            return False
    return True

def get_char_score(char):
    score = 0
    letters_scores = {'a': 1, 'b' : 3, 'c' : 3, 'd' : 2, 'e' : 1,
                      'f' : 4, 'g' : 2, 'h' : 4, 'i' : 1, 'j' : 8,
                      'k' : 5, 'l' : 1, 'm' : 3, 'n' : 1, 'o' : 1,
                      'p' : 3, 'q' : 10, 'r' : 1, 's' : 1, 't' : 1,
                      'u' : 1, 'v' : 4, 'w' : 4, 'x' : 8, 'y' : 4, 'z' : 10}
    return letters_scores[char]

def get_word_score(word):
    score = 0
    for char in word:
        score += get_char_score(char)
    return score

for word in dictionary:
    if is_word_fessible(word, letters):
        score = get_word_score(word)
        if score > max_score:
            max_score = score
            max_score_word = word
print(max_score_word)

