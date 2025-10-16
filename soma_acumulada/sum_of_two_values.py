n , x = map(int , input().split())
a = list(map(int , input().split()))

values = {}

for i in range(n):
    if a[i]  in values:
        values[a[i]].append(i)   
    else:
        values[a[i]] = [i]
usados = []
for i in range(n):
    alvo = x - a[i]
    if alvo in values:
        for j in values[alvo]:
            if (i+1 , j+1) not in usados and (j+1 , i+1) not in usados and i != j :
                print(i+1 , j+1)
            usados.append((i+1 , j+1))
if len(usados) == 0:
    print(-1)
