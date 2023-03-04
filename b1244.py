S = int(input())
swit = list(map(int,input().split()))

def man(num) :
    for i in range(1,S+1) :
        idx = i-1
        if i % num == 0 :
            if swit[idx] == 1 :
                swit[idx] = 0
            elif swit[idx] == 0 :
                swit[idx] = 1

def woman(num) :
    idx = num-1
    if swit[idx] == 1 :
        swit[idx] = 0
    elif swit[idx] == 0 :
        swit[idx] = 1

    i = 0
    while True :
        i += 1
        if idx-i < 0 or idx+i >= S or swit[idx-i] != swit[idx+i] :
            break
        elif idx-i >= 0 and idx+i < S and swit[idx-i] == swit[idx+i] :
            if swit[idx-i] == 0 :
                swit[idx-i],swit[idx+i] = 1,1
            elif swit[idx-i] == 1 :
                swit[idx-i],swit[idx+i] = 0,0

student = int(input())
for i in range(student) :
    sex,num = map(int,input().split())
    if sex == 1 :
        man(num)
    elif sex == 2 :
        woman(num)

cnt = 0
for i in swit :
    cnt += 1
    print(i, end=' ')
    if cnt % 20 == 0 :
        print()
