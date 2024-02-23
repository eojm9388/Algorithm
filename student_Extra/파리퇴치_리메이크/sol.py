import sys
sys.stdin = open("input.txt")

T = int(input())

# 내려치기
def smash(i, j):
    # 죽은 파리수
    cnt = 0
    # 평범한 파리채를 휘둘렀을때 죽는 파리 수 구하기
    for di in range(M):
        for dj in range(M):
            ni = i + di
            nj = j + dj
            cnt += filed[ni][nj]
    # 구멍 뚫린만큼 죽은 파리 수 빼기
    for di in range(1, M-1):
        for dj in range(1, M-1):
            ni = i + di
            nj = j + dj
            cnt -= filed[ni][nj]

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