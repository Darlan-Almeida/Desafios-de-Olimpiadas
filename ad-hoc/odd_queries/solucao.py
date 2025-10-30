t = int(input())

while t > 0:
    t -= 1
    n , q = map(int , input().split())
    a = list(map(int ,input().split()))
    acumulada = [a[0]]
    for i in range(1 , n):
        acumulada.append(acumulada[i-1] + a[i])

    while q > 0:
        q -= 1
        l , r , k = map(int , input().split())
        seq = k * (r - l + 1)

        x1 = acumulada[l-2] if l > 1 else 0
        x2 = acumulada[n-1]
        
        result = x1 + seq + (x2 - acumulada[r-1])
        #print(x1 , seq , x2 , acumulada[r-1])
        if result % 2 == 1:
            print("YES")
        else:
            print("NO")