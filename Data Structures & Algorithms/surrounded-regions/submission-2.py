class Solution:
    def __init__(self):
        self.dirs=[(1,0),(0,1),(-1,0),(0,-1)]
        self.cantchange="CC"


    def solve(self, board: List[List[str]]) -> None:
        stack = []
        for r in range (len(board)):
            if board[r][0] == "O":
                stack.append((r,0))
            
            if board[r][len(board[0])-1] == "O":
                stack.append((r,len(board[0])-1))
            
        for c in range(len(board[0])):
            if board[0][c] == "O":
                stack.append((0,c))
            
            if board[len(board)-1][c] == "O":
                stack.append((len(board)-1,c))

        self.calc_surrounded(board,stack)
        
    def calc_surrounded(self, board, stack):
        while stack:
            r,c=stack.pop()
            board[r][c] = self.cantchange

            for dr,dc in self.dirs:
                totr=r+dr
                totc=c+dc

                if 0<=totr<len(board) and 0<=totc<len(board[0]) and board[totr][totc] == "O":
                    stack.append((totr,totc))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] ="X"
                
                elif board[r][c] == self.cantchange:
                    board[r][c] = "O"
