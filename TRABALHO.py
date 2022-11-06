import matb
print(":::::::::::::CALCULADORA::::::::::::")
operador = 1
while (operador != '0'):
    val1 = int(input("INSIRA PRIMEIRO NUMERO:    "))
    val2 = int(input("INSIRA SEGUNDO NUMERO: "))
    operador = input("Selecione operador +, -, *,/ ,% ou DIGITE [0] Para SAIR")
    saida = operador
    if (operador == '+'):
        res = matb.som(val1, val2)
        print(f"SOMA:  {val1} + {val2} = {res}")
    elif (operador == '-'):
        res = matb.sub(val1, val2)
        print(f"Subtração:  {val1} - {val2} = {res}")
    elif (operador == '*'):
        res = matb.mul(val1, val2)
        print(f"Multiplicacao:  {val1} * {val2} = {res}")
    elif (operador == '/'):
        res = matb.div(val1, val2)
        print(f"Divisao:  {val1} / {val2} = {res}")
    elif (operador == '%'):
        res = matb.por(val1, val2)
        print(f"Porcentagem(%):  {val1}% de {val2} = {res}")
    elif (saida == '0'):
        print("::::::::::::Calculadora Finalizada... Até logo.::::::::::::::")
        exit(0)