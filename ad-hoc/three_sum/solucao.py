"""

n , alvo = map(int , input().split())
a = list(map(int , input().split()))
ordenado = sorted(a)

l , m , r = 0 , n // 2 , n - 1

resultado = ordenado[l] + ordenado[m] + ordenado[r]
out = [ordenado[l] , ordenado[m] , ordenado[r]]
while resultado != alvo:

    while alvo > resultado:
        if m + 1 < r:
            m += 1
            resultado = ordenado[l] + ordenado[m] + ordenado[r]
            out = [ordenado[l] , ordenado[m] , ordenado[r]]
        elif l + 1 < m:
            l += 1
            resultado = ordenado[l] + ordenado[m] + ordenado[r]
            out = [ordenado[l] , ordenado[m] , ordenado[r]]
        else:
            print("IMPOSSIBLE")
            exit(0)
        
    while alvo < resultado:
        if m - 1 > l :
            m -= 1
            resultado = ordenado[l] + ordenado[m] + ordenado[r]
            out = [ordenado[l] , ordenado[m] , ordenado[r]]

        elif r - 1 > m:
            r -= 1
            resultado = ordenado[l] + ordenado[m] + ordenado[r]
            out = [ordenado[l] , ordenado[m] , ordenado[r]]
        else:
            print("IMPOSSIBLE")
            exit(0)
x = set()
for i in range(3):
    for j in range(n):
        if out[i] == a[j] and j not in x:
            out[i] = j+1
            x.add(j)
            break
    
print(*sorted(out))


"""
import bisect as bs
def bisect(lista , v):

    l , r = 0 , len(lista) - 1

    while l < r:
        m = (l + r) // 2
        if lista[m] == v:
            return m
        elif lista[m] > v:
            r = m - 1
        else:
            l = m + 1
    return -1

n , alvo = map(int , input().split())
a = list(map(int , input().split()))
ordenado = sorted(a)

l , r = 0 , n - 1
exec = 0
out = []
while l < r:
    busca = alvo - (ordenado[l] + ordenado[r])
    pos1 = bs.bisect_left(ordenado[l+1:r-1] , busca) + l+1

    #print(l , r , busca ,pos1)

    if ordenado[pos1] == busca:
        out = [ordenado[l] , ordenado[pos1], ordenado[r]]
        break
    elif pos1 == r-1:
        l += 1
    else: 
        r -= 1

if not out:
    print('IMPOSSIBLE')
else:
    x = set()
    for i in range(3):
        for j in range(n):
            if out[i] == a[j] and j not in x:
                out[i] = j+1
                x.add(j)
                break
        
    print(*sorted(out))

