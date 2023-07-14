n = 333
tam = len(str(n))*'1'
dim = n
while True:
    dim = dim-int(tam)
    if dim == 11 or dim == 0:
        print("YES")
        break
    elif dim < 11:
        print("NO")
        break
    tam = len(str(dim))*'1'
  