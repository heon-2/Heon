# 이코테 Ch04.구현 2번 - 왕실의 나이트

# 8x8 체스판 생성
arr = [ [0]*8 for _ in range(8)]

def knight(y,x) :
    cnt = 0
    # 나이트가 이동할 수 있는 8가지 경우의 수
    directy = [-1,-2,-2,-1,1,2,2,1]
    directx = [-2,-1,1,2,2,1,-1,-2]

    for i in range(8) :
        dy = y + directy[i]
        dx = x + directx[i]
    # 범위안에 있으면 움직일 수 있으므로 cnt += 1
        if 0 <= dy < 8 and 0 <= dx < 8 :
            cnt += 1
    return cnt

# 좌표 입력받기 ( '소문자 알파벳' + '한 자리 숫자' )
coordinate = input()
# 소문자 알파벳 숫자로 변환
i = ord(coordinate[0]) - 97
# 입력받은 자료형이 'str' 이므로 'int' 로 변환
j = int(coordinate[1]) - 1
print(knight(i,j))