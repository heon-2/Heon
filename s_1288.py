T = int(input())
for tc in range(1,T+1) :
    # 숫자 입력받기
    num = int(input())
    # 양 세는 횟수
    cnt = 0
    # 0~10까지 나오면 정답이니깐 비교대상
    answer = [ str(i) for i in range(10) ]
    # 지금까지 본 숫자 저장하는 리스트
    num_lst = []

    while True :
        cnt += 1
        # 현재 보고 있는 양 = 주어진 숫자 * 양 세는 횟수
        now = num * cnt
        for i in str(now) :
            if i not in num_lst :
                num_lst.append(i)
        # 비교를 위해 오름차순 정렬
        num_lst.sort()
        # 지금까지 본 숫자와 정답과 같으면
        # 현재 보고 있는 양의 번호 출력
        if answer == num_lst :
            print(f'#{tc} {now}')
            break
