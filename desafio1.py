'''Cibele, Camila e Celeste são três irmãs inseparáveis. Estão sempre juntas e adoram fazer esportes, ler, cozinhar, jogar no computador... Agora estão aprendendo a programar computadores para desenvolverem seus próprios jogos.

Mas nada disso interessa para esta tarefa: estamos interessados apenas nas suas idades. Sabemos que Cibele nasceu antes de Camila e Celeste nasceu depois de Camila.

Dados três números inteiros indicando as idades das irmãs, escreva um programa para determinar a idade de Camila.'''




a = int(input())

b = int(input())

c = int(input())


lista = [a , b , c ]

lista_ordenada = sorted(lista)

print(lista_ordenada[1])
