"""
    Escreva um programa que solicite ao usuário um número e
    verifique se ele é par ou ímpar. Imprima uma mensagem informando o 
    resultado.
"""
def q1():
    number = int(input(''))

    if number % 2 == 0:
        print("Par")
    else:
        print("Impar")

"""
    Dada a string use o operador de fatiamento para imprimir somente a metade final
    Para 'abcdef, imprima: 'def'
    Para 'texto', imprima 'to'
"""

def q2():

    string = input(" ")
    
    contador = 0
    for i in string:
        contador += 1

    inicio = contador/2
    fim = contador
    new_string = string[(int(inicio + 0.5)):fim]

    print(new_string)



"""
    Leia um número da entrada e imprima todos os 10 primeiros múltiplos dele na mesma linha
"""
def q3():
    list = []

    number = int(input(''))

    for i in range(1 , 11):
        multiple = number * i

        list.append(multiple)
        
    for i in list:
        print( i , end=" ")


    

"""
    Escreva um programa que solicite ao usuário para digitar seu nome em letras
    minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula. Você
    não deve usar o método str.capitalize(). Preposições não devem ser iniadas com maiúsculo
    Exemplo: 
     - romulo junior - Romulo Junior
     - ze da manga - Ze da Manga
"""

def q4():
    name = input('')
    list_name = name.split()
    pos_space = []
    list_name_upper = []
    proibido_upper = ["dos" , "de" , "da" , "das"]

    for index , i in enumerate(name):
        if(i == " "):
            pos_space.append(index)

    for i in list_name:
        if(i in proibido_upper):
            preposicao  =  i
            list_name_upper.append(preposicao)
        else:
            new_string = ''
            tamanho = len(i)
            new_string = i[0].upper () + i[1:tamanho]
            list_name_upper.append(new_string)

    for index , i in enumerate(list_name_upper):        
        if(index == len(list_name_upper) - 1):
            print(i )
        else:
            print(i, end=" ")



"""
    Verificação de Triângulo: Peça ao usuário o comprimento de três lados em uma única entrada
    e verifique se eles podem formar um triângulo. 
    Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
    Exemplo:
        333: equilátero
        322: isosceles
        234: escaleno
"""
def q5():
    triangulo = input("")

    if(triangulo[0]  == triangulo[1] and triangulo[0] == triangulo[2]):
        print("equilátero")
    elif(triangulo[0]  != triangulo[1] and triangulo[0] != triangulo[2] and triangulo[1] != triangulo[2]):
        print("escaleno")
    else:
        print("isósceles")

#q3()
