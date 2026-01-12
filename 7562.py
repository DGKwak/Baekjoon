from collections import deque
import sys

n = int(sys.stdin.readline())

def bfs(x, y, chess_board):
    q = deque([(y, x)])
    chess_board[y][x] = 1
    
    knight = [[1, 2], [2, 1], [1, -2], [2, -1], [-1, 2], [-2, 1], [-1, -2], [-2, -1]]
    
    while q:
        curr_y, curr_x = q.popleft()
        
        for move in knight:
            ny = curr_y + move[0]
            nx = curr_x + move[1]
            
            if 0 <= ny < m and 0 <= nx < m:
                if chess_board[ny][nx] == 0:
                    chess_board[ny][nx] = chess_board[curr_y][curr_x] + 1
                    q.append((ny, nx))

    return chess_board

for _ in range(n):
    m = int(sys.stdin.readline())
    
    chess_board = [[0 for _ in range(m)] for _ in range(m)]
    
    start_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())
    
    result = bfs(start_x, start_y, chess_board)
    print(result[end_y][end_x] - 1)