def dfs(n,tlst) :
    if n ==M :
        ans.append(tlst)
        return

    prev = 0
    for j in range(N) :
        if v[j] == 0 and prev != lst[j] :
            prev = lst[j]
            v[j] = 1
            dfs(n+1,tlst+[lst[j]])
            v[j] = 0

N,M = map(int,input().split())
lst = sorted(list(map(int,input().split())))

ans  = []
v = [0] * N
dfs(0,[])


# 딕셔너리나 셋을 활용해 중복을 제거하는 방법도 있으나, 그것들은 다 만들어놓고 제거하는 방법이라
# 사전에 제거하는 것이 효율적인 방법임
