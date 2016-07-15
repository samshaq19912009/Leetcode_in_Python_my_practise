class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def check(x,y):
            tmp = board[x][y]
            board[x][y] = 'D'
            for i in range(9):
                if board[i][y] == tmp:
                    return False
            for j in range(9):
                if board[x][j] == tmp:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j] == tmp:
                        return False
            
            board[x][y] = tmp
            return True
        
        def dfs(board):
            for x in range(9):
                for y in range(9):
                    #find a spot to fill
                    if board[x][y] == '.':
                        for k in '123456789':
                            board[x][y] = k
                            if check(x,y) and dfs(board):
                                return True
                            board[x][y] = '.'
                        #this test failure
                        return False
            #this is important!!!!!!
            return True
        dfs(board)
    
       
            
