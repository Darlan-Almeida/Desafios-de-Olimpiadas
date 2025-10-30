n , q = map(int , input().split())
a = list(map(int , input().split()))
for i in range(1 , n):
    a[i] += a[i-1]
while q > 0:
    q -= 1
    l , r = map(int , input().split())
    if l > 1:
        print(a[r-1] - a[l-2])
    else:
        print(a[r-1])

