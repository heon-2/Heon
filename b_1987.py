R,C = map(int,input().split())
graph = [ list(input()) for _ in range(R) ]

from collections import deque

def bfs(y,x) :
    path = [graph[y][x]]
    q = deque()
    q.append((y,x))
    visited = [[False]*C for _ in range(R) ]
    visited[y][x] = True
    directy = [-1,0,0,1]
    directx = [0,-1,1,0]

    while q :
        v1,v2 = q.popleft()
        for i in range(4) :
            dy = directy[i] + v1
            dx = directx[i] + v2
            if 0<=dy<R and 0<=dx<C and graph[dy][dx] not in path and visited[dy][dx] == False   :
                visited[dy][dx] = True
                q.append((dy,dx))
                path.append(graph[dy][dx])

    print(len(path))

bfs(0,0)