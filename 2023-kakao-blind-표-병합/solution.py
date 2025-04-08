"""
프로그래머스
표 병합
https://school.programmers.co.kr/learn/courses/30/lessons/150366
"""

TABLE_SIZE = 50
EMPTY = "EMPTY"

class Table:
    def __init__(self):
        self._table = [["" for _ in range(TABLE_SIZE)] for _ in range(TABLE_SIZE)]
        self._merge_ptrs = {(r, c): (r, c) for c in range(TABLE_SIZE) for r in range(TABLE_SIZE)}

    def get_merge_parent(self, r, c):
        parent = self._merge_ptrs.get((r, c))
        if parent == (r, c):
            return parent
        self._merge_ptrs[(r,c)] = self.get_merge_parent(*parent)
        return self._merge_ptrs[(r,c)]
    
    def get_value(self, r, c):
        parent_r, parent_c = self.get_merge_parent(r, c)
        return self._table[parent_r][parent_c]

    def update(self, r, c, value):
        self._table[r][c] = ""
        parent_r, parent_c = self.get_merge_parent(r, c)
        self._table[parent_r][parent_c] = value

    def update_value(self, old_val, new_val):
        for r in range(TABLE_SIZE):
            for c in range(TABLE_SIZE):
                if self.get_value(r, c) == old_val:
                    self.update(r, c, new_val)

    def merge(self, r1, c1, r2, c2):
        parent1 = self.get_merge_parent(r1, c1)
        parent2 = self.get_merge_parent(r2, c2)

        if parent1 == parent2:
            return

        pr1, pc1 = parent1
        pr2, pc2 = parent2

        if not self._table[pr1][pc1] and self._table[pr2][pc2]:
            self._merge_ptrs[parent1] = parent2
            self._table[pr1][pc1] = ""
        else:
            self._merge_ptrs[parent2] = parent1
            self._table[pr2][pc2] = ""

    def unmerge(self, r, c):
        parent_r, parent_c = self.get_merge_parent(r, c)
        value = self._table[parent_r][parent_c]
        cells = []

        for ir in range(TABLE_SIZE):
            for ic in range(TABLE_SIZE):
                if self.get_merge_parent(ir, ic) == (parent_r, parent_c):
                    cells.append((ir, ic))

        for ir, ic in cells:
            self._merge_ptrs[(ir, ic)] = (ir, ic)
            self._table[ir][ic] = ""

        self._table[r][c] = value

    def print(self, r, c):
        val = self.get_value(r, c)
        return val if val else EMPTY


def solution(commands):
    table = Table()
    answer = []

    for command in commands:
        args = command.split(" ")

        if args[0] == "UPDATE" and len(args) == 4:
            r, c, value = args[1:]
            table.update(int(r)-1, int(c)-1, value)

        elif args[0] == "UPDATE" and len(args) == 3:
            old_val, new_val = args[1:]
            table.update_value(old_val, new_val)

        elif args[0] == "MERGE":
            r1, c1, r2, c2 = map(int, args[1:])
            table.merge(r1-1, c1-1, r2-1, c2-1)

        elif args[0] == "UNMERGE":
            r, c = map(int, args[1:])
            table.unmerge(r-1, c-1)

        elif args[0] == "PRINT":
            r, c = map(int, args[1:])
            answer.append(table.print(r-1, c-1))

    return answer

if __name__ == "__main__":
    commands = ["MERGE 1 1 2 2", "MERGE 1 1 3 3", "UPDATE 3 3 A", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3"]
    print(solution(commands))