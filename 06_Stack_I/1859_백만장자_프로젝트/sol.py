import time
import sys
sys.stdin = open("input.txt")

start = time.time()


T = int(input())

def sale(sales):
    global result
    if not sales:
        return
    else:
        max_price = max(sales)
        max_price_index = sales.index(max_price)
        if max_price_index != 0:
            result += (max_price_index * max_price) - sum(sales[:max_price_index])
        new_sales = sales[max_price_index+1:]
        sale(new_sales)



for tc in range(1, T+1):
    N = int(input())
    sales = list(map(int, input().split()))
    result = 0

    sale(sales)
    print(f'#{tc}', result)



end = time.time()
print(end-start)