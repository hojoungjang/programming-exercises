import sys

def solution(letters, length):

    def validate(code):
        vowels = 0
        consonants = 0
        for letter in code:
            if letter in "aeiou":
                vowels += 1
            else:
                consonants += 1
        
        if vowels < 1 or consonants < 2:
            return False
        return True

    def combine(idx, code):
        if len(code) == length and validate(code):
            codes.append("".join(code))
            return
        
        if idx >= len(letters):
            return
        
        code.append(letters[idx])
        combine(idx+1, code)
        code.pop()
        combine(idx+1, code)

    ################################
    letters.sort()
    codes = []
    combine(0, [])
    return codes


if __name__ == "__main__":
    L, C = map(int, sys.stdin.readline().strip().split(" "))
    letters = [char for char in sys.stdin.readline().strip().split(" ")]
    codes = solution(letters, L)
    for code in codes:
        print(code)