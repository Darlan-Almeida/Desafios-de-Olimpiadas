n = int(input())
a = list(map(int , input().split()))

for i in range(1 , n):
    a[i] = a[i] + a[i-1] if a[i] + a[i-1] > a[i] else a[i]

print(max(a))