import random, time


#Verificar se a jogada do user foi válida.
def avaliar_jogada(jogada):
	lista_jogadas_possiveis = ["pedra", "Pedra", "tesoura", "Tesoura", "Papel", "papel"]
	if jogada not in lista_jogadas_possiveis:
		print("\t Jogada inválida, por favor tente novamente.")
		return 0
	return 1
def verificar_resultado(jogada_cpu, jogada_player):
	pedra = ["Pedra", "pedra"]
	papel = ["Papel", "papel"]
	tesoura = ["Tesoura", "tesoura"]

	if(jogada_cpu in pedra):
		if(jogada_player in pedra):
			return -1 #Empate
		if(jogada_player in tesoura):
			return 1 #Win_CPU
		else:
			return 0 #Win_Player
	if(jogada_cpu in papel):
		if(jogada_player in pedra):
			return 1 #Win_CPU
		if(jogada_player in tesoura):
			return 0 #Win_Player
		else:
			return -1 #Empate
	if(jogada_cpu in tesoura):
		if(jogada_player in pedra):
			return 0 #Win_Player
		if(jogada_player in tesoura):
			return -1 #Empate
		else:
			return 1 #Win_CPU

def empate(jogadas_completas, win_cpu, win_player, jogadas_cpu):

	opcao_invalida = 0
	print("\n\t Rodada #"+str(jogadas_completas) + "  Pontuação: Player("+str(win_player)+") vs CPU("+str(win_cpu)+")")
	escolha_cpu_numero = random.randint(0,2) #Gerar random jogada
	jogada_cpu = jogadas_cpu[escolha_cpu_numero] #Jogada
	
	while(not opcao_invalida):
		jogada_player = input("\n\t Insira a sua jogada: ")
		opcao_invalida = avaliar_jogada(jogada_player)
				
		winner = verificar_resultado(jogada_cpu, jogada_player)

		print("\n\t O computador está a fazer a sua jogada...")
		time.sleep(3)
		print("\t O computador jogou... " + jogadas_cpu[escolha_cpu_numero])
			
		if(winner == 1): #Win_CPU
			print("\t O computador ganhou o jogo!")
			win_cpu += 1
		elif(winner == 0): #Win_CPU
			print("\t Ganhaste o jogo!")
			win_player += 1
		elif(winner == -1):
			print("\t Empataram novamente! Queres jogar outra rodada decisiva? (S/N):")
			decisao = input()
			if(decisao == "S" or decisao == "s"):
				empate(jogadas_completas+1, win_cpu, win_player, jogadas_cpu)
			elif(decisao == "N" or decisao == "n"):
				return

def main():
	#Menu e primeiras variáveis
	print("\n\t   Bem Vindo ao Jogo Pedra-Papel-Tesoura\t\n")
	print("\n\t Neste jogo vais jogar contra o computador\t\n")
	print("\n\n\t\t\t Boa sorte \t\t\n")
	print("\n\n")


	nome = input("\tInsere o teu nome: ")
	numero_jogadas = int(input("\tInsere o numero de jogadas: "))

	jogadas_cpu = ["Pedra", "Papel", "Tesoura"]
	print("\n\n\t Olá " + nome + ", vais jogar " + str(numero_jogadas) + " rondas contra o computador. Boa sorte\n\n")

	#contadores de vitorias
	win_player = 0
	win_cpu = 0

	jogadas_completas = 1 #track do numero de rondas já feitas
	#Jogo
	time.sleep(1)
	while(jogadas_completas < numero_jogadas+1):
		opcao_invalida = 0
		print("\n\t RODADA #"+str(jogadas_completas) + "  Pontuação: Player("+str(win_player)+") vs CPU("+str(win_cpu)+")")
		escolha_cpu_numero = random.randint(0,2) #Gerar random jogada
		jogada_cpu = jogadas_cpu[escolha_cpu_numero] #Jogada
		while(not opcao_invalida):
			jogada_player = input("\n\t Insira a sua jogada: ")
			opcao_invalida = avaliar_jogada(jogada_player)
			
		winner = verificar_resultado(jogada_cpu, jogada_player)
		print("\n\t O computador está a fazer a sua jogada...")
		time.sleep(3)
		print("\t O computador jogou... " + jogadas_cpu[escolha_cpu_numero])
		
		if(winner == 1): #Win_CPU
			print("\t O computador ganhou esta rodada!")
			win_cpu += 1
		elif(winner == 0): #Win_CPU
			print("\t Ganhaste esta rodada!")
			win_player += 1
		elif(winner == -1):
			print("\t Empataram esta rodada!")
		jogadas_completas += 1


	print("\n\n\t\t PONTUAÇÃO FINAL \n\n \t\t" + nome + ": "+str(win_player) +" vitória(s)\n\t\t CPU: "+str(win_cpu)+" vitoria(s)\n\n")

	if(win_cpu > win_player):
		print("\n\t O computador ganhou o jogo! Boa sorte para a próxima.")
	elif(win_player > win_cpu):
		print("\n\t Parabéns "+nome+" ganhaste o jogo!")
	elif(win_player == win_cpu):
		print("\n\t Empataram o jogo! Queres jogar a última jogada para decidir o vencedor? (S/N): ", end = "")
		decisao = input()
		if(decisao == "S" or decisao == "s"):
			empate(jogadas_completas, win_cpu, win_player, jogadas_cpu)
		elif(decisao == "N" or decisao == "n"):
			print("\n\t Empate confirmado!")
	print("\n\t Obrigado por jogares!")

if __name__ == '__main__':
	main()