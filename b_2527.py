for _ in range(4) :
    sj1,si1,ej1,ei1,sj2,si2,ej2,ei2 = map(int,input().split())

    # 바깥쪽에 있는 경우
    if si1 > ei2 or ei1 < si2 or sj1 > ej2 or ej1 < sj2 :
        ans = 'd'
    elif ej1 == sj2 or sj1 == ej2 : # 세로가 일치 (붙어있는 경우)
        if ei1 == si2 or si1 == ei2 : # 가로가 일치 (붙어있는 경우)
            ans = 'c' # 가로 세로 다 붙어있으면 점.
        else :
            ans = 'b' #세로만 붙어있다. 그러면 변 (하나만 붙어있음)
    elif ei1 == si2 or si1 == ei2 : # 세로 일치하지 않고 가로만 일치하면 변
        ans = 'b'

    else :  # 나머지는 a
        ans ='a'
    print(ans)