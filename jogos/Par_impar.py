"""
NOME: Matheus Silva de Lima
TURMA: 360
Computação e Soluções de Problemas I.

Trabalho T2
Questão número 2

Escreva um programa que simule o jogo de Par ou Ímpar. Primeiramente, o jogador deve escolher
entre PAR ou IMPAR. Depois, o jogador que deve escolher um número entre 0 e 9. O computador
deve gerar um valor aleatório também entre 0 e 9. Então, o programa deve informar quais os valores
informados por cada um e deve informar qual foi o vencedor! Lembrar que deve-se controlar para
que o usuário não informe valores incorretos, caso isso ocorra, deve-se pedir um novo valor válido.
"""
print("NOME: Matheus Silva de Lima")
print("TURMA: 360")
print("\n")

#Escolha do par ou impar do usuario
x = False
while x == False:
	escolha = input("Escolha par ou impar: ").lower()
	if escolha != "par" and escolha != "impar":
		print("Digite par ou impar.")
	else: 
		x = True

#Escolha do numero
y = False
while y == False:
	num_usuario = int(input("Escolha um numero de 0 a 9: "))
	if num_usuario < 0 or num_usuario > 9:
		print("Digite um numero de 0 a 9: ")
	else:
		y = True

#Numero aleatorio da maquina
from random import randrange
num_maquina = randrange(0, 10)

print("\n")
print ("Seu numero escolhido foi", num_usuario, "e a maquina foi", num_maquina)

#Verificaçao se o usuario ganhou ou perdeu.
resultado = num_usuario + num_maquina
if resultado % 2 == 1:
	print("O resultado do jogo foi", resultado,  "= impar.")
	if escolha == "impar":
		print("Voce ganhou.")
	else:
		print("Voce escolheu par, você perdeu.")
elif resultado % 2 == 0:
	print("O resultado do jogo foi", resultado,"= par.")
	if escolha == "par":
		print("Voce ganhou.")
	else:
		print("Voce escolheu impar, você perdeu.")


