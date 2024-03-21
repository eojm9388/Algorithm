import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop

def prim(start):
    # 우선순위 큐 사용
    pq = []
    # 시작점 추가 (가중치, 노드 번호)
    heappush(pq, (0, start))

    # 방문 처리
    visited = [0] * (V+1)
    # 가중치 합
    sum_weight = 0

    while pq:
        # 현재 가중치, 현재 노드 번호
        weight, now_node = heappop(pq)
        # 만약 방문했던 노드라면 건너뜀 -> 이미 가중치가 작은게 방문함
        if visited[now_node] == 1:
            continue

        # 방문 처리
        visited[now_node] = 1
        # 가중치 더하기
        sum_weight += weight

        # 갈 수 있는 노드 탐색
        for next_node in range(V+1):
            # 만약 갈 수 있고, 방문했던 노드가 아니라면
            if graph[now_node][next_node] == 0 or visited[next_node]:
                continue
            # 우선순위 큐에 추가
            heappush(pq, (graph[now_node][next_node], next_node))

    return sum_weight



T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    # 간선 정보 리스트
    # 마지막 노드 번호가 V이기 때문에 노드의 개수는 V+1
    # 인접 행렬로 저장
    graph = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
        graph[e][s] = w

    sum_weight = prim(0)
    print(f'#{test_case}', sum_weight)



