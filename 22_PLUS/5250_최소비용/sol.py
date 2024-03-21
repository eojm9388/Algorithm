import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop

def Dijkstra():
    pq = []
    # 우선순위 큐 (사용한 연료, i, j)
    heappush(pq, (0, 0, 0))

    while pq:
        dist, i, j = heappop(pq)
        # 만약 이미 최소 연료가 있다면 pass
        if distance[i][j] <= dist:
            continue

        # 통과한다면 최소 연료이다
        distance[i][j] = dist

        # 델타 탐색
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni = i + di
            nj = j + dj
            # 범위안이라면
            if 0<=ni<N and 0<=nj<N:
                # 만약 다음 지형이 더 높은 곳이라면
                if MAP[ni][nj] > MAP[i][j]:
                    # 다음 이동 연료 = 현재 연료 + 1 + 높이차
                    next_dist = dist + 1 + (MAP[ni][nj] - MAP[i][j])
                # 다음 지형이 낮은 곳이라면
                else:
                    # 다음 이동 연료 = 현재 연료 + 1
                    next_dist = dist + 1

                # 우선 순위 큐에 추가
                heappush(pq, (next_dist, ni, nj))




T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # 비교적 큰 값
    INF = int(1e6)
    # 칸의 높이
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # 해당 칸에 이동하는데 드는 최소 연료
    distance = [[INF] * N for _ in range(N)]

    Dijkstra()

    print(f'#{test_case}', distance[N-1][N-1])