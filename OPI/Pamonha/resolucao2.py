# Função para calcular a quantidade de reais que Abraão precisará pegar emprestado
def calcular_emprestimo(k, n, w):
    valor_total = (w * (w + 1) / 2) * k  # Calcula o valor total das pamonhas
    emprestimo = max(0, valor_total - n)  # Calcula a diferença entre o valor total e o dinheiro que Abraão possui
    return emprestimo


k = int(input("Digite o custo da pamonha (k): "))
n = int(input("Digite a quantidade de dinheiro que Abraão possui (n): "))
w = int(input("Digite a quantidade de pamonhas que Abraão deseja comprar (w): "))
    
emprestimo = calcular_emprestimo(k, n, w) 
print("Abraão precisará pegar emprestado", emprestimo, "reais dos seus pais.")
