def busca(a , alvo):
    l , r = 0 , len(a)-1
    while l <= r:
        meio = (l+r) // 2
  
        if a[meio] > alvo:
            r = meio - 1
        else:
            l = meio + 1
    
    return l

n = int(input())
a = list(map(int , input().split()))
b = list(map(int , input().split()))

count = 0
positivos = 0
negativos = 0
zeros = 0
for i in range(n):
    valor = a[i] - b[i]
    if valor >= 0:
        if valor == 0:
            zeros += 1
        else:
            a[positivos] = valor
            positivos += 1
    else:
        b[negativos] = valor
        negativos += 1

a = a[0:positivos]
b = b[0:negativos]
a.sort()
b.sort()
#print(a , b)
tam_a = positivos-1
if sum(a) == 0:
    print(0)
else:
    result = 0
    for i in range(negativos):
        if b[i] + a[tam_a] > 0:
            alvo = abs(b[i])
            posicao_elemento = busca(a ,  alvo)
            #tam_a -= 1
            result += positivos - posicao_elemento


    result += (positivos*(positivos-1))/2 + zeros * positivos
    print(int(result))
