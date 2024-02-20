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
    
    if( idade == int(idade) and idade <= 150 and idade >= 0):
        return True
    else:
        return False

def validar_email(email):
    position_at = None
    position_dominio = None
    position_dns = email[-4::]
    for index , i in enumerate(email):
        if( i == "@"):
            position_at = index + 1
            position_dominio = email[position_at]
    
    if( "@" not in email):
        return False

    elif( position_dominio != " "  and  position_dominio != "." and position_dns == ".com"):
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
    numbers = ["0" , "1" ,"2" ,"3" , "4" ,"5" , "6" , "7" ,"8", "9"]

    for i in entrada:
        if(i == i.upper() and i != ' ' and i not in numbers):
            upper += 1

        if(i == i.lower() and i != ' ' and i not in numbers):
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


def min_custom(lista_numeros):
    min_number = None
    elements = 0

    for i in lista_numeros:
        elements += 1

    for index , i in enumerate(lista_numeros):
        if(elements >= 1):
            if(index < elements - 1):
                if(lista_numeros[index] < lista_numeros[index + 1]):
                    min_number = lista_numeros[index]
                else:
                    min_number = lista_numeros[elements - 1]
        
        return min_number

def startswith_custom(string , prefixo):
    elements = 0

    for i in prefixo:
        elements += 1

    if(string[0:elements] == prefixo):
        return True
    else:
        return False

def endswith_custom(string, sufixo):
    elements = 0

    for i in sufixo:
        elements -= 1

    if(string[elements::] == sufixo):
        return True
    else:
        return False   

def split_custom(string , caractere):
    lista = []
    inicio = 0
    fim = 0
    position_caractere = 0
    
    for index , i in enumerate(string):
        if( i == caractere):
            position_caractere = index + 1
            fim = index
            lista.append(string[inicio:fim])
            inicio += fim + 1
        
    
    lista.append(string[position_caractere:])
    return(lista)  

def strip_custom(string, caracteres_remover):
    word = ''
    for index , i in enumerate(string):
        if(i not in caracteres_remover):
            word += string[index] 
    return word

def replace_custom(string, substring_antiga, substring_nova):
    nova_string = ""
    i = 0

    while i < len(string):
        if string[i:i + len(substring_antiga)] == substring_antiga:
            nova_string += substring_nova
            i += len(substring_antiga)
        else:
            nova_string += string[i]
            i += 1

    return nova_string

def sum_list(*args):
    result = 0
    for i in args:
        result += i

    return result

def quantity_elements(*args):
    
    """ The function count the elements parametrize

    Args:
        *args : this is all elements parametrize

    Returns:
        int : return a quantity of elements in the list
    
    
    """

    quantity = 0
    for i in args:
        quantity += 1
    return quantity

def test_scope_function():
    temperatura = 30
    def ligar_ar():
        temperatura = 20

    ligar_ar()
    print(temperatura)

def use_filter(*args):
    return filter( lambda args : args % 2 == 0 , args)


def use_uppers(*args)
    uppers = map(lambda x: x[0].upper() + x[1::], args)
    print(list(uppers)) 


def use_global():
    temperatura = 30
    def ligar_ar():
        global temperatura
        temperatura = 20

    ligar_ar()
    print(temperatura)

