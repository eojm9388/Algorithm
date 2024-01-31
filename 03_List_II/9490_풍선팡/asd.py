import sys
sys.stdin = open('input.txt', "r")

# 테스트 케이스 수 입력받기
T = int(input())

# 각각의 테스트 케이스 별로 입력값 받기
for t in range(1, T + 1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]
    flower_list = []
    for i in range(N):
        for j in range(M):
            flowers = balloons[i][j]
            # 현재 좌표의 꽃가루 수
            my_flower = flowers
            # di [0, 0, 0, 0, 0, -2, -1, 0, 1, 2]
            di = list(range(-my_flower, my_flower+1))
            for _ in range(-my_flower, my_flower+1):
                di.insert(0, 0)
            # dj [-2, -1, 0, 1, 2, 0, 0, 0, 0, 0]
            dj = list(range(-my_flower, my_flower+1))
            for _ in range(-my_flower, my_flower+1):
                dj.append(0)

                                # 10개
            for k in range(2*(2*my_flower+1)):
                ni = i + di[k]
                nj = j + dj[k]
                if ni in range(N) and nj in range(M):
                    flowers += balloons[ni][nj]
            # 본인의 꽃가루 가 2번 더 추가됨
            flowers -= my_flower
            flowers -= my_flower
            flower_list.append(flowers)

    print(f'#{t} {max(flower_list)}')
