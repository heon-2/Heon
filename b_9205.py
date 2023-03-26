from collections import deque
T = int(input())
for tc in range(1,T+1) :
    lst = []
    n = int(input())
    for i in range(n+2) :
        x,y = map(int,input().split())
        lst.append((x,y))
    graph = [[] for _ in range(n+2)]
    for i in range(n+2) :
        for j in range(n+2) :
            if i != j :
                dis_x = abs(lst[i][0]-lst[j][0])
                dis_y = abs(lst[i][1]-lst[j][1])
                if dis_x + dis_y <= 1000 :
                    graph[i].append(j)
    visited = [ False for _ in range(n+2) ]

    def bfs(x,visited) :
        visited[x] = True
        q = deque()
        q.append(x)
        flag = 0

        while q :
            v = q.popleft()
            if v == n+1 :
                flag = 1
                break
            for i in graph[v] :
                if not visited[i] :
                    visited[i] = True
                    q.append(i)

        if flag == 1 :
            print('happy')
        else :
            print('sad')

    bfs(0,visited)

