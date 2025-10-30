entrada = input()

nebuloso = {'a' , 'e' , 'i' , 'o' , 'u', '1' , '3' , '5' , '7' , '9'}

qtd = 0

for i in entrada:
    if i in nebuloso:
        qtd += 1

print(qtd)