class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(start_index, current_node):

            cur = current_node
            for i in range(start_index, len(word)):
                char = word[i]

                if char == ".":
                    for child in cur.children:
                        if child and dfs(i + 1, child):
                            return True
                    return False
                else:
                    index = ord(char) - ord('a')
                    if cur.children[index] is None:
                        return False
                    cur = cur.children[index]
            return cur.endOfWord
        return dfs(0, self.root)
            



