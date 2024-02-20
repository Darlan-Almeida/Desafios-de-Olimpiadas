# Escreva um programa que solicite ao usuário o seu nome e a sua idade, armazenando esses valores em variáveis. Em seguida, imprima uma mensagem formatada mostrando o nome e a idade do usuário.

def print_age_and_name():
    name = input("submit your first name: ")
    age = int(input("How old are you? "))
    
    print(name , "is" , age , "old")

print_age_and_name()


# Escreva um programa que solicite ao usuário dois números inteiros e armazene-os em variáveis. Em seguida, calcule e imprima a soma, subtração, multiplicação e divisão desses números.


def operations():
    number1 = int(input("Submit the first number: "))
    number2 = int(input("Submit the second number: "))

    sum = number1 + number2
    subrtaction = number1 - number2
    divison = number1/ number2
    multiplication = number1 * number2


    print("The sum of these numbers is", sum)
    print("The subrtaction of these numbers is", subrtaction)
    print("The divison of these numbers is", divison)
    print("The multiplication of these numbers is", multiplication)


operations()

'''
Escreva um programa que solicite ao usuário o raio de um círculo e calcule a área
 e o perímetro desse círculo. Imprima os resultados formatados.'''


def circle():
    pi = 3.1415
    radius = float(input("submit the radius size of circle in cm: "))
    area = pi * radius ** 2
    perimeter = pi * (radius * 2)
    print("the area is" , area , "CM" )
    print("the perimeter is" , perimeter , "CM" )


circle()


#Escreva um programa que solicite ao usuário uma temperatura em graus Celsius e converta-a para Fahrenheit. Imprima o resultado formatado.


def celsius_to_farhenheit():
    celsius = float(input("send the temperature in celsius scale: "))
    farhenheit = (celsius * 9/5) + 32
    print("The temperature in scale celsius to transform in farhenheit is" , farhenheit)

celsius_to_farhenheit()


#Escreva um programa que solicite ao usuário o seu salário mensal e o número de meses trabalhados no ano. Calcule e imprima o salário anual.

def salary():
    salary_month = float(input("How much is your salary month?"))
    month = int(input("How much moth your worked?"))
    salary_years = salary_month * month
    print("Your years salary is" , salary_years)


salary()

#Escreva um programa que solicite ao usuário um número e verifique se ele é par ou ímpar. Imprima uma mensagem informando o resultado.
def par_or_impar():
    number = int(input("send a number: "))
    rest = number % 2

    if(rest != 0):
        print("this number is impar")

    else:
        print("this number is par")

'''Escreva um programa que solicite ao usuário dois valores booleanos (True ou False) e armazene-os em variáveis.
 Em seguida, aplique os operadores lógicos "and", "or" e "not" entre essas variáveis e imprima os resultados.'''
def boolean():
    value1 = int(input("send True(1) or False(0): "))
    value2 = int(input("send True(1) or False(0): "))

    value1_parse_boll = bool(value1)
    value2_parse_boll = bool(value2)

    conjuntion = value1_parse_boll and value2_parse_boll
    disjuncion = value1_parse_boll or value2_parse_boll
    negation = not value1_parse_boll
    negation2 = not value2_parse_boll

    print("conjuntion:" , conjuntion)
    print("disjuntion:" , disjuncion)
    print("negation value1:" , negation)
    print("negation value2:" , negation2)


boolean()


def sentences():
    sentence1 = input("send a senteces")
    sentence2 = input("send other senteces")

    if(sentence1 == sentence2):
        print("the sentences are equal")

    else:
        print("the sentences are not equal")

'''Escreva um programa que solicite ao usuário dois números e verifique se o primeiro
 número é maior que o segundo. Imprima uma mensagem informando o resultado da comparação.'''

sentences()

def numbers_comparations():
    number1 = float(input("send the first number: "))
    number2 = float(input("send the second number: "))

    if(number1 > number2):
        print("The first number is max betwenn two")
    
    elif(number1 == number2):
        print("The numbers are equals")

    else:
        print("the second number is max betwenn two")


'''Escreva um programa que solicite ao usuário a sua idade e 
verifique se ele é maior de idade (idade igual ou superior a 18 anos). 
Imprima uma mensagem informando o resultado.'''

numbers_comparations()

def age():
    age = int(input("How age are you?"))

    if(age >= 18):
        print("Your is adult")

    else:
        print("Your is not adult")

age()

'''
Escreva um programa em Python que solicite ao usuário
dois números inteiros e troque os valores das variáveis. Em seguida, imprima os valores atualizados.'''

def permutation():
    number1 = int(input("send the first name:"))
    number2 = int(input("send the second name"))

    number1 , number2 = number2 , number1

    print("The first number now is", number1)
    print("The second number now is", number2)

permutation()

'''
Um foguete atinge uma velocidade constante de 1500 m/s. 
Se ele leva 40 segundos para atingir essa velocidade,
qual é a altitude máxima que o foguete alcançará?'''

def foguete():
    velocity = 1500
    time = 40
    altitude = velocity * time

    print("The max altitude alcanced is" , altitude , "m")

'''Um sistema de foguete opera em Celsius, mas você precisa fornecer a temperatura em Fahrenheit.
 Dada a fórmula de conversão: Fahrenheit = (Celsius * 9/5) + 32, 
 converta uma temperatura de 25°C para Fahrenheit. '''

foguete()

def foguete_celsius_to_Fahrenheit():
    celsius = 25
    farhenheit = (celsius * 9/5) + 32
    print("The temperature in scale celsius to transform in farhenheit is" , farhenheit)

foguete_celsius_to_Fahrenheit()

'''Escreva um programa que dado um dia, mes e ano calcule o valor em termos de UNIX Epoch﻿ Time (o número de milessegundos desde 00:00 de 01 de Janeiro de 1970).

a) Considere que todos os anos possuem 365 dias
b) Considere os anos bissextos'''
def calc_miliseconds():
    
    milisecond = 1000
    second = 60
    minutes = 60
    hour = 24
    day_years = 365
    day_years_bissext = 366

    years_now = 1970

    years_bissext = 0

    years = 0

    day_input = int(input("send the day: "))
    month_input = int(input("send the month: "))
    years_input = int(input("send the years: "))

    array = range(years_now, years_input)

    for i in array:
        if(i % 4 == 0):
            years_bissext += 1
        else:
            years += 1

    result = ((years_bissext *  day_years_bissext * hour * minutes * second * milisecond) + (years * day_years * hour * minutes * second * milisecond)) + (day_input * hour * minutes * second * milisecond) + (month_input* 30 * hour * minutes * second * milisecond)
    print(result, "milisecond")
    
calc_miliseconds()

