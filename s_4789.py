T = int(input())
for tc in range(1,T+1) :

    # 문제에서 문자열로 준다했으므로 str로 받아
    arr = str(input())

    # clap = 박수치는사람 수 / hire = 고용해야 할 사람 수
    clap,hire = 0,0
    # 첫 번째 사람부터 마지막 사람까지
    for i in range(1,len(arr)+1) :
        # 박수 칠 사람이 0이면 패스하므로 0이상인 경우에
        if int(arr[i-1]) > 0 :
            # i번째 사람이 박수치려면 i-1 이상이어야 함.
            if clap >= i-1 :
            # 조건 만족하면 박수 치는 사람 수 더해주기 ( index가 0부터 시작하니깐 주의 )
                clap += int(arr[i-1])
            # 조건 만족 못하면
            else :
                # (필요한 사람 수 - 박수치는 사람) 만큼 고용하고,
                # 고용한 사람들은 박수쳐줄거니깐 그만큼 늘려주고,
                # 고용하면 위에 조건을 만족하게 되니깐 박수 치는 사람 수 더해주기.
                hire += i-1-clap
                clap += i-1-clap
                clap += int(arr[i-1])
# 고용한 사람 수 출력
    print(f'#{tc} {hire}')

