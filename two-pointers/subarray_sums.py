n, x = map(int, input().split())
a = list(map(int, input().split()))

soma = 0
qtd = 0
l = 0

for r in range(n):
    soma += a[r]
    while soma > x:
        soma -= a[l]
        l += 1
    if soma == x:
        qtd += 1

print(qtd)
