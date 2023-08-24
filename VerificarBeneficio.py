idade=0
salario=0
dependentes=0
nome=0
while(idade<18):
   idade=int(input(f"Digite sua idade: "))
   if(idade>=18):
      nome=str(input(f"Digite seu nome: "))
   else:
      print(f"menor de idade, por tanto nao poderá seguir com cadastro. ")
salario=float(input(f"{nome}, quanto você recebe mensalmente? "))
dependentes=int(input(f"{nome}, possui quantos dependentes em sua residencia(mae, pai, filhos, etc...). Se nao possuir, Digite 0 "))
if(salario<1000 and dependentes<=2):
   print(f"{nome}, CREDITO PRE APROVADO!!! VOCE PODERA SEGUIR COM SEU BENEFICIO.")
   print(f"Seu salario atual: {salario}, e compativel com beneficio e você poderar ter {dependentes} dependentes.")
else:
   print("Seu salario é superior a R$1000 ou numero de dependentes excede os requisitos, portanto nao podera seguir com beneficio")
