import sys
sys.stdin = open("input.txt", "r")

from collections import deque
T = int(input())

def BFS(i):
    q = deque()
    q.append([i, 0])
    visited = [False] * 1000010
    while q:
        v = q.popleft()
        if v[0] == M:
            return v[1]
        y = v[1] + 1

        for x in [v[0]-1, v[0]+1, v[0]*2, v[0]-10]:
            if x > 0 and x < M+10 and visited[x] == False:
                q.append([x, y])
                visited[x] = True


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    min_cnt = BFS(N)
    print(f'#{test_case}', min_cnt)