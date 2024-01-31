import sys
sys.stdin = open('input.txt', "r")

# 테스트 케이스 수 입력받기
T = int(input())

# 각각의 테스트 케이스 별로 입력값 받기
for t in range(1, T + 1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    flower_list = []
    for i in range(N):
        for j in range(M):
            flowers = balloons[i][j]
            my_flowers = flowers
            for k in range(4):
                for l in range(1, my_flowers + 1):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if ni in range(N) and nj in range(M):
                        flowers += balloons[ni][nj]
            flower_list.append(flowers)

    print(f'#{t} {max(flower_list)}')