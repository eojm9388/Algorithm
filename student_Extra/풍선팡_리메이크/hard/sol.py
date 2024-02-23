import sys
import copy
sys.stdin = open("input.txt")

T = int(input())

def Pang_2(x, y):
    flowers = Filed[x][y]
    if flowers % 2 == 1:
        for dx, dy in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and die[nx][ny] == 0:
                flowers += Filed[nx][ny]


    else:
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and die[nx][ny] == 0:
                flowers += Filed[nx][ny]

    return flowers



def Pang(i, j):
    global shot
    shot = 1
    flowers = Filed[i][j]
    die[i][j] = 1
    if flowers % 2 == 1:
        for di, dj in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and die[ni][nj] == 0:
                flowers += Filed[ni][nj]
                die[ni][nj] = 1
        if flowers % 2 == 1:
            shot += 1
            if shot > 2:
                return flowers
            for x in range(N):
                for y in range(M):
                    if die[x][y] == 0:
                        result.append(flowers + Pang_2(x, y))



    else:
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<M and die[ni][nj] == 0:
                flowers += Filed[ni][nj]
                die[ni][nj] = 1

        if flowers % 2 == 0:
            shot += 1
            if shot > 2:
                return flowers
            for x in range(N):
                for y in range(M):
                    if die[x][y] == 0:
                        result.append(flowers + Pang_2(x, y))


    return flowers


for tc in range(1, T+1):
    N, M = map(int, input().split())

    Filed = [list(map(int, input().split())) for _ in range(N)]
    shot = 1
    result = []
    for i in range(N):
        for j in range(M):
            die = [[0] * M for _ in range(N)]
            result.append(Pang(i, j))


    # print(result)
    print(f'#{tc}', max(result))