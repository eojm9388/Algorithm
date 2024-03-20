import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def BFS(i):
    q = deque()
    # 시작 번호 방문처리 -> 나중에 0으로 변경
    visited[i] = 1
    # [번호, 통신 시간]
    q.append([i, 0])
    while q:
        v = q.popleft()
        # 현재 번호에 연결된 모든 비상 연락망 연결
        for j in adj[v[0]]:
            # 방문 안한 번호에만 연결
            if visited[j] == 0:
                # 걸린 시간으로 기록
                visited[j] = v[1]+1
                q.append([j, v[1]+1])




for test_case in range(1, 11):
    # 입력 받는 데이터 개수 N, 시작 번호 start
    N, start = map(int, input().split())
    # 입력 받은 데이터
    arr = list(map(int, input().split()))
    # 인접 리스트
    adj = [[] for _ in range(101)]
    # 방향 그래프 정보 넣기
    for i in range(0, N, 2):
        adj[arr[i]].append(arr[i+1])
    # 방문처리 해줄 리스트 생성
    visited = [0] * 101
    # BFS 탐색
    BFS(start)
    # 시작지점 0으로 초기화
    visited[start] = 0

    # 가장 나중에 연락 받은 시간
    max_time = 0
    # 가장 나중에 연락 받은 번호 중 제일 높은 수
    result = 0
    # 낮은 숫자부터 확인
    for i in range(101):
        if visited[i] != 0:
            # 제일 오래 걸렸다면
            if max_time <= visited[i]:
                max_time = visited[i]
                # 제일 나중 번호
                result = i

    print(f'#{test_case}', result)
