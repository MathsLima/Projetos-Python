
def inicia_tabuleiro():
	tabuleiro = [
		" ", " ", " ", 
		" ", " ", " ",     
		" ", " ", " "
	]

	return tabuleiro


def apresenta_tabuleiro(tabuleiro):
	print(tabuleiro[0], '|', tabuleiro[1], '|', tabuleiro[2])
	print('-' * 9)
	print(tabuleiro[3], '|', tabuleiro[4], '|', tabuleiro[5])     
	print('-' * 9)
	print(tabuleiro[6], '|', tabuleiro[7], '|', tabuleiro[8])


def le_jogada(jogador):
	mensagem = jogador + ", digite um número de 0 a 8 para indicar em qual posição você deseja jogar: "    
	posicao = int(input(mensagem))

	return posicao


def realiza_jogada(tabuleiro, jogador, posicao):
	if (jogador == "jogador1"):
		simbolo = "X"
	else:
		simbolo = "O"           

	tabuleiro[posicao] = simbolo
	apresenta_tabuleiro(tabuleiro)


def verifica_tabuleiro(tabuleiro):
	# Jogador 1
	if (
		
		(tabuleiro[0] == "X" and tabuleiro[1] == "X" and tabuleiro[2] == "X") or
		(tabuleiro[3] == "X" and tabuleiro[4] == "X" and tabuleiro[5] == "X") or
		(tabuleiro[6] == "X" and tabuleiro[7] == "X" and tabuleiro[8] == "X") or

		
		(tabuleiro[0] == "X" and tabuleiro[3] == "X" and tabuleiro[6] == "X") or
		(tabuleiro[1] == "X" and tabuleiro[4] == "X" and tabuleiro[7] == "X") or
		(tabuleiro[2] == "X" and tabuleiro[5] == "X" and tabuleiro[8] == "X") or

		
		(tabuleiro[0] == "X" and tabuleiro[4] == "X" and tabuleiro[8] == "X") or         
		(tabuleiro[6] == "X" and tabuleiro[4] == "X" and tabuleiro[2] == "X")
	):
		return 1

	# Jogador 2
	elif (
		
		(tabuleiro[0] == "O" and tabuleiro[1] == "O" and tabuleiro[2] == "O") or	
		(tabuleiro[3] == "O" and tabuleiro[4] == "O" and tabuleiro[5] == "O") or	
		(tabuleiro[6] == "O" and tabuleiro[7] == "O" and tabuleiro[8] == "O") or	

		
		(tabuleiro[0] == "O" and tabuleiro[3] == "O" and tabuleiro[6] == "O") or	
		(tabuleiro[1] == "O" and tabuleiro[4] == "O" and tabuleiro[7] == "O") or	
		(tabuleiro[2] == "O" and tabuleiro[5] == "O" and tabuleiro[8] == "O") or	

		
		(tabuleiro[0] == "O" and tabuleiro[4] == "O" and tabuleiro[8] == "O") or	
		(tabuleiro[6] == "O" and tabuleiro[4] == "O" and tabuleiro[2] == "O")	   
	):
		return 2



print("Posições do tabuleiro")
print(" 0 | 1 | 2 ")
print('-' * 9)
print(" 3 | 4 | 5 ")
print('-' * 9)
print(" 6 | 7 | 8 ")
print("\n")

print("Jogo")
tabuleiro = inicia_tabuleiro()
apresenta_tabuleiro(tabuleiro)
jogador1 = input("Qual o nome do primeiro jogador? ")
jogador2 = input("Qual o nome do segundo jogador? ")



i = 0

while i < 9:                         
	i = i + 1                                       
	
	if i % 2 != 0:
		posicao = le_jogada(jogador1)
		realiza_jogada(tabuleiro, "jogador1", posicao)
	else:
		posicao = le_jogada(jogador2)
		realiza_jogada(tabuleiro, "jogador2", posicao)

	verificador = verifica_tabuleiro(tabuleiro)                             
	if (verificador == 1):
		print("Parabéns ", jogador1, " ganhou o jogo!!!!")
		i = 9
	elif (verificador == 2):
		print("Parabéns ", jogador2, " ganhou o jogo!!!!")
		i = 9
	elif (verificador != 1 and verificador != 2 and i == 9):
		print("O jogo empatou!")


