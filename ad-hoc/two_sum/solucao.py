n , alvo = map(int , input().split())
a = list(map(int , input().split()))
elementos = {}

print
for i in range(n):
    meta = alvo - a[i]
    if meta in elementos:
        print(elementos[meta] + 1 , i+1)
        exit(0)
    elementos[a[i]] = i
    
print("IMPOSSIBLE")