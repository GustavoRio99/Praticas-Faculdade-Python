

def dormir(nome):
    for i in range(101):
        print(f"{nome} esta dormindo...{i}%")
    condicao = int(input(f" DESEJA [1]ACORDAR {nome} :) OU [2]DEIXAR {nome} DORMINDO? (U-u..Zzz) "))
    if (condicao == 1):
        print(f"{nome} ACABOU DE ACORDAR :) ")
    if (condicao == 2):
        print("Volte daqui a pouco...Até logo! (U-u..Zzz)")
        exit()


def brincar():
    menu2 = int(input(f"ESOLHA UMA BRINCADEIRA: [1]JOGO PERGUNTAS E RESPOSTAS / [2]JOGO FORCA  / [3]VOLTAR"))
    if (menu2 == 1):
        print(f"{nome} FALANDO: O jogo possui perguntas por temas e de multipla escolha...=D")
        print(f"{nome} FALANDO: Escolha um Tema: =D")
        tema = int(input("[1]TECNOLOGIA E INFORMATICA // [2]MATEMATICA & FISICA // [3] CONHECIMENTO GERAL"))
         #if(tema==1):



print("Bem vindo!!... Vamos comerçar?")
inicio = int(input("SIM[1] // NAO[2]: "))
if inicio != 1:
    print("Quando estiver pronto, volte novamente, até logo...!")
    exit()
else:
    nome = input("Dê um nome ao seu TAMAGOSHI: . . . ")
    # pet=input("Dê um nome ao seu TAMAGOSHI: . . . ")
condicao = 0
menu2 = 0
while (condicao != 2):
    while (menu2 != -99):
        menu = int(input(f"INTERAÇOES COM {nome} ;D          :"
                         f"[1]ALIMENTAR {nome}  "
                         f"[2]BRINCAR com {nome}  "
                         f"[3]COLOCAR {nome} p/ DORMIR  "))
        if (menu == 2):
            brincar()
        if (menu == 3):
            dormir(nome)
