import sys
sys.stdin = open("input.txt")

T = int(input())

def Pang(i, j):
    flowers = Filed[i][j]

    if flowers % 2 == 1:
        for di, dj in [[1, 1], [1, -1], [1, 1], [-1, 1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                flowers += Filed[ni][nj]
    else:
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<M:
                flowers += Filed[ni][nj]


    return flowers


for tc in range(1, T+1):
    N, M = map(int, input().split())

    Filed = [list(map(int, input().split())) for _ in range(N)]

    result = []

    for i in range(N):
        for j in range(M):
            result.append(Pang(i, j))
    print(result)
    print(f'#{tc}', max(result))