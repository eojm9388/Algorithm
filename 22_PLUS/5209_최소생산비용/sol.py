# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

# 생산한 제품 개수, 생산 비용
def f(i, c):
    global min_cost
    if c >= min_cost:
        return

    if i == N:
        min_cost = min(min_cost, c)
        return

    for j in range(N):
        # 아직 생산하지 않은 공장이라면 생산
        if used[j] == 0:
            used[j] = 1
            f(i+1, c+arr[i][j])
            # 초기화
            used[j] = 0




for test_case in range(1, T + 1):
    N = int(input())
    # 공장별 생산비용
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최소 비용
    min_cost = 99 * 15

    # 공장당 한가지씩 생산 -> 생산한 공장 기록
    used = [0] * N

    f(0, 0)

    print(f'#{test_case}', min_cost)