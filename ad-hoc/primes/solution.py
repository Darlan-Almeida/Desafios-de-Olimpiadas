entrada = int(input())

def eh_primo(n):
    i = 3
    while True:
        if i > n**1/2:
            return True
        elif n % i == 0:
            return False

        i += 2
    return False
        
if eh_primo(entrada - 2):
    print(2 , entrada - 2)
else:
    print(-1)