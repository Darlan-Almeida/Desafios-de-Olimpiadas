n , k = input().split()
entrada = [int(i) for i in input().split()]
entrada.sort()
menor = entrada[len(entrada) - 1] - entrada[0]

for i in range(int(k)+1):
    x = entrada[len(entrada) - 1 - int(k) + i] - entrada[i]
    print(x)
    if x < menor:
        menor = x

print(menor)