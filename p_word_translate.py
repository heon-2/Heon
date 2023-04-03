from collections import deque


def solution(begin, target, words):
    # 타겟이 words에 없으면 0반환
    if target not in words:
        return 0
    # 타겟이 words에 있을 때,
    else:
        # begin이 words에 있으면, 그냥 진행

        visited = [0] * len(words)
        answer = bfs(begin, target, words, visited)
        return answer


def bfs(begin, target, words, visited):
    q = deque()
    # words의 첫단어 큐에 넣어주고, visited 1 체크
    q.append(words[0])
    visited[0] = 1
    while q:
        # 뽑은 단어의 인덱스 찾기
        pick = q.popleft()
        pick_idx = words.index(pick)
        for word in words:
            # 뽑은 단어랑 각 단어랑 비교해서 알파벳 몇개가 같은지 비교
            same_cnt = 0
            for i in range(len(begin)):
                if pick[i] == word[i]:
                    same_cnt += 1
            # 만약 전체 단어의 개수에 -1 한 만큼 같다면 ( = 알파벳 1개만 다르다면! )
            if same_cnt == len(word) - 1:
                # 그 단어가 있는 인덱스를 저장해두자
                idx = words.index(word)
                # 그 인덱스값의 visited 배열이 0이라면(아직 방문 안 했다면, +1 해주기)
                if visited[idx] == 0:
                    visited[idx] = visited[pick_idx] + 1
                    q.append(words[idx])
                # 방문했지만 해당 단어로 변환하기 위해 최솟값이 존재한다면 최솟값 갱신해주기.
                else:
                    if visited[idx] > visited[pick_idx] + 1:
                        visited[idx] = visited[pick_idx] + 1
                        q.append(words[idx])
    # 타겟의 인덱스 번호를 찾아서 visited 배열에 적혀있는 숫자에 -1 한 값 리턴해주기
    # 시작할 때 1부터 시작했으니깐.
    rlt = words.index(target)
    return visited[rlt] - 1