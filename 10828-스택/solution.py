import sys

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, val):
        self._stack.append(val)

    def pop(self):
        if not self._stack:
            return -1
        return self._stack.pop()
    
    def size(self):
        return len(self._stack)
    
    def empty(self):
        return 0 if self._stack else 1
    
    def top(self):
        if not self._stack:
            return -1
        return self._stack[-1]

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    stack = Stack()
    for _ in range(n):
        command = sys.stdin.readline().strip().split(" ")
        if command[0] == "push":
            stack.push(int(command[1]))
        elif command[0] == "pop":
            print(stack.pop())
        elif command[0] == "size":
            print(stack.size())
        elif command[0] == "empty":
            print(stack.empty())
        elif command[0] == "top":
            print(stack.top())
