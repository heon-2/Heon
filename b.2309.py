dwarf = [ int(input()) for _ in range(9) ]
dwarf.sort()
def seven(x,y) :
    global sum,dwarf_lst
    sum = 0
    dwarf_lst = []
    for i in dwarf :
        if i != x and i != y :
            sum += i
            dwarf_lst.append(i)
    if sum == 100 :
        return 1

breaker = False

for i in range(9) :
    if not breaker :
        for j in range(9) :
            if i != j :
                x = seven(dwarf[i],dwarf[j])
                if x == 1 :
                    print(*dwarf_lst,sep='\n')
                    breaker = True
                    break

