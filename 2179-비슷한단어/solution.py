"""
백준
비숫한 단어
https://www.acmicpc.net/problem/2179

입력의 크기를 보고 브루트포스는 안된다고 판단을 내렸지만, 어떤 제출은
단순 브루트포스를 사용해도 통과하는 경우가 있는 모양이다.

브루트포스로 생각했을때 간단하게 모든 문자열을 다른 문자열들과 비교해서
prefix 갈아를 구한다. 문제의 좀 까다로운 조건이 prefix 길이가 같을
경우 입력순으로 빠른 조합이 답이 되어야한다. 이부분은 최대 prefix 길이와
더불어 그에 해당하는 조합의 인덱스도 보관해주면 해결 할 수 있다. 어찌됬든
인덱스는 마지막에 단어 자체를 리턴해야하기 때문에 유용하다.
이렇게 했을때 시간 복잡도는 O(n^2 * m)
- n 은 단어의 개수
- m 은 단어 하나의 최대 길이
각 단어의 쌍을 비교하고 비교할때 한자한자 비교하기 때문이다

개선된 방법도 존재하는데 먼저 내가 전혀 생각하지 못한 방법이다. 간단한데
왜 생각하지 못했을까라는 아쉬움이 남는다. 방법은 문자열을 정렬하고 붙어있는
것들끼리 비교한다. 이렇게하면 가장 길수 있는 경우만 비교하게 되고 문자들을
단순히 순회하면 된다. 참고로 정렬을 하면 문자들의 입력순서를 잃어버리기 때문에
따로 저장해두어야한다.

나는 생각을 많이 한 탓에 트리 자료구조를 사용해 풀었다. 코드도 헷갈리고 이 문제에
적용하기에는 직관적이지 않았다고 개인적으로 생각한다. 그래서 생각보다 좀 애를 먹었다.

어쨋든 이렇게 개선하면 시간복잡도는 O(n * m) 까지 개선 할 수 있다.
"""
import sys

class Trie:
    def __init__(self, val=None):
        self.val = val
        self._trie = {}

def solution(words):
    root = Trie()
    max_match_len = -1
    matched_words = []

    node = root
    for char in words[0]:
        node._trie[char] = Trie(val=char)
        node = node._trie[char]

    for word in words[1:]:
        node = root
        prefix = []

        for char in word:
            if char not in node._trie:
                break
            prefix.append(char)
            node = node._trie[char]

        if len(prefix) > max_match_len:
            max_match_len = len(prefix)
            matched_words = []
        if len(prefix) >= max_match_len:
            while node and node._trie:
                for char in node._trie:
                    node = node._trie[char]
                    prefix.append(char)
                    break
            matched_words.append(("".join(prefix), word))

        node = root
        for char in word:
            if char not in node._trie:
                node._trie[char] = Trie(val=char)
            node = node._trie[char]
    
    words_order = {word: i for i, word in enumerate(words)}
    matched_words.sort(key=lambda words: (words_order[words[0]], words_order[words[1]]))
    return matched_words[0]


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    words = [sys.stdin.readline().strip() for _ in range(n)]
    for word in solution(words):
        print(word)
