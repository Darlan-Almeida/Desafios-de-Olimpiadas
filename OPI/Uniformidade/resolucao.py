palavra = str(input())

letras = list(palavra)

maiusculas = 0

minusculas = 0

for i in letras:
    if(i == i.upper()):
        maiusculas += 1
    else:
        minusculas += 1

if(maiusculas > minusculas):
    print(palavra.upper())

else:
    print(palavra.lower())
