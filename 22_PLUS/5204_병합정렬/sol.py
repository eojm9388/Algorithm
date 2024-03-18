# import sys
# sys.stdin = open("input.txt")

from collections import deque

T = int(input())

def merge(left, right):
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 증가
    global cnt
    result = []
    if left[-1] > right[-1]:
        cnt += 1

    # 왼쪽과 오른쪽 리스트들의 제일 앞에 값을 넣을거기 때문에 큐로 만듬
    q_left = deque(left)
    q_right = deque(right)

    while len(q_left) > 0 or len(q_right) > 0:
        # 리스트가 둘다 남아있을 경우
        if len(q_left) > 0 and len(q_right) > 0:
            # 제일 앞에 값 비교 후 작은 값 result에 추가
            if q_left[0] <= q_right[0]:
                result.append(q_left.popleft())
            else:
                result.append(q_right.popleft())

        # 둘 중 하나만 남았을 경우 작은 갑부터 추가
        elif len(q_left) > 0:
            result.append(q_left.popleft())
        elif len(q_right) > 0:
            result.append(q_right.popleft())

    return result



def merge_sort(arr):
    n = len(arr)
    # arr가 더 이사 나눠지지 않을 때까지 나누기
    if n == 1:
        return arr

    # 왼쪽과 오른쪽 리스트로 나누기
    left = []
    right = []
    # 중간 인덱스
    m = n // 2

    for l in range(m):
        left.append(arr[l])

    for r in range(m, n):
        right.append(arr[r])

    # 다시 왼쪽, 오른쪽 리스트 2등분 나누기
    left = merge_sort(left)
    right = merge_sort(right)

    # 병합하기
    return merge(left, right)




for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    temp = []

    temp.append(merge_sort(arr)[N//2])
    temp.append(cnt)

    print(f'#{tc} {temp[0]} {temp[1]}')
