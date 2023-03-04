T = int(input())
for tc in range(1,T+1) :
    N,M = map(int,input().split())

    # 페인트 칠해야 할 국기 받기
    russia = [list(input()) for _ in range(N) ]

    # 페인트 칠하는 횟수 구하기
    def paint(W,B,R) :
        # 페인트 칠한 횟수
        cnt = 0
        # 국기 모두 탐색 ( 흰,파,빨 영역 구분해서 )
        for i in range(N) :
            for j in range(M) :
                # 흰색으로 칠할 범위만큼에서, 흰색이 아니면 칠해야 하니깐 카운트 +1
                if 0 <= i < W :
                    if russia[i][j] != 'W' :
                        cnt += 1
                # 파란색으로 칠할 범위에서 파란색 아니면 +1
                elif W <= i < W+B :
                    if russia[i][j] != 'B' :
                        cnt += 1
                # 빨강색으로 칠할 범위에서 빨강 아니면 +1
                elif W+B <= i < W+B+R :
                    if russia[i][j] != 'R' :
                        cnt += 1
        return cnt

    # 페인트 칠할 수 있는 경우의 수 구하기
    # 조합 쓸 줄 몰라서 3중 포문으로 구함.
    lst = []
    # 흰색,파랑,빨강색 각각이 1보다 크고 합해서 N이 되는 경우의 수 구하기
    # 중복을 피해야 하므로 리스트 안에 없으면 넣기.
    for W in range(1,N-1) :
        for B in range(1,N-1) :
            for R in range(1,N-1) :
                if W+B+R == N and [W,B,R] not in lst :
                    lst.append([W,B,R])

    # 구한 경우의 수 중에서 최솟값 구하기
    minn = 21e8
    # 경우의 수(W,B,R)이 담겨있는 리스트의 각 W,B,R을 함수에 넣어
    for i in lst :
        cnt = paint(i[0],i[1],i[2])
        # 함수에 넣어서 리턴 받은 cnt 값이 최솟값보다 작으면 최솟값 갱신!
        if minn > cnt :
            minn = cnt
    # 최솟값 출력
    print(f'#{tc} {minn}')