"""
비밀번호 발음하기
백준
https://www.acmicpc.net/problem/4659
"""
import sys

VOWELS = ["a", "e", "i", "o", "u"]

def contains_vowel(password: str):
    for char in VOWELS:
        if char in password:
            return True
    return False

def obeys_type_streak(password: str):
    streak_length = 3
    vowels = 0
    consonants = 0

    for i in range(len(password)):
        if password[i] in VOWELS:
            vowels += 1
        else:
            consonants += 1
        
        if vowels + consonants > streak_length:
            if password[i-streak_length] in VOWELS:
                vowels -= 1
            else:
                consonants -= 1

        if vowels == streak_length or consonants == streak_length:
            return False

    return True
    
def obeys_char_streak(password: str):
    for i in range(len(password)-1):
        if password[i] == password[i+1] and password[i] not in "eo":
            return False
    return True

def solution(password: str):
    return contains_vowel(password) and obeys_type_streak(password) and obeys_char_streak(password)


if __name__ == "__main__":
    passwords = []
    while (password := sys.stdin.readline().strip()) != "end":
        isStrong = solution(password)
        print(f"<{password}> is {"acceptable" if isStrong else "not acceptable"}.")
