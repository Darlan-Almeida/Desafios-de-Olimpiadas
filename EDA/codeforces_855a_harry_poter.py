n = int(input())

nomes = set()
while n > 0:
    n -= 1

    nome = input()
    
    if nome in nomes:
        print("YES")
    else:
        print("NO")
        nomes.add(nome)

    