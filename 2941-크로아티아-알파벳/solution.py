import sys

def solution(word):
    i = 0
    cnt = 0
    while i < len(word):
        if word[i:i+2] == "c=":
            i += 2
        elif word[i:i+2] == "c-":
            i += 2
        elif word[i:i+3] == "dz=":
            i += 3
        elif word[i:i+2] == "d-":
            i += 2
        elif word[i:i+2] == "lj":
            i += 2
        elif word[i:i+2] == "nj":
            i += 2
        elif word[i:i+2] == "s=":
            i += 2
        elif word[i:i+2] == "z=":
            i += 2
        else:
            i += 1
        cnt += 1
    return cnt


if __name__ == "__main__":
    word = sys.stdin.readline().strip()
    print(solution(word))