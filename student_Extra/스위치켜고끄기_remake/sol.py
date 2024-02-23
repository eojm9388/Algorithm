import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 스위치 개수 N
    N = int(input())
    # 스위치 점등 상태
    switch = [0] + list(map(int, input().split()))
    # 학생 수 S
    S = int(input())
    # 학생 정보 리스트
    student = [list(map(int, input().split())) for _ in range(S)]

    def switch_on_off(i):
        if switch[i] == 0:
            switch[i] = 1
        else:
            switch[i] = 0

    def PrimeNumber(num):
        for i in range(2, num):
            if num % i == 0:
                return False

        return True
    # 학생 성별 s (1남자, 2여자), 학생이 받은 번호
    for s, n in student:
        # 남학생일 경우
        if s % 2 == 1:
            for i in range(2, N+1):
                if PrimeNumber(i):
                    for j in range(i-n, i+n+1):
                        if j < 1 or j > N:
                            continue
                        else:
                            switch_on_off(j)
        # 여학생일 경우
        else:
            for i in range(1, n+1):
                if n % i == 0:
                    switch_on_off(i)

    # 20개 단위로 스위치 출력
    print(f'#{tc}')
    for j in range(1, N, 20):
        print(' '.join(map(str, switch[j:j+20])))