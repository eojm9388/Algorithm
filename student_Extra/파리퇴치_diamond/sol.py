import sys
sys.stdin = open("input.txt")

T = int(input())

# 내려치기


def smash(i, j):
    # 죽은 파리수
    cnt = 0
    dj = M // 2
    for n in range(1, M//2+1):
        up = i + n
        down = i - n
        if 0 <= up < N:
            for m in range(0, M//2+1):
                left = j - m
                right = j + m

        if 0 <= down < N:


    count = 0
    while count < M:
        l_i = j - dj
        r_i = j + dj
        if l_i < 0:
            l_i = 0
        if r_i >= N:
            r_i = N-1
        for k in range(l_i, r_i+1):
            filed[i+count][k]




    return cnt

for tc in range(1, T+1):
    N, M = map(int, input().split())
    filed = [list(map(int, input().split())) for _ in range(N)]
    result = []
    # 전체 순회
    for i in range(N-M+1):
        for j in range(N-M+1):
            result.append(smash(i, j))

    print(f'#{tc}', max(result))