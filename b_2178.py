# 백준 2178번 미로탐색

# deque 모듈 부르고 N*M 그래프 입력받기
from collections import deque
N,M = map(int,input().split())
graph = [ list(map(int,input())) for _ in range(N) ]

# bfs 함수 만들기
def bfs(y,x) :
    # 4방향
    directy = [-1,0,0,1]
    directx = [0,-1,1,0]
    # 큐 만들고 입력 받은 0,0 추가하기
    q = deque()
    q.append((y,x))

    # 큐 만들어주고
    while q :
        v1,v2 = q.popleft()
        for i in range(4) :
    # 4방향에 대해서 1) 범위를 벗어나지 않고, 2) 그래프가 1이면
            dy = v1 + directy[i]
            dx = v2 + directx[i]
            if 0 <= dy < N and 0 <= dx < M and graph[dy][dx] == 1 :
                # 이전 값에 비해 +1 을 입력해줌
                graph[dy][dx] = graph[v1][v2]+1
                # 그리고 큐에 담기
                q.append((dy,dx))
    # 그래프의 N,M ( 오른쪽 아래 마지막 ) 에 입력된 숫자 리턴해주기.
    # 시작점과 끝점의 최소거리임.
    return graph[N-1][M-1]
print(bfs(0,0))