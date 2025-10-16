t = int(input())

# igual ou menor mais próxima
def bs(alvo , a):
    l, r = 0 , len(a) - 1

    while l <= r:
        meio = (l+r) // 2
        if a[meio] == alvo:
            return meio
        elif a[meio] > alvo:
            r = meio - 1
        else:
            l = meio + 1
    return l - 1
        

while t > 0:
    t -= 1
    n , q = map(int , input().split())
    degraus = list(map(int , input().split()))
    questions = list(map(int , input().split()))

    distintos_unicos = sorted(degraus)
    for i in range(n - 1 , 0 , -1):
        if distintos_unicos[i] == distintos_unicos[i-1]:
            distintos_unicos.remove(distintos_unicos[i]) 
    
    acumulador = [0 for i in distintos_unicos]
    maior_encontrado = 0
    pos_maior = -1
    for i in range(n):
        valor = degraus[i] + degraus[i - 1] if i > 0 else degraus[i]
        if degraus[i] > maior_encontrado:
            maior_encontrado = degraus[i]
            pos_maior = i
        
        pos = bs(maior_encontrado, distintos_unicos)
        if pos > - 1:
            acumulador[pos] = valor
        
        degraus[i] = valor

    result = []
    for i in questions:
        if i == 0:
            result.append(0)
        else:
            pos = bs(i , distintos_unicos)
            if pos > -1:
                result.append(acumulador[pos])
            else:
                result.append(0)
    
    print(*result)


#alternativa usado dict

"""while t > 0:
    t -= 1
    n , q = map(int , input().split())
    degraus = list(map(int , input().split()))
    questions = list(map(int , input().split()))

    distintos = {}
    for i in range(1 , n):
        valor = degraus[i] + degraus[i - 1]
        distintos[degraus[i]] =  valor
        degraus[i] = valor
 
    # transforma distito em uma lista faz a bs e referencia o valor armazenado em outra lista
"""