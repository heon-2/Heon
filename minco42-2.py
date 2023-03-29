
# 순서 상관있고 중복 없어야 함.  => 순열로 접근하기
# 5개를 5개. 경우의 수

number = list(map(int,input().split()))
used = [False] *5
path = []
calcul_lst = []
def dfs(level) :

    if level == 5 :
        calcul = (path[0]*path[1]) - (path[2]*path[3]) + path[4]
        calcul_lst.append(calcul)

    for i in range(5) :
        if not used[i] :
            used[i] = True
            path.append(number[i])
            dfs(level+1)
            path.pop()
            used[i] = False

dfs(0)

print(max(calcul_lst))
print(min(calcul_lst))

# 의문. 백트래킹을 어찌해?