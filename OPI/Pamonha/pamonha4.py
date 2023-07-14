def pamonha():

    k = int(input())
    n = int(input())
    w = int(input())

    total = []
    for i in range(1,w+1):
        total.append(k*i)

    if sum(total) > n:
        return sum(total)-n
    else:
        return 0
