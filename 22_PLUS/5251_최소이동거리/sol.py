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
    V, E = map(int, input().split())

    INF = int(1e10)
    edge = [[] for _ in range(V+1)]
    distance = [INF] * (V+1)
    for _ in range(E):
        s, e, d = map(int, input().split())
        edge[s].append([d, e])

    Dijkstra(0)
    print(f'#{test_case}', distance[V])


