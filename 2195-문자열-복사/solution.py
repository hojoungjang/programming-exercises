import sys

def solution(source, target):
    i = 0
    cnt = 0

    while i < len(target):
        
        max_length = 0
        j = 0
        
        while j < len(source):
            if target[i] != source[j]:
                j += 1
                continue

            length = 0
            temp_i = i
            temp_j = j
            
            while temp_i < len(target) and temp_j < len(source) and target[temp_i] == source[temp_j]:
                length += 1
                temp_j += 1
                temp_i += 1
            
            if length > max_length:
                max_length = length
            j += length

        i += max_length
        cnt += 1

    return cnt


if __name__ == "__main__":
    source = sys.stdin.readline().strip()
    target = sys.stdin.readline().strip()
    print(solution(source, target))
