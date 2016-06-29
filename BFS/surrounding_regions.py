class Solution:
    # @params, 2D array
    # capture all regions by modifying the input borad in-place
    # do not return any thing

    def solve(self, board):
        if not board:
            return
        m, n = len(board), len(board[0])
        
        vis = [[False for j in range(n)] for i in range(m)]
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        
        for i in range(m):
            for j in range(n):
                if borad[i][j] == 'X' or vis[i][j]:
                    continue
                q, q2 = [], []
                flag = True
                q.append((i,j))
                q2.append((i,j))
                while q:
                    curx, cury = q.pop(0)
                    for k in range(4):
                        nx, ny = curx+dx[k], cury+dy[k]
                        #if reach the borader
                        if nx < 0 or ny < 0 or nx >= m or ny >= n:
                            flag = False
                            continue
                        if vis[nx][ny] or borad[nx][ny] == 'X':
                            continue
                        vis[nx][ny] = True
                        q.append((nx, ny))
                        q2.append((nx, ny))
                
                if flag:
                    for x, y in q2:
                        borad[x][y] = 'X'



                        
