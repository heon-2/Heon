# 7개 중 3개를 뽑아. => 조합 / 중복x

N,pick = map(int,input().split())
card = list(map(int,input().split()))
minn = 21e8
path = []
used = [False]*N

ans = [0]*pick
def comb(level,start) :
    global minn,gop,ans
    if level == pick :
        gop = 1
        for i in path :
            gop *= i
        if gop < minn :
            minn = gop
            for i in range(len(path)) :
                ans[i] = path[i]
        return

    for i in range(start,N) :
        if not used[i] :
            used[i] = True
            path.append(card[i])
            comb(level+1,start+1)
            path.pop()
            used[i] = False

comb(0,0)

ans.sort()
print(*ans)

