class Trie:

    def __init__(self):
        self.dic = {}

    def insert(self, word: str) -> None:
        start = self.dic
        for w in word:
            if w not in start:  # has value
                start[w] = {}
                start = start[w]
            else:
                start = start[w]
        start[0] = 0  # word is end

    def search(self, word: str) -> bool:
        start = self.dic
        for w in word:
            if w not in start:
                return False
            else:
                start = start[w]
        if 0 in start:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        start = self.dic
        for w in prefix:
            if w not in start:
                return False
            else:
                start = start[w]
        return True