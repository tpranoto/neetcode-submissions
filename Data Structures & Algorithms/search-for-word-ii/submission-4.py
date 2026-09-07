class Node:
    def __init__(self,char):
        self.val = char
        self.children = {}
        self.isWord = False
    
    def add(self, word):
        temp = self
        for w in word:
            if w not in temp.children:
                temp.children[w] = Node(w)
            temp = temp.children[w]
        temp.isWord = True

class Solution:
    def __init__(self):
        self.dirs = [(1,0),(0,1),(-1,0),(0,-1)]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Node("0")
        for w in words:
            trie.add(w)

        res = set()
        visited= set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in trie.children:
                    self.dfs(board,r,c,"",trie,visited,res)

        return list(res)
                
    def dfs(self, board,r,c,curWord,trie,visited,result):
        if not (0<=r<len(board)) or not (0<=c<len(board[0])) or (r,c) in visited or board[r][c] not in trie.children:
            return
        
        visited.add((r,c))
        curWord+=board[r][c]
        trie = trie.children[board[r][c]]

        if trie.isWord:
            result.add(curWord)
        
        for dr,dc in self.dirs:
            self.dfs(board,dr+r,dc+c,curWord,trie,visited,result)
        
        visited.remove((r,c))



        
