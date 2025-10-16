def bs(alvo , a):
    l, r = 0 , len(a) - 1

    while l <= r:
        meio = (l+r) // 2
        if a[meio] == alvo:
            return meio
        elif a[meio] > alvo:
            r = meio - 1
        else:
            l = meio + 1
    return l - 1

"""a = [1 , 2 , 5]
print(bs(1 , a))
print(bs(2 , a))
print(bs(4 , a))
print(bs(9 , a))
print(bs(10 , a))"""



"""a = [1 , 2 , 3 ,  5 , 7 , 9 , 11]
print(bs(0 , a))
print(bs(1 , a))
print(bs(2 , a))
print(bs(4 , a))
print(bs(6 , a))
print(bs(8 , a))
print(bs(10 , a))
print(bs(11 , a))
print(bs(15 , a))"""

a = [5]
print(bs(2 , a))