"""
NOME: Matheus Silva de Lima
TURMA: 360
Computação e Soluções de Problemas I.

Trabalho T2
Questão número 1

Escreva um programa que simule um jogo de adivinhação de números. O computador escolhe um
número aleatório entre 1 e 30, e o jogador (usuário) tem até 5 chances de acertar o número escolhido
pelo computador. Se o jogador informar um valor incorreto (fora dos limites pedidos), deve-se pedir
outro número, repetidamente, até que o jogador informe um valor correto, o qual contará como uma
jogada válida. O programa deve informar se o jogador ganhou, ou após 5 tentativas, informar que o
jogador perdeu e mostrar qual era o valor sorteado.
"""
print("NOME: Matheus Silva de Lima")
print("TURMA: 360")

#A maquina criara um numero aleatorio.
from random import randrange
num_random = randrange(1, 31)

tentativa = 5    #O numero de tentativas máximas é 5.
while tentativa > 0:    
	tentativa = tentativa - 1
	print("\n")
	num = int(input("Digite um número de 1 a 30: "))
	print("Você escolheu o número:", num)
	if num <= 0 or num > 30 and tentativa != 0:     #Validação do numero digitado pelo usuario. Se for a ultima tentativa nao printa.
		print("Digite um número válido de 1 a 30. Você tem mais", tentativa, "tentativas.") 
	else:
		if num_random == num:    #Se o numero for igual ao aleatorio, o usuario ganhou.
			tentativa = 0        #Sai do while
			print("\n")		
			print("Parabéns, você ganhou o jogo!")
		elif num_random != num:  # Se o numero for diferente, ele irá repetir o while até a ultima tentativa.
			if tentativa == 0:
				print("\n")        
				print("Você perdeu o jogo.") 
			else:
				print("\n")
				print("Tente novamente. Você tem mais", tentativa, "tentativas.")   
		
print("O número sorteado foi:", num_random)





