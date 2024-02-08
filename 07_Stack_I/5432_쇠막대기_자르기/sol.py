import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = list(input())
    N = len(str1)

    counts = [None] * N

    for i in range(1, N):
        if str1[i-1] == '(' and str1[i] == ')':
            counts[i] = 'l'
        elif str1[i-1] == '(' and str1[i] == '(':
            counts[i] = 's'
        elif str1[i-1] == ')' and str1[i] == '(':
            counts[i] = 's'
        elif str1[i-1] == ')' and str1[i] == ')':
            counts[i] = 's'

    print(counts)