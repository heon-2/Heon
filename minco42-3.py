words =['BTS','SBS','BS','CBS','SES']
ans = input()
cnt = 0
while True :
    cnt += 1
    path = []
    word_lst = []
    def dfs(level) :
        if level == cnt :
            word_lst.append(''.join(path))
            return

        for i in range(5) :
            path.append(words[i])
            dfs(level+1)
            path.pop()

    dfs(0)
    if ans in word_lst :
        print(cnt)
        break




