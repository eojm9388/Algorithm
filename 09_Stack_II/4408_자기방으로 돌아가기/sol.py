# import sys
# sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    start_room = [2]
    end_room = [400]

    result = []
    for i in range(N):
        count = 0
        start, end = map(int, input().split())
        if start % 2 == 1:
            start += 1
        if end % 2 == 1:
            end += 1

        for j in range(i+1):
            if end_room[j] == start:
                continue
            elif start_room[i] == end:
                continue
            if start_room[j] <= start <= end_room[j]:
                count += 1

        result.append(count)
        start_room.append(start)
        end_room.append(end)

    print(f'#{tc}', max(result))