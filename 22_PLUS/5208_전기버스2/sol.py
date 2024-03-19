# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 정류장 번호, 남은 배터리, 교체 횟수
def f(i, battery, c):
    global min_cnt
    # 최소 교체 횟수 이상이라면 가지치기
    if c >= min_cnt:
        return

    # 정류장에 도착했다면 최소 교체 횟수 갱신
    if i >= N:
        min_cnt = min(min_cnt, c)
        return

    # 배터리가 0이라면 강제 교체
    if battery == 0:
        battery = battery_arr[i]
        c += 1

    # 배터리 교체 안하고 1칸 가기
    f(i + 1, battery - 1, c)
    # 배터리 교체하고 1칸 가기
    f(i + 1, battery_arr[i+1], c+1)


for test_case in range(1, T + 1):
    temp = list(map(int, input().split()))
    N = temp[0]
    # 정류장 충전기
    battery_arr = [0] + temp[1:] + [0]
    min_cnt = N - 1

    f(1, battery_arr[1], 0)
    print(f'#{test_case}', min_cnt)
