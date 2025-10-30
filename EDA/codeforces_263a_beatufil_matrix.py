v = []

for i in range(5):
    entrada = list(input().split())
    v.append(entrada)

alvo = 3
result = 0
for i in range(5):
    for j in range(5):
        if v[i][j] == '1':
            
            result = abs(i+1 - alvo) + abs(j+1 - alvo)
            break

print(result)
