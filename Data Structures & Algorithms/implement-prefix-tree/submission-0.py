class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.trie = TrieNode()
    
    def insert(self, word):
        curr = self.trie

        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        
        curr.endOfWord = True

    def search(self, word):
        curr = self.trie

        for s in word:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        
        return curr.endOfWord

    def startsWith(self, prefix):
        curr = self.trie

        for s in prefix:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return True
