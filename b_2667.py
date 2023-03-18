N = int(input())

cnt = 0
cnt_lst = []
graph = []
visited = [ [False]*N for _ in range(N) ]
for i in range(N) :
    graph.append(list(map(int,input())))

def dfs(x,y,cnt) :
    if x < 0 or x >= N or y < 0 or y >= N :
        return False

    if graph[x][y] == 1 and not visited[x][y] :
        visited[x][y] = True
        graph[x][y] = 0
        dfs(x+1,y,cnt+1)
        dfs(x-1,y,cnt+1)
        dfs(y+1,x,cnt+1)
        dfs(y-1,x,cnt+1)
        cnt_lst.append(cnt)
        return True
    else :
        return False

for i in range(N) :
    for j in range(N) :
        dfs(i,j,0)

print(cnt_lst)