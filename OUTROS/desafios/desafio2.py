'''
1. Escreva um programa que solicita um número ao usuário e determina se é positivo, negativo ou zero. 
2. Verificação de Número Par/Ímpar: Crie um programa que pede ao usuário um número e verifica se ele é par ou ímpar.
3. Calculadora Simples: Faça uma calculadora que pede ao usuário dois números e uma operação (+, -, *, /) e retorna o resultado dessa operação.
4. Maior de Três Números: Escreva um programa que solicita três números ao usuário e retorna o maior dentre eles.
5. Classificação de Idade: Peça a idade do usuário e classifique-a em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).
6. Verificação de Triângulo: Peça ao usuário o comprimento de três lados e verifique se eles podem formar um triângulo. Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
7. Conversão de Notas: Escreva um programa que converte uma nota de 0 a 100 em uma escala de conceitos: A (90-100), B (80-89), C (70-79), D (60-69) e F (0-59).
8. Validação de Login: Crie um programa que pede ao usuário um nome de usuário e uma senha. Se o nome de usuário for "admin" e a senha for "12345", exiba "Acesso concedido", caso contrário, exiba "Acesso negado".
9. Calculadora de IMC: Peça ao usuário seu peso e altura e calcule o índice de massa corporal (IMC). Em seguida, mostre uma mensagem indicando se a pessoa está abaixo do peso, com peso normal, com sobrepeso, obesa ou muito obesa.
10. Verificação de Ano Bissexto: Escreva um programa que verifica se um ano fornecido pelo usuário é bissexto ou não.'''

# question 1

def question1():
    number = float(input("send a number: "))

    if( number > 0):
        print("This number is positive")
    elif(number < 0):
        print("This number is negative")
    else:
        print("This number is zero")


def question2():
    number = float(input("send a number: "))

    if( number % 2 == 0):
        print("This number is even")
    else:
        print("This number is odd")


def question3():
    number1 = float(input("send a number: "))
    number2 = float(input("send other number"))
    operations = input("Whats operation you will perform: '+' , '-' , '*' or '/' ")

    if( operations == "+"):
        sum = number1 + number2
        print("This sum of the numbers is:" , sum)
    elif(operations == "-"):
        subtration = number1 - number2
        print("This subtration of the numbers is:" , subtration)
    elif(operations == "*"):
        multiplication = number1 * number2
        print("This multiplication of the numbers is:" , multiplication)
    elif(operations == "/"):
        divison= number1 / number2
        print("This divison of the numbers is:" , divison)
    else:
        print("Select only avaliable operations")


def question4():
    number1 = float(input("send the first number: "))
    number2 = float(input("send the second number: "))
    number3 = float(input("send the third number: "))

    if(number1 > number2 and number1 > number3):
        print("The first number is the biggest on the list")
    elif(number2 > number1 and number2 > number3):
        print("The second number is the biggest on the list")
    else:
        print("The third nimber is the biggest on the list")
    
#5. Classificação de Idade: Peça a idade do usuário e classifique-a em "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).


def question5():
    age = int(input("Send your age:"))

    if(age <= 12):
        print("You are a Child")
    elif( age > 12 and age <= 19):
        print("you are a teenager")
    elif( age > 19 and age < 60):
        print("you are a adult")
    else:
        print("you are elderly")

# 6.Peça ao usuário o comprimento de três lados e verifique se eles podem formar um triângulo. Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.

def question6():
    side1 = float(input("Send the first side of the triangule: "))
    side2 = float(input("Send the second side of the triangule: "))
    side3 = float(input("Send the third side of the triangule: "))

    if( side1 > 0 and side2 > 0 and side3 > 0):
        print("This is not a triangule")

    elif( side1 == side2 and side1 == side3):
        print("This triangule is equilateral")

    elif( side1 != side2 and side1 != side3 and side2 != side3):
        print("This triangule is isoceles")

# 7.Escreva um programa que converte uma nota de 0 a 100 em uma escala de conceitos: A (90-100), B (80-89), C (70-79), D (60-69) e F (0-59).

def question7():
    score = float(input("Send the score: "))

    if( score >= 90 ):
        print("This score is scale A")

    elif( score < 90 and score >= 80 ):
        print("This score is scale B")

    elif( score < 80 and score >= 70  ):
        print("This score is scale C")

    elif( score < 70 and score >= 60  ):
        print("This score is scale D")

    else:
        print("This score is scale F")

#Validação de Login: Crie um programa que pede ao usuário um nome de usuário e uma senha. Se o nome de usuário for "admin" e a senha for "12345", exiba "Acesso concedido", caso contrário, exiba "Acesso negado".

def question8():
    login = input("Send the user login: ")
    password = input("Send the password: ")

    if(login == 'admin' and password == '12345'):
        print("Acess sucessfully")
    else:
        print("Acess failde. Verify your login user or your password, It is incorrect")


def question9():
    Weight = float(input("Send the weight: "))
    height = float(input("Send the height: "))

    imc = weight / height * height

# Calculadora de IMC: Peça ao usuário seu peso e altura e calcule o índice de massa corporal (IMC). Em seguida, mostre uma mensagem indicando se a pessoa está abaixo do peso, com peso normal, com sobrepeso, obesa ou muito obesa.

    if imc <= 18.5:
        print("Your IMC is underweight")

    elif imc > 18.5 and imc <= 24.9:
        print("Your IMC is ideal")
    
    elif imc > 24.9 and imc <= 29.9:
        print("yor IMC is a little higher")
    
    elif imc > 29.9 and  imc <= 34.9:
        print("your IMC is obesity 1")

    elif imc > 34.9 and imc <= 39.9:
        print("your IMC is severe obesity")

    else:
        print("your IMC is morbid obesity")


def question10():
    years = int(input("Send the years: "))

    if( years % 4 == 0 and years % 100 == 0 and years % 400 == 0):
        print("This years is  bissext")

    elif( years % 4 == 0 and years % 100 != 0 and years % 400 != 0):
        print("This years is  bissext")

    else:
        print("This years not is bissext")


question1()
question2()
question3()
question4()
question5()
question6()
question7()
question8()
question9()
question10()
