import sys
sys.stdin = open("input.txt")

T = int(input())

def DFS(i, k, s):
    global min_s
    global cnt
    cnt += 1

    if s > min_s:
        return

    elif i == k:
        if min_s > s:
            min_s = s
        return

    for n in range(N):
        if visited[n] < 2:
            visited[n] += 1
            DFS(i+1, k, s+arr[i][n])
            visited[n] -= 1

for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    visited = [0] * N
    min_s = 1000000000000
    DFS(0, N, 0)

    print(min_s)
    print(cnt)

    print()
    # print(arr)