n = 2
a = "1 1"
b = "3 2"

op_a = a.split()
op_a = int(op_a[0]) - int(op_a[1])

op_b = b.split()
op_b = int(op_b[0]) - int(op_b[1])

if op_a < op_b:
    print("YES")
else:
    print("NO")

