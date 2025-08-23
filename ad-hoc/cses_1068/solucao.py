entrada = int(input())
saida = str(entrada)

elemento = entrada
while elemento != 1:
    if elemento % 2 == 0:
        elemento = elemento / 2
    else:
        elemento = elemento * 3 + 1
    
    saida += " " + str(int(elemento))

print(saida)