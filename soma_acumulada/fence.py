n , k = map(int , input().split())
a = list(map(int , input().split()))

for i in range(1 , n):
    a[i] = a[i-1] + a[i]
menor = a[k-1]
inicial = 1

#print(a)
for i in range(1 , n):
    if k+i-1 < n:
        valor = a[k+i-1] - a[i-1]
        if valor < menor:
            menor = valor
            inicial = i+1

print(inicial)