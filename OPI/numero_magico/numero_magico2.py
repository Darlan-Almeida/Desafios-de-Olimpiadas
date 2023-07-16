while(True):    
     
    entrada = str(input())

    entradasplited = list(entrada)

    entrada_numero = int(entrada)

    elevacoes = []

    contador = 0
    elevacao = 0
    contador2 = 0

    for i in entradasplited:
        contador += 1
        magico = (10 ** contador) + 1
        elevacao += magico
        elevacoes.append(elevacao)
        elevacao -= 1

    for i in elevacoes:
        contador2 += 1
        if(elevacoes):
            while(entrada_numero >= elevacoes[-contador2]):
                entrada_numero -= elevacoes[-contador2]

    if(entrada_numero != 0):
        print("NO")
    else:
        print("YES")
        
