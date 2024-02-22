import sys
sys.stdin = open('input.txt')

T = int(input())

BIN = [format(i, 'b').zfill(4) for i in range(17)]
END_BIN = [i.rstrip('0') for i in BIN]
# print(BIN)
# print(END_BIN)
def make_code(start, count, line, after):
    new_line = line
    after_code = new_line[start] + after
    if count > 1:
        new_code = BIN[int(line[start], 16)]
    else:
        new_code = END_BIN[int(line[start], 16)]
    start -= 1
    while len(new_code) < 56:
        after_code = new_line[start] + after_code
        code_one = BIN[int(line[start], 16)]
        new_code = code_one + new_code
        start -= 1
    if new_line[start-1] != '0':
        new_code = make_code(start-1, count+1, new_line, after_code) + new_code
        return new_code, after_code
    else:
        return new_code, after_code
#
#

def make_after(code, after):
    after_code = code.replace(after, '').rstrip('0')
    return after_code
for tc in range(1, T+1):
    print(tc)
    N, M = map(int, input().split())
    code_line = []
    for n in range(N):
        line = input().rstrip('0')
        s = len(line)
        if s:
            code, after = make_code(-1, 1, line, '')
            line = make_after(line, after)
            print(line)
            while len(line):
                continue


            k = len(code) % 56

            # print(code[k:])


    # print(code_line)

