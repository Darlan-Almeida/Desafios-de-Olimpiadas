entrada = input().split()

def eh_palindromo(n):
    for i in range(int(len(n)/2)):
        if n[i] != n[len(n)-i-1]:
            return False
    return True

p = 0
for i in range(int(entrada[0]) , int(entrada[1])+1):
    if eh_palindromo(str(i)):
        p += 1
print(p)