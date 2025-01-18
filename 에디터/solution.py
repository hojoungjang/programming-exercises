"""
백준
에디터
https://www.acmicpc.net/problem/1406

처음에는 간단해 보이지만 좀 더 들여다보면 문자 끝 부분을 제외한
글자 추가 또는 삭제시 효율적으로 데이터를 변경 할 수 있어야
한다.

단순하게 리스트를 (또는 배열) 사용해 접근 할 경우 추가/삭제는 
매번 새롭게 단어 전체를 복사하게 된다.

리스트식의 데이터 컬렉션에서 아무 위치에서 빠르게 데이터 삭제/추가 
해야 할 경우 링크드리스트가 있다. 추가로 우리는 앞뒤로 커서를 움직이기
떄문에 더블리링크드리스트가 적합하다.
"""
import sys

class DoublyLinkedList:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

def solution(text, commands):
    head = ptr = DoublyLinkedList()
    for char in text:
        node = DoublyLinkedList(char)
        ptr.next = node
        node.prev = ptr
        ptr = node

    for command in commands:
        command_args = command.split(" ")
        if command_args[0] == "L":
            if ptr.prev:
                ptr = ptr.prev
        elif command_args[0] == "D":
            if ptr.next:
                ptr = ptr.next
        elif command_args[0] == "B":
            if ptr.prev:
                ptr.prev.next = ptr.next
                if ptr.next:
                    ptr.next.prev = ptr.prev
                ptr = ptr.prev
        elif command_args[0] == "P":
            node = DoublyLinkedList(command_args[1])
            node.next = ptr.next
            node.prev = ptr
            ptr.next = node
            if node.next:
                node.next.prev = node
            ptr = node

    new_text = []
    ptr = head.next
    while ptr:
        new_text.append(ptr.val) 
        ptr = ptr.next
    return "".join(new_text) 

if __name__ == "__main__":
    text = [char for char in sys.stdin.readline().strip()]
    n = int(sys.stdin.readline().strip())
    commands = [sys.stdin.readline().strip() for _ in range(n)]
    print(solution(text, commands))
