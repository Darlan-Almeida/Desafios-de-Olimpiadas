'''A prefeitura contratou um novo professor para ensinar as crianças do bairro a jogar tênis na quadra de tênis do parque municipal. O professor convidou todas as crianças do bairro interessadas em aprender a jogar tênis. Ao final do primeiro mês de aulas e treinamentos foi organizado um torneio em que cada participante disputou exatamente seis jogos. O professor vai usar o desempenho no torneio para separar as crianças em três grupos, de forma a ter grupos de treino em que os participantes tenham habilidades mais ou menos iguais, usando o seguinte critério:

participantes que venceram 5 ou 6 jogos serão colocados no Grupo 1;
participantes que venceram 3 ou 4 jogos serão colocados no Grupo 2;
participantes que venceram 1 ou 2 jogos serão colocados no Grupo 3;
participantes que não venceram nenhum jogo não serão convidados a continuar com os treinamentos.
Dada uma lista com o resultado dos jogos de um participante, escreva um programa para determinar em qual grupo ele será colocado.
Entrada
A entrada consiste de seis linhas, cada linha indicando o resultado de um jogo do participante. Cada linha contém um único caractere: V se o participante venceu o jogo, ou P se o jogador perdeu o jogo. Não há empates nos jogos.
Saída
Seu programa deve produzir uma única linha na saída, contendo um único inteiro, identificando o grupo em que o participante será colocado. Se o participante não for colocado em nenhum dos três grupos seu programa deve imprimir o valor -1.
Exemplos
Entrada
V
V
P
P
P
V
Saída
2

Entrada
P
P
P
P
P
P
Saída
-1
'''

contador = 0
partidas = []

for i in range(0 , 6):
    partida = str(input())
    partidas.append(partida)



for i in partidas:
    if(i in "v"):
        contador = contador + 1


if(contador == 5 or contador == 6):
    print("1")
    
    
if(contador == 4 or contador == 3):
    print("2")
    
    
    
if(contador == 2 or contador == 1):
    print("3")
    
    
if( contador == 0):
    print("-1")
