def f(i, k, s):
    if


    if i == k:
        print(*P)

    else:
        for j in range(i, k):
            P[i], P[j] = P[j], P[i]
            f(i+1, k, )
            P[i], P[j] = P[j], P[i]





P = [1, 2, 3]
f(0, 3, 0)