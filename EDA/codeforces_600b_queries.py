import bisect

n , m = map(int , input().split())
nums = list(map(int , input().split()))
busca = list(map(int , input().split()))

busca_sorteada = sorted(busca)
acumulador = [0 for i in range(m)]

for i in nums:
    pos = bisect.bisect_left(busca_sorteada , i)
    if pos < len(acumulador):
        acumulador[pos] += 1

for i in range(1 , m):
    acumulador[i] += acumulador[i-1]

result = []

for i in busca:
    result.append(acumulador[bisect.bisect_left(busca_sorteada , i)])

print(*result)