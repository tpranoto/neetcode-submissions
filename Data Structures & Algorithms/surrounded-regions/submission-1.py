
DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        stack = []

        for r in range(len(board)):
            if board[r][0] == "O":
                stack.append((r,0))
            if board[r][len(board[0])-1] == "O":
                stack.append((r,len(board[0])-1))
        
        for c in range(len(board[0])):
            if board[0][c] == "O":
                stack.append((0,c))
            if board[len(board)-1][c] == "O":
                stack.append((len(board)-1,c))

        self.dfs(board,stack)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "CC":
                    board[r][c] = "O"

    
    def dfs(self,board,stack):
        while stack:
            row,col = stack.pop()
            board[row][col] = "CC"

            for dr,dc in DIRS:
                totr = row+dr
                totc = col+dc

                if 0<=totr<len(board) and 0<=totc<len(board[0]) and board[totr][totc] == "O":
                    stack.append((totr,totc))
            
    

