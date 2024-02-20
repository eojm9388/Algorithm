# import sys
# sys.stdin = open('input.txt')

T = int(input())

def pre_order(n):
    global count
    # 왼쪽 자식에 노드가 있다면
    if left[n]:
        count += 1
        # 왼쪽 자식으로 이동
        pre_order(left[n])
    # 오른쪽 자식이 있다면
    if right[n]:
        count += 1
        # 오른쪽으로 이동
        pre_order(right[n])



for tc in range(1, T+1):
    # 간선의 개수 E, 서브 트리의 루트 N
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))
    # 노드의 개수
    count = 1
    # 왼쪽 자식
    left = [0] * (E+2)
    # 오른쪽 자식
    right = [0] * (E+2)

    # 트리 생성
    for i in range(E):
        # 부모, 자식
        p, c = edge[2*i], edge[2*i+1]
        # 왼쪽 자식부터 만들어준다.
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    # 전위 순회 -> 순회는 상위 노드를 순화하지 않는다.
    pre_order(N)
    print(f'#{tc}', count)
