linhas = int(input())
i = 0
lista_numeros = []
circulos = 0

while( i < linhas):
    i += 1
    numeros = int(input())
    lista_numeros.append(numeros)
    try:
        if(lista_numeros[i - 1] == lista_numeros[i- 2]):
            lista_numeros.pop(i-1)
    except:
        pass
    circulos = len(lista_numeros)
        
print(circulos)
