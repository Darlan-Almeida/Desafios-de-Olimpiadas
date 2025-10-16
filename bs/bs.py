def busca(a , l, r , alvo):
    
    l = 0
    r = len(a) - 1

    while True:

        meio = (l + r) // 2

        if l > r:
            return meio+1

        if a[meio] == alvo:
            return meio
        elif a[meio] > alvo:
            r = meio - 1   # busca na metade esquerda
        else:
            l = meio + 1   # busca na metade direita


    
a = [1, 3, 5, 7, 9, 11]
print(busca(a, 0, len(a) - 1, 7))   # Saída: 3
print(busca(a, 0, len(a) - 1, 2))   # Saída: -1
print(busca(a, 0, len(a) - 1, 10))   # Saída: -1