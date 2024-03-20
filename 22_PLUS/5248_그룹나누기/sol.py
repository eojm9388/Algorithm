import sys
sys.stdin = open("input.txt", "r")

def make_p(i):
    p = [x for x in range(i)]

    return p

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])

    return p[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        if root_x < root_y:
            p[root_y] = root_x
        else:
            p[root_x] = root_y



T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))
    p = make_p(N+1)

    for j in range(M):
        union(arr[2*j], arr[2*j+1])

    for k in range(1, N+1):
        find_set(k)

    cnt = 0
    visited = []
    for n in p[1:]:
        if n not in visited:
            cnt += 1
            visited.append(n)

    print(f'#{test_case}', cnt)