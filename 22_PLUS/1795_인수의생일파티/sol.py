import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop

def Dijkstra(start):
    pq = []
    heappush(pq, (0, start))

    while pq:
        dist, now_node = heappop(pq)
        if distance[now_node] < dist:
            continue

        for next_dist, next_node in edge[now_node]:

            new_dist = dist + next_dist
            if new_dist >= distance[next_node]:
                continue
            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))


T = int(input())

for test_case in range(1, T + 1):
    V, E, X = map(int, input().split())
    INF = int(1e10)
    edge = [[] for _ in range(V+1)]
    distance = [INF] * (V+1)
    for _ in range(E):
        s, e, d = map(int, input().split())
        edge[s].append([d, e])

    # X 에서 각 집에 가는 최단 경로
    Dijkstra(X)
    distance_back = distance[:]
    max_dist = 0
    # 각 집에서 X까지 가는 최단 경로
    for i in range(1, V+1):
        if i == X:
            continue
        distance = [INF] * (V+1)
        Dijkstra(i)
        max_dist = max(max_dist, distance[X] + distance_back[i])

    print(f'#{test_case}', max_dist)


