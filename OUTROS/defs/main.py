def saudacao(nome):
    response = f"Olá, {nome}!"
    return response

def dobro(numero):
    result = numero * 2
    return result

def saudacao_personalizada(nome, idioma):
    

    if(idioma == "inglês"):
        return f"Hello, {nome}!"

    elif( idioma == "espanhol"):
        return f"Hola, {nome}!"
    
    else:
        return f"Bonjour, {nome}!"


def  potencia(base, expoente):
    result = base ** expoente

    return result

def idade_valida(idade):
    
    if( idade == int(idade) and idade <= 150 and idade > 0):
        return True
    else:
        return False

def validar_email(email):
    position_at = None
    for index , i in enumerate(email):
        if( i == "@"):
            position_at = index + 1
            
    domain= email[position_at:]

    if(domain == "email.com"):
        return True
    else:
        return False

def calcular_pagamento(horas_trabalhadas , taxa_hora):
    salary = horas_trabalhadas * taxa_hora

    return salary


def maior_numero(a , b , c):
    array = [a , b , c]
    more = 0
    elements = 0

    for i in array:
        elements += 1

    for index , i in enumerate(array):
        if(index < elements - 1):
            if( array[index] > array[index + 1]):
                more =  array[index]

            else:
                more = array[elements - 1]

    return more


def contagem_letras(entrada):
    upper = 0
    lower = 0

    for i in entrada:
        if(i == i.upper()):
            upper += 1

        else:
            lower += 1
    return upper , lower


def len_custom(iteravel):
    elements = 0

    for i in iteravel:
        elements += 1

    return elements

def sum_custom(lista_numeros):
    result = 0

    for i in lista_numeros:
        result += i

    return result

def max_custom(lista_numeros):
    more = None
    elements = 0

    for i in lista_numeros:
        elements += 1
        

    for index , i in enumerate(lista_numeros):
        if(elements >= 1):
            if(index < elements - 1):
                if( lista_numeros[index] > lista_numeros[index + 1]):
                    more =  lista_numeros[index]

                else:
                    more = lista_numeros[elements - 1]

        return more

