"""
NOME: Matheus Silva de Lima
TURMA: 360
Computação e Soluções de Problemas I.

Trabalho T2
Questão número 3.

Escreva um programa que implemente o Jogo "Vinte e Um" (Blackjack). Neste jogo, são sorteados:
a. Três cartas para o computador;
b. Duas cartas + 1 carta opcional para o jogador. Por exemplo, o jogo informa quais são as cartas do
   jogador e a soma das 2 cartas obrigatórias, e o jogador escolhe se pretende ter uma 3ª carta ou
   não. Em caso positivo, o seu valor total será a soma das 3 cartas.
   No Blackjack, os dez, valetes, damas e reis têm o valor de dez cada um. Na regra original, os "Áses"
   podem ter dois valores diferentes, tanto um como onze (você poderia escolher qual o melhor).
   Mas para facilitar a implementação, aqui o valor sorteado terá um valor fixo. Desta forma, os
   valores válidos sorteados são de 1 a 11.
   O objetivo do jogo é somar 21. Se o jogador exceder 21, perde o jogo. Caso contrário, quem se
   aproximar mais de 21 ganha o jogo (se o computador exceder 21, o jogador ganha), sendo que
   em caso de empate entre o jogador e o computador, o jogador perde.
"""
print("NOME: Matheus Silva de Lima")
print("TURMA: 360")
print("\n")

from random import randrange

#Valores sorteados para o computador
num_maq1 = randrange(1, 12)
num_maq2 = randrange(1, 12)
num_maq3 = randrange(1, 12)
numeros_maq = num_maq1, num_maq2, num_maq3  #Verificacao dos numeros sorteados
soma_maq = num_maq1 + num_maq2 + num_maq3   #Soma dos valores encontrados
print("Os numeros da maquina são:", numeros_maq) 
print("A soma da maquina é:", soma_maq) 

#Valores sorteados para o usuario
num_usuario1 = randrange(1, 12)
num_usuario2 = randrange(1, 12)
numeros_usuario = num_usuario1, num_usuario2   #Verificacao dos numeros sorteados
soma_usuario = num_usuario1 + num_usuario2     #Soma dos valores encontrados
print("Os seus numeros são:", numeros_usuario) 
print("A sua soma é:", soma_usuario) 

#Pergunta da carta opcional
escolha = input("Deseja escolher uma carta opcional? (sim ou nao) ").lower()
if escolha == "sim":
	num_usuario3 = randrange(1, 12)
	print("O seu novo numero é:", num_usuario3)
	soma_usuario = soma_usuario + num_usuario3
	print("A sua nova soma é:", soma_usuario)
elif escolha == "nao":
	print("Sua soma final é:", soma_usuario)

#Verificação do usuario
if soma_usuario == 21:
	print("Parabens! Voce marcou 21 ganhou o jogo.")
elif soma_maq == 21:
	print("Voce perdeu o jogo, a maquina marcou 21 e ganhou.")		
elif soma_usuario > 21:
	print("Voce perdeu o jogo, ultrapassou 21.")
elif soma_maq > 21:
	print("Parabens! Voce ganhou o jogo, a maquina ultrapassou 21.")
elif soma_maq == soma_usuario:
	print("Empate: Voce perdeu o jogo.")	
elif 21 - soma_maq > 21 - soma_usuario:
	print("Parabens! Voce venceu por estar mais perto de 21. ")
else:
	print("Voce perdeu! A maquina venceu por estar mais perto de 21.")









    


		



         