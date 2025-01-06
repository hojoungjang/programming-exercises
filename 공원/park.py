"""
프로그래머스
공원
https://school.programmers.co.kr/learn/courses/30/lessons/340198
"""

from bisect import bisect_right

def solution(mats, park):
    if not park:
        return -1
    
    park_rows = len(park)
    park_cols = len(park[0])
    
    def check_empty_square(start_row, start_col, n):
        """
        Checks if square with start position at (row, col) 
        and side length of n is empty based on the assumption
        that given start position with n-1 length is already
        a square
        """
        if n == 0:
            return False
        
        if start_row + n > park_rows or start_col + n > park_cols:
            return False

        for row_offset in range(n-1):
            row = start_row + row_offset
            col = start_col + n - 1
            if park[row][col] != "-1":
                return False
            
        last_row = start_row + n - 1
        for col in range(start_col, start_col + n):
            if park[last_row][col] != "-1":
                return False
        
        return True

    max_size = -1
    
    for row in range(park_rows):
        for col in range(park_cols):
            size = 0
            while check_empty_square(row, col, size+1) is True:
                size += 1
            max_size = max(max_size, size)
                
    mats.sort()
    idx = bisect_right(mats, max_size)
    return mats[idx-1] if idx != 0 else -1



if __name__ == "__main__":
    print(solution([5, 3, 2], [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]))
