# 청소해야 할 방 크기
N,M = map(int,input().split())
# 로봇 좌표랑 로봇 방향 입력받기
r,c,d = map(int,input().split())
# 방 입력받기
room = [list(map(int,input().split())) for _ in range(N) ]
# 다이렉트 배열 설정 => 0 : 북쪽 / 1 : 동쪽 / 2 : 남쪽 / 3 : 서쪽
directy = [-1,0,1,0]
directx = [0,1,0,-1]

# 방 청소 횟수
clean_cnt = 0

# d를 - 하면서 풀어나갈 생각이라 4를 더해줌. ( 뒤에서 4로 나눗셈해야해서 음수면 안되기 때문에! )
d += 4

# 청소하는 함수
def clean(y,x) :
    # 로봇의 회전횟수
    turn_cnt = 0
    global clean_cnt,d

    # 0이면 청소안된 곳이니깐 청소하고 청소횟수 +1
    # 오늘은 7이 좋아서 7로 칠해줘
    if room[y][x] == 0 :
        room[y][x] = 7
        clean_cnt += 1

    # 로봇 회전시키기
    while True :
        # 로봇이 4번 돌았으면 ( = 4방향이 모두 청소됐다면) 후진 시켜줘.
        if turn_cnt == 4 :
            # 후진
            d -=2
            # 후진해야 하는 곳이 1이면 청소 횟수 출력하고 브레이크
            v = d % 4
            dy = y+directy[v]
            dx = x+directx[v]
            if room[dy][dx] == 1 :
                print(clean_cnt)
                break
            # 후진해야 하는 곳이 1이 아니면, 벽이 아니니깐 후진하기
            else :
                # 후진하고도 방향은 유지해야하니깐 다시 원상복귀
                d +=2
                clean(dy,dx)
                break

        # 90도 반시계방향 회전
        d -= 1
        move = d % 4
        dy = y + directy[move]
        dx = x + directx[move]

        # 회전한 곳이 0이면 이동하기
        if room[dy][dx] == 0 :
            clean(dy,dx)
            return
        # 만약 회전한 곳이 0이 아니면 회전 횟수 +1
        turn_cnt += 1

clean(r,c)