class Node:

    def __init__(self, key):
        self.key = key
        self.children_length = {}
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, insert_str):

        current_node = self.head

        child_length = len(insert_str)
        if child_length in current_node.children_length:
            current_node.children_length[child_length] += 1
        else:
            current_node.children_length[child_length] = 1

        for str in insert_str:
            if str not in current_node.children:
                current_node.children[str] = Node(str)

            child_length -= 1
            current_node = current_node.children[str]

            if child_length in current_node.children_length:
                current_node.children_length[child_length] += 1
            else:
                current_node.children_length[child_length] = 1

    def search(self, str_without_q, q_mark):
        current_node = self.head
        for str in str_without_q:
            if str in current_node.children:
                current_node = current_node.children[str]
            else:
                return 0

        if q_mark in current_node.children_length:
            return current_node.children_length[q_mark]
        else:
            return 0


def solution(words, queries):
    answer = []
    trie = Trie()
    reverse_trie = Trie()
    for word in words:
        trie.insert(word)
        reverse_trie.insert(word[-1::-1])

    for query in queries:
        if query[0] == "?":
            query = query[-1::-1]
            q_mark_index = query.find("?")
            str_without_q = query[:q_mark_index]
            q_mark = len(query) - len(str_without_q)
            answer.append(reverse_trie.search(str_without_q, q_mark))
        else:
            q_mark_index = query.find("?")
            str_without_q = query[:q_mark_index]
            q_mark = len(query) - len(str_without_q)
            answer.append(trie.search(str_without_q,q_mark))
    # print(answer)
    return answer


# solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])



