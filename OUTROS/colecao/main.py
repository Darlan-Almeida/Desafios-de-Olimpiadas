from random import random, randint





"""Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) está no vetor. Caso o valor x não seja encontrado, o
programa deve imprimir o valor -1 
- Crie uma lista de 5 elementos e preencha com uma iteração sobre a lista com valores lidos do teclado
- Leia um número do teclado
- Compare se este número está na lista"""




def fill():
    list_number = [ ]

    for _ in range(5):
        number = int(input("send the number"))
        list_number.append(number)

    number_verify = int(input("verify if the number is in list"))


    if(number_verify in list_number):
        print("The number is in list!")
    
    else:
        print("The number is not list!")


def dice():
    dice_quantity = [randint(1,6) for i in range(50)]

    number = int(input("Send the number"))

    quantity_number = 0


    for i in dice_quantity:
        if( i == number):
            quantity_number += 1


    print(quantity_number)

#fazendo...
def list_manipulation():
    list_random =  [2, 1, 20,5, 17,19,14,4, 18,2]
    list_manipulated = []
    for_index = 0
    new_numero = int()

    for index, i in enumerate(list_random):
        if(index == 0):
            list_manipulated.append(i)
        for j in list_manipulated:
            if(index >= for_index):
                for_index += 1
                new_numero = i + j
                list_manipulated.append(new_numero)
                
                
    print(list_random)
    print(list_manipulated)


list_manipulation()

            



