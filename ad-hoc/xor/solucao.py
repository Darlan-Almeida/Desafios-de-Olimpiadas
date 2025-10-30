n , q = map(int , input().split())
a = list(map(int , input().split()))
acumulada = [a[0]]

for i in range(1 , n):
    acumulada.append(acumulada[i-1] ^ a[i])

while q > 0:
    q -= 1
    l , r = map(int , input().split())

    if l == 1:
        print(acumulada[r-1])
    else:
        print(acumulada[r-1] ^ acumulada[l-2])