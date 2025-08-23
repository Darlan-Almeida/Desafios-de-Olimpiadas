entrada = input()
n , m = entrada.split()
n = int(n)
m = int(m)
contador = 0

while n >= 1 and m >= 1:
    if not ((n == 1 and m == 0) or ( m == 1 and n == 0)):
        contador += 1
    n -= 1
    m -= 1
    
if contador % 2 != 0:
    print("Akshat")
else:
    print("Malvika")
