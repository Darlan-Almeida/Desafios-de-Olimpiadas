n = int(input())
a = list(map(int , input().split()))
s = {a[0]}
maior = 1

l,r = 0 , 1

while r < n:
    if a[l] == a[r]:
        s.remove(a[l])
        l += 1
    if a[r] in s:
        s.remove(a[l])
        l += 1
    else:
        s.add(a[r])
        if len(s) > maior:
            maior = len(s)
        r += 1

"""for i in range(n):
    for j in range(i , n):
        if a[j] in s:
            s = set()
            break
        else:
            s.add(a[j])
        if len(s) > maior:
            maior = len(s)
"""
print(maior)