v = list(map(int , input().split()))

result = 0
for i in range(len(v)):
    result += 2**i if v[i] == 1 else 0

print(result)