from random import choice
vocabulario=["memoria", "discorigido", "processador", "computador", "monitor", "teclado"]
class bv:
    fome=0
    energia=100
def alimentar():
    bv.fome=bv.fome+25
    bv.energia=bv.energia-10
    return bv.fome
    return bv.energia
def dormir(nome):
    for i in range(101):
        print(f"{nome} esta dormindo...{i}%")
    bv.energia=100
    condicao = int(input(f" DESEJA [1]ACORDAR {nome} :) OU [2]DEIXAR {nome} DORMINDO? (U-u..Zzz) "))
    if (condicao == 1):
        print(f"{nome} ACABOU DE ACORDAR :) ")
    if (condicao == 2):
        print("Volte daqui a pouco...Até logo! (U-u..Zzz)")
        exit()
def brincar():
    bv.energia = 50
    bv.fome=0
    condicao = int(input(f"ESOLHA UMA BRINCADEIRA: [1]JOGO DA FORCA"))
    if (condicao == 1):
        vocabulario=["memoria", "discorigido", "processador", "computador", "monitor", "teclado"]
    palavra = choice(vocabulario)
    print("JOGO DA FORCA\n")
    print("Bem vindo ao JOGO DA FORCA. Boa sorte! TEMA TECNOLOGIA\n")
    chances = 6
    alfabeto = list("abdcefghijklmnopqrstuvwxyz")
    tentativas = []
    while True:
	    print(tentativas)
	    print("Chances: ",chances)
	    for letra in palavra:
		    if letra in tentativas:
			    print(letra, end = ' ')
		    else:
			    print('_', end= ' ')
	    palpite = input("\nDigite seu palpite ou 'SAIR' e voltar para menu.").lower()
	    if palpite == "sair" :
		    break
	    elif (palpite not in alfabeto or palpite == ''):
		    print("Hein!? Fala direito! Isso não é uma letra!")
		    continue
	    elif (palpite in tentativas):
		    print("Você é desmemoriado ou o quê!? Você já tentou essa letra. Tente outra!")
		    continue
	    tentativas.append(palpite)
	    if(palpite in palavra):
		    print("ACERTÔ, MIZERAVI!")
	    else:
		    print("Errou feio, errou rude!")
		    chances-=1
	    if(chances == 0):
 		    print("Perdeu, pivete! Game over!!! >:)")
 		    break
	    elif set(palavra).issubset(set(tentativas)):
		    print("Parabéns, você acertou! Weeee are the champions, my frieeeend!")
		    break
print("Bem vindo!!... Vamos comerçar?")
inicio = int(input("SIM[1] // NAO[2]: "))
if inicio != 1:
    print("Quando estiver pronto, volte novamente, até logo...!")
    exit()
else:
    nome = input("Dê um nome ao seu TAMAGOSHI: . . . ")
condicao = 0
menu2 = 0
while (condicao != 2):
    while (menu2 != -99):
        print(f"FOME = {bv.fome}")
        print(f"ENERGIA = {bv.energia}")
        menu = int(input(f"INTERAÇOES COM {nome} ;D          :\n"
                         f"[1]ALIMENTAR {nome}  \n"
                         f"[2]BRINCAR com {nome}  \n"
                         f"[3]COLOCAR {nome} p/ DORMIR  \n"))
        if (menu==1):
            if (bv.energia == 0):
                print(f"{nome} Precisa dormir.")
            while(bv.fome!=100):
                parar=int(input(f"Deseja continuar ALIMENTANDO {nome} DIGITE: [1]"))
                print(f"FOME: {alimentar()}")
                if(bv.fome==100):
                    print(f"{nome} Esta bem alimentado.")
                else:
                    print(f"{nome} ainda esta com FOME ")
        if (menu == 2):
            brincar()
        if (menu == 3):
            dormir(nome)

