import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    result = 0
    count = 0
    stack = []
    for tk in str1:
        if tk == '(':
            if stack:
                count += 1
                stack.append(tk)
            else:
                stack.append(tk)

        else:
            if count:
                print(stack, count)
                result += count
                count -= 1
            stack.pop()

    print(result)





