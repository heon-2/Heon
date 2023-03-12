N = int(input())
# 맥스값과 맥스값에 해당하는 인덱스
mx_i = mx = 0

# DAT를 이용해서 오름차순 정렬
lst = [0]*1001
for _ in range(N) :
    L,H = map(int,input().split())
    # L위치에 H기록
    lst[L] = H

    # 최댓값과 인덱스 계속 갱신해주기.
    if mx < H :
        mx_i, mx = L , H

# 맥스값을 기준으로 왼쪽 구간
ans = 0
mx = 0
for i in range(mx_i+1) :
    mx = max(mx,lst[i])
    ans += mx

# 맥스값을 기준으로 오른쪽 구간
mx = 0
for i in range(1000,mx_i,-1) :
    mx = max(mx,lst[i])
    ans += mx
print(ans)


