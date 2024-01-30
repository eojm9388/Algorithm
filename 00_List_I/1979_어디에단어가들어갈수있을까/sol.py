import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def row_check(x, y, k):
    check_count = 0
    # 범위를 벗어난다면 0
    if x + k >= N:
        return 0
    # 다음 칸이 비어있다면 0
    if x < N - k:
        if word_map[x+k][y] == 1:
            return 0

    for i in range(k):
        if word_map[x+i][y] == 1:
            check_count += 1

    if check_count == K:
        return 1
    else:
        return 0


def column_check(x, y, k):
    check_count = 0
    if y + k >= N:
        return 0

    if y < N - k:
        if word_map[x][y+k] == 1:
            return 0

    for i in range(k):
        if word_map[x][y+i] == 1:
            check_count += 1

    if check_count == K:
        return 1
    else:
        return 0





for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    word_map = [list(map(int, input().split())) for i in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            result += row_check(i, j, K)
            result += column_check(i, j, K)
    print(result)
