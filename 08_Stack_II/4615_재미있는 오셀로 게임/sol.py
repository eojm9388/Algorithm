import sys

sys.stdin = open("input.txt")

T = int(input())


def f(x, y, color):
    board[y - 1][x - 1] = color


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = [[None] * N for _ in range(N)]

    board[N // 2 - 1][N // 2 - 1] = 'W'
    board[N // 2 - 1][N // 2] = 'B'
    board[N // 2][N // 2 - 1] = 'B'
    board[N // 2][N // 2] = 'W'

    for m in range(M):
        x, y, color = map(int, input().split())
        if color == 1:
            color = 'B'
        else:
            color = 'W'

        f(x, y, color)

    for i in range(N):
        print(board[i])

