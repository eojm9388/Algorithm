import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def check(x, y, k):
    check_count = 0
    result = 0
    for i in range(k):
        if y + k >= N:
            break
        else:
            if word_solving[x][y+i] == 0:
                break
            else:
                check_count += 1
    if check_count == k:
        if word_solving[x][y+k] == 0:
            result += 1


    check_count = 0
    for j in range(k):
        if x + k >= N:
            break
        else:
            if word_solving[x+j][y] == 0:
                break
            else:
                check_count += 1

    if check_count == k:
        if word_solving[x+k][y] == 0:
            result += 1
    return result





for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    word_solving = [list(map(int, input().split())) for i in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            result += check(i, j, K)
    # print(result)
