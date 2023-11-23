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

"""- Vetor original [2, 1, 20,5, 17,19,14,4, 18,2]
- Vetor manipulado [2, 3, 25,35,82,166, 327, 644, 1302,2588]"""
def list_manipulation():
    list_random =  [2, 1, 20,5, 17,19,14,4, 18,2]
    list_manipulated = []
    new_numero = int()

    for index, valor in enumerate(list_random):
        if(index == 0):
            list_manipulated.append(valor)
        else:
            for valor2 in list_manipulated:
                new_numero += valor2

            list_manipulated.append(new_numero + valor)
            new_numero = 0    

                
                
    print(list_random)
    print(list_manipulated)




            

def exponenciacion(lista):
    print(list(map(lambda x: x ** 2, lista)))


"""
5 - Crie uma lista de quadrados dos números de 1 a 10 usando list comprehension.
- Crie uma lista de números de 1-10 utilizando range
- Utilizando list comprehension gere os números quadrados a partir da primeira lista
"""

def list_comprehension():
    lista =[ ]
    for i in range(11):
        lista.append(i)

    new_list = [i ** 2 for i in lista]

    print(new_list)

'''
6 - Faça um programa que converta uma lista de temperaturas de Fahrenheit para Celsius, em seu programa o usuário deverá inserir uma sequência de valores que representam a temperatura em graus Fahrenheit, seu programa deve receber esses valores e armazenar em uma lista até que o valor inserido pelo usuário seja um valor em branco (uma string vazia). Converta todos os valores presentes na lista para graus Celsius usando a função map e imprima na tela em uma formatação amigável ao usuário.
- Utilize o while e no bloco de repetição leia dados de temperatura do usuário
- Acrescente os dados na lista
- Crie uma função para converter temperatura Celcios para Farenheint
- Use a função map com a função e a lista
- Imprima todas os valores da nova lista
'''

def temperature():
    temperature_celsius = input("type of the temperture in Celsius Scale:")
    list_celsius = []
    while( temperature_celsius != ""):
        list_celsius.append(temperature_celsius)
        temperature_celsius = input("type of the temperture in Celsius Scale:")

    def celsius_to_farenheith(celsius):
        farenheith = (float(celsius) * 1.8) * 32

        return farenheith
    
    conversions = list(map(celsius_to_farenheith , list_celsius))

    for conversion in conversions:
        print(f"{conversion:.2f}")
        
"""6 - A partir do dicionário de nomes e idades de pessoas a seguir, faça um programa que imprima em ordem a partir dos nomes das pessoas, mostre a soma das idades, a média das idades e a pessoa mais velha. 
```py
people = {
    "Rafael": 41,
    "Anne": 28,
    "Jen": 32,
    "Satan": 2000000,
    "Frank": 12,
    "Sally": 19,
    "Bob": 42,
    "Sue": 21,
    "Jill": 32,
    "Jack": 32,
}"""

def employes():
    people = {
    "Rafael": 41,
    "Anne": 28,
    "Jen": 32,
    "Satan": 20,
    "Frank": 12,
    "Sally": 19,
    "Bob": 42,
    "Sue": 210,
    "Jill": 32,
    "Jack": 32,
    }
    
    list_order = sorted(people)
    ages = 0
    quantity_people = len(people)
    people_old_ages = 0
    people_old = ""
    for person in list_order:
        print(person)
        ages +=  people[person]

        if(people[person] > people_old_ages):
            people_old = person



    average = ages/ quantity_people

    print(f"The sum of ages is equal: {ages}")
    print(f"The average of ages is equal: {average}")
    print(f"The people more old is {people_old}")


"""
7 - Escreva um programa em Python para calcular a soma de todos os elementos de cada tupla armazenada dentro de uma lista de tuplas.

Lista original de tuplas:

[(1, 2), (2, 3), (3, 4)]

Soma de todos os elementos de cada tupla armazenada dentro da mencionada lista de tuplas:

[3, 5, 7]

Lista original de tuplas:

[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

Soma de todos os elementos de cada tupla armazenada dentro da mencionada lista de tuplas:

[9, -1, 7, 8]

"""


def list_tupls():
    list_origin = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
    list_manipulated = [ ]
    som_tupls = None
    for i in list_origin:
        if(som_tupls != None):
            list_manipulated.append(som_tupls)
        som_tupls = 0
        for j in i:
            som_tupls += j 
    list_manipulated.append(som_tupls)
    print(list_manipulated)

list_tupls()