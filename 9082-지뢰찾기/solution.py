import sys

UNKNOWN = "#"
MINE = "*"

def solution(num_mines, field):
    for i, item in enumerate(field):
        if item == MINE:
            if i-1 >= 0:
                num_mines[i-1] -= 1
            if i+1 < len(num_mines):
                num_mines[i+1] -= 1
            num_mines[i] -= 1

    for i, num in enumerate(num_mines):
        for j in range(i-1, i+2):
            if num == 0:
                break

            if j < 0 or j >= len(field):
                continue
            
            if field[j] != UNKNOWN:
                continue

            available = True
            for k in range(j-1, j+2):
                if k < 0 or k >= len(field):
                    continue
                if num_mines[k] == 0:
                    available = False
                    break
            
            if available:
                field[j] = MINE
                for k in range(j-1, j+2):
                    if k < 0 or k >= len(field):
                        continue
                    num_mines[k] -= 1

    return field.count(MINE)
            

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        num_mines = [int(val) for val in sys.stdin.readline().strip()]
        field = [val for val in sys.stdin.readline().strip()]
        print(solution(num_mines, field))
