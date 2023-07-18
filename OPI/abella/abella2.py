def permutacoes(digitos):
    if len(digitos) == 1:
        return [digitos]
    else:
        perms = []
        for i in range(len(digitos)):
            resto = digitos[:i] + digitos[i+1:]
            for p in permutacoes(resto):
                perms.append([digitos[i]] + p)
        return perms

def verifica_condicoes(d, a1, a2, a3, a4):
    s = str(d)
    count_4 = s.count('4')
    count_7 = s.count('7')
    count_47 = s.count('47')
    count_74 = s.count('74')
    return count_4 == a1 and count_7 == a2 and count_47 == a3 and count_74 == a4

def menor_numero_abella(a1, a2, a3, a4):
    digitos = ['4', '7']
    perms = permutacoes(digitos)
    for p in perms:
        num = int(''.join(p))
        if verifica_condicoes(num, a1, a2, a3, a4):
            return num
    return -1

# Teste do exemplo fornecido
a1, a2, a3, a4 = 1, 1, 1, 0
resultado = menor_numero_abella(a1, a2, a3, a4)
print(resultado)
