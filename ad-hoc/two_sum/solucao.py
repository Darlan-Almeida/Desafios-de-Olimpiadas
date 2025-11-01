def busca(x , y):
    pos1 = 0
    pos1_preenchida = False
    pos2 = 0


    for i in range(n):
        if a[i] == x and not pos1_preenchida:
            pos1 = i
            pos1_preenchida = True
        elif a[i] == y:
            pos2 = i
        
    if pos1 > pos2:
        menor , maior = pos2 , pos1
    else:
        menor , maior = pos1 , pos2

    print(menor + 1 , maior + 1)

n , alvo = map(int , input().split())
a = list(map(int , input().split()))
ordenado = sorted(a)

l , r = 0 , n - 1
while l < r:
    soma = ordenado[l] + ordenado[r]

    if soma == alvo:
        busca(ordenado[l] , ordenado[r])
        exit(0)

    elif soma < alvo:
        l += 1
    else:
        r -= 1

print("IMPOSSIBLE")

















"""elementos = {}


for i in range(n):
    meta = alvo - a[i]
    if meta in elementos:
        print(elementos[meta] + 1 , i+1)
        exit(0)
    elementos[a[i]] = i
    
print("IMPOSSIBLE")"""