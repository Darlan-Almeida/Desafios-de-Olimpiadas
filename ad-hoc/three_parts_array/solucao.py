l = 0
r = int(input()) - 1
a = list(map(int , input().split()))

l_sum = a[l]
r_sum = a[r]
total = 0

while l < r:
    
    if l_sum == r_sum:
        total = l_sum
        l += 1
        r -= 1
        l_sum += a[l]
        r_sum += a[r]
    elif l_sum > r_sum:
        r -= 1
        r_sum += a[r]
    else:
        l += 1
        l_sum += a[l]

print(total)