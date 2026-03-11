from collections import deque

def solution(maps):
    n = len(maps) # 열의 길이
    m = len(maps[0]) # 행의 길이
    
    # 상, 하, 좌, 우 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque([(0, 0)])
    
    # 시작점 방문 처리는 따로 안 해도 됨 (거리를 1로 시작하므로)
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                
    answer = maps[n-1][m-1]
    
    return answer if answer > 1 else -1