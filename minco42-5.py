# 입력받은 숫자의 개수로 10을 만들 수 있는 조합의 수를 출력하시오
# 사용되는 숫자의 범위는 1~9

pick = int(input())
summ = 0
cnt = 0
def dfs(level) :
    global summ,cnt
    if level == pick :
        if summ == 10 :
            cnt +=1
            return
        else :
            return
    for i in range(1,10) :
        summ += i
        dfs(level+1)
        summ -= i
dfs(0)

print(cnt)