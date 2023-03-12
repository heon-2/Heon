import sys
sys.stdin = open("fly.txt", "r")

T = int(input())
for tc in range(1,T+1) :
    N,M = map(int,input().split())
    fly = [list(map(int,input().split())) for _ in range(N) ]

    # 파리를 때리고 잡은 개체 수 리턴
    def attack(y,x) :
        kill_cnt = 0
        for i in range(M) :
            for j in range(M) :
                if 0 <= y+i < N and 0 <= x+j < N :
                    kill_cnt += fly[y+i][x+j]
        return kill_cnt

    # 범위 내 모든 좌표마다 파리채 휘두르고 죽인 파리 수 리스트에 넣기
    cnt_lst = []
    for i in range(N) :
        for j in range(N) :
            kill = attack(i,j)
            cnt_lst.append(kill)

    # 리스트에 있는 최댓값 프린트
    max_cnt = 0
    for i in cnt_lst :
        if i > max_cnt :
            max_cnt = i
    print(f'#{tc} {max_cnt}')