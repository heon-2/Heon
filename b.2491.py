N = int(input())
arr = list(map(int,input().split()))
rev_arr = arr[::-1]
cnt = 1
rev_cnt = 1
maxx = 1
for i in range(N-1) :
    if arr[i] <= arr[i+1] :
        cnt += 1
        if i == N-2 :
            if cnt >= maxx :
                maxx = cnt
    else :
        if cnt >= maxx :
            maxx = cnt
        cnt = 1
for i in range(N-1) :
    if rev_arr[i] <= rev_arr[i+1] :
        rev_cnt += 1
        if i == N-2 :
            if rev_cnt >= maxx :
                maxx = rev_cnt
    else :
        if rev_cnt >= maxx :
            maxx = rev_cnt
        rev_cnt = 1
print(maxx)

# 90% 에서 실패. 반례가 뭐지
# 이번엔 94 %
