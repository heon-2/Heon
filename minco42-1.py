ingredient = list(input())

path = [''] * 3

def gimbap(level,start) :
    if level == 3 :
        for i in path :
            print(i,end='')
        print()
        return

    for i in range(start,len(ingredient)) :
        path[level] = ingredient[i]
        gimbap(level+1,i)
        path[level] = ''

gimbap(0,0)


