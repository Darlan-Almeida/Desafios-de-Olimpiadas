def encontrar_maior_menor(lista):
    if not lista:
        return None, None  # Retorna None se a lista estiver vazia

    maior = lista[0]
    menor = lista[0]

    for elemento in lista:
        if elemento > maior:
            maior = elemento
        if elemento < menor:
            menor = elemento

    return maior, menor

# Exemplo de uso
lista_numeros = [9, 3, 7, 1, 5, 2]
maior_numero, menor_numero = encontrar_maior_menor(lista_numeros)

print("Maior número:", maior_numero)
print("Menor número:", menor_numero)
