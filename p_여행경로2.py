
def solution(tickets):
    answer = []

    def dfs(ed,tickets,i,level) :
        if level == len(tickets) :
            print(path)
        for k in range(len(tickets)) :
            if i != k :
                if tickets[k][0] == ed:
                    if not visited[k] :
                        visited[k] = True
                        path.append(tickets[k][1])
                        dfs(tickets[k][1],tickets,k,level+1)
                        visited[k] = False


    for i in range(len(tickets)) :
        visited = [False] * len(tickets)
        visited[i] = True
        path = [tickets[i][0],tickets[i][1]]
        rlt = dfs( tickets[i][1], tickets, i,0)
        if rlt is not None :
            if len(rlt) == len(tickets) +1 :
                answer.append(path)
    answer.sort()

    return answer

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
solution([["ICN", "BBB"], ["ICN", "CCC"], ["BBB", "CCC"], ["CCC", "BBB"], ["CCC", "ICN"]])