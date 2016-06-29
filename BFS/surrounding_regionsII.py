class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return
        
        if not board or not board[0]:
            return

        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            board[i] = list(board[i])
        
        for j in range(n):
            self.fill(board, 0, j)
            self.fill(borad, m-1, j)
            
        for i in range(m):
            self.fill(board, i, 0)
            self.fill(board, i, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] == 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'

    def fill(self, board, i, j):
        m = len(board)
        n = len(board[0])

        queue = [(i,j)]

        while queue:
            row, col = queue.pop(0)

            if row < 0 or row >= m or col < 0 or col >=n or board[row][col] != 'O':
                continue

            board[row][col] = '#'
            queue.append((row-1, col))
            queue.append((row+1, col))
            queue.append((row, col+1))
            queue.append((row, col-1))


