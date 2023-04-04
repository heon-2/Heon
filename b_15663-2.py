N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
visited = [False] * len(lst)
path = []
answers = set()

def x(level,path) :

    if level == M :
        result = " ".join(map(str,path))
        if result not in answers :
            answers.add(result)
            print(result)
        return

    for i in range(len(lst)) :
        if not visited[i] :
            visited[i] = True
            x(level+1,path+[lst[i]])
            visited[i] = False

x(0,path)

# for answer in answers :
#     print(*answer)


# 1 = 6
# 9 = 12
# 7 = 6
# 4개 중 2개 뽑는 경우 각 숫자는 6번씩 등장함 => 총 경우의 수가 12개니깐..

