import heapq

n = int(input())
v = list(map(int, input().split()))

fila = []
freq = {}
qtd_votos = v[0]

for i in range(1, n):
    if v[i] in freq:
        freq[v[i]] += 1
    else:
        freq[v[i]] = 1

    heapq.heappush(fila , -int(v[i]))
usados = set()
maior = -1


while fila:
    elemento = -heapq.heappop(fila)
    freq_ele = freq[elemento]
    if elemento not in usados: 
        while qtd_votos <= elemento:
            #print(qtd_votos , elemento)
            usados.add(elemento)
            if qtd_votos + (1 * freq_ele)  <= elemento:
                qtd_votos += (1 * freq_ele)
                elemento -= 1
            elif qtd_votos == elemento:
                qtd_votos += 1
                elemento -= 1

            else:
                qtd_votos += (elemento - qtd_votos + 1)

            if elemento in freq:
                    heapq.heappop(fila)
                    freq_ele += freq[elemento]
            #print(qtd_votos , elemento)


print(qtd_votos - v[0])