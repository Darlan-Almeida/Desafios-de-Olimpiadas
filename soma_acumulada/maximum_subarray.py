n = int(input())
a = list(map(int , input().split()))

for i in range(1 , n):
    a[i] += a[i-1] if a[i] + a[i-1] > a[i] else a[i]

idx_maior = 0
maior = a[idx_maior]
for i in range(n):
    if a[i] > maior:
        maior = a[i]
        idx_maior = i

menor = 0
if maior <= 0:
    maior = a[0]
    acumula = 0
    for i in range(1 , n):
        if a[i] > a[i-1] * 2:
            var = a[i] - a[i-1]
            maior = var
            if a[i] > a[i-1]:
                acumula += var
        else:
            acumula = 0
    if acumula != 0:
        print(acumula)
    else:
        print(maior)
else:
    for i in range(idx_maior):
        if a[i] < menor:
            menor = a[i]
    print(maior - menor)
