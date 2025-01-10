import sys

class MySet:
    MAX_NUM = 20

    def __init__(self):
        """
        number range is between 1 and 20 [1,20]
        """
        self._set = [0 for _ in range(self.MAX_NUM + 1)]

    def add(self, x: int):
        self._set[x] = 1

    def remove(self, x: int):
        self._set[x] = 0

    def check(self, x: int):
        return self._set[x]

    def toggle(self, x: int):
        self._set[x] = 0 if self._set[x] == 1 else 1

    def all(self):
        for x in range(1, self.MAX_NUM+1):
            self._set[x] = 1

    def empty(self):
        for x in range(1, self.MAX_NUM+1):
            self._set[x] = 0

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    my_set = MySet()
    for _ in range(n):
        command = sys.stdin.readline().strip().split(" ")

        if len(command) == 1:
            op = command[0]
        else:
            op, x = command
            x = int(x)

        if op == "add":
            my_set.add(x)
        elif op == "remove":
            my_set.remove(x)
        elif op == "check":
            print(my_set.check(x))
        elif op == "toggle":
            my_set.toggle(x)
        elif op == "all":
            my_set.all()
        elif op == "empty":
            my_set.empty()
