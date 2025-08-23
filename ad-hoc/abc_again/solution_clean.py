
N, Q = map(int, input().split())
S = list(input().strip())

# Contar ocorrências iniciais de "ABC"
count = 0
for i in range(N - 2):
    if S[i] == 'A' and S[i + 1] == 'B' and S[i + 2] == 'C':
        count += 1

for _ in range(Q):
    x, c = input().split()
    x = int(x) - 1  # converter para índice 0-based

    # Remover ocorrências afetadas
    for i in range(x - 2, x + 1):
        if 0 <= i <= N - 3:
            if S[i] == 'A' and S[i + 1] == 'B' and S[i + 2] == 'C':
                count -= 1

    # Atualizar caractere
    S[x] = c

    # Adicionar ocorrências afetadas
    for i in range(x - 2, x + 1):
        if 0 <= i <= N - 3:
            if S[i] == 'A' and S[i + 1] == 'B' and S[i + 2] == 'C':
                count += 1

    # Imprimir resultado atual
    print(count)
