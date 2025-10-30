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

x = entrada - 2
if eh_primo(x) and x > 2:
    print(2 , x)
else:
    print(-1)