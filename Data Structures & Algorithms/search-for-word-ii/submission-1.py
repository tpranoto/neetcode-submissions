class Node:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        temp= self

        for c in word:
            if c not in temp.children:
                temp.children[c] = Node(c)
            temp = temp.children[c]
        temp.isWord = True


DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Node("")
        for w in words:
            trie.addWord(w)

        res = set()
        visited = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in trie.children:
                    self.dfs(board,r,c,trie,visited,"",res)

        return list(res)

    def dfs(self,board,r,c,node,visited,curWord,res):
        if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or (r,c) in visited or board[r][c] not in node.children:
            return

        visited.add((r,c))
        curWord += board[r][c]
        node = node.children[board[r][c]]
        if node.isWord:
            res.add(curWord)
            
        for dr,dc in DIRS:
            self.dfs(board,r+dr,c+dc,node,visited,curWord,res)
        
        visited.remove((r,c))
        

