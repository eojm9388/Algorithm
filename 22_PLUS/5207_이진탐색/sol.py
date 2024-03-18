import sys
sys.stdin = open("input.txt")

T = int(input())

def binary_search(target, direction):
    global cnt
    low = 0
    high = len(A) - 1

    while low <= high:
        m = (low + high) // 2

        # 찾았다면 개수 증가
        if A[m] == target:
            cnt += 1
            return

        # 오른쪽 부분은 direction 2
        elif A[m] < target:
            # 같은 방향이면 조건 부적합
            if direction == 2:
                return
            low = m + 1
            direction = 2
        # 왼쪽 부분은 direction 1
        elif A[m] > target:
            if direction == 1:
                return
            high = m - 1
            direction = 1

    return



for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # A 리스트 정렬
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0

    for i in B:
        # B 리스트 요소 이진 탐색
        binary_search(i, 0)



    print(f'#{tc}', cnt)