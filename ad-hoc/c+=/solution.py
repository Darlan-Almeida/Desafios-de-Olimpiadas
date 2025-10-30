t = int(input())

while t > 0:
    t -= 1
    a , b  ,c = map(int , input().split())
    if a > c or b > c:
        print(0)
    else:
        fator_soma = 0
        
        if a > b:
            b += a
            fator_soma = b
        else:
            a += b
            fator_soma = a
        
        qtd = 1
    
        while max(a , b) <= c:
            if max(a,b) == a:
                b += a
            else:
                a += b

            qtd += 1
            
        print(qtd)