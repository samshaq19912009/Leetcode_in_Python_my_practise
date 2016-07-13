class Solution:
    def valid_sudoku(self, board):
        n = len(board)
        for x in range(n):
            for y in range(n):
                if not board[x][y] == '.' or not self.check(board,x,y):
                    return False
        return True

    def check(self, board, x, y):
        tmp = board[x][y]
        board[x][y] = 'D'
        n = len(board)
        for i in range(n):
            if board[i][y] == tmp:
                return False
        for j in range(n):
            if board[x][j] == tmp:
                return False
        for i in range(3):
            for j in range(3):
                if board[(x/3)*3+i][(y/3)*3+j] == tmp:
                    return False
        board[x][y] = tmp
        return True

