


def calc_emprestimo():
  cesta = 0
  custo_pamonha = int(input())
  saldo = int(input())
  quantidade_pamonha = int(input())

  for i in range(0,quantidade_pamonha+1):
    valor_compra = i  * custo_pamonha
    cesta += valor_compra

  emprestimo = cesta - saldo

  
  if(emprestimo > 0):
    emprestimo = emprestimo

  else:
    emprestimo = 0


  return(emprestimo)

print(calc_emprestimo())