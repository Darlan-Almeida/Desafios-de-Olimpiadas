# A. Do Not Be Distracted!

t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    cadeia = input()

    letras = set()
    letras.add(cadeia[0])

    result = "YES"
    for i in range(1 , n):
        if cadeia[i] in letras and cadeia[i-1] != cadeia[i]:
            result = "NO"
            break
        letras.add(cadeia[i])

    
    print(result)