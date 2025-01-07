DIRECTION_OFFSETS = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
OPEN = "O"
CLOSED = "X"
START = "S"

def solution(park, routes):
    def get_start_point():
        for i in range(len(park)):
            for j in range(len(park[0])):
                if park[i][j] == START:
                    return i, j
        return -1, -1
    
    def closed_path(row, new_row, col, new_col):
        lo_r, hi_r = min(row, new_row), max(row, new_row)
        lo_c, hi_c = min(col, new_col), max(col,new_col)
        for row_idx in range(lo_r, hi_r+1):
            for col_idx in range(lo_c, hi_c+1):
                if park[row_idx][col_idx] == CLOSED:
                    return True
        return False
    
        
    park_height = len(park)
    park_width = len(park[0])
    
    # starting point
    r, c = get_start_point()
    if r == -1 and c == -1:
        raise Exception("No start point found")
    
    for route in routes:
        direction, magnitude = route.split(" ")
        row_offset, col_offset = DIRECTION_OFFSETS.get(direction, (0,0))
        new_r = r + row_offset * int(magnitude)
        new_c = c + col_offset * int(magnitude)
        
        # Out of bound
        if new_r < 0 or new_r >= park_height:
            continue
        if new_c < 0 or new_c >= park_width:
            continue
            
        # obstacle check
        if closed_path(r, new_r, c, new_c):
            continue
            
        r, c = new_r, new_c
    
    return [r, c]


if __name__ == "__main__":
    print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))
