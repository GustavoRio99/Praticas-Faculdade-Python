import math
def som(val1, val2):
    return val1 + val2


def sub(val1, val2):
    return val1 - val2


def div(val1, val2):
    return val1 / val2


def mul(val1, val2):
    return val1 * val2


def por(val1, val2):
    return (val2 * (val1 / 100))


print(":::::::::::::CALCULADORA::::::::::::")
operador = 1
while (operador != '0'):
    val1 = int(input("INSIRA PRIMEIRO NUMERO:    "))
    val2 = int(input("INSIRA SEGUNDO NUMERO: "))
    operador = input("Selecione operador +, -, *,/ ,% ou DIGITE [0] Para SAIR")
    saida = operador
    if (operador == '+'):
        res = som(val1, val2)
        print(f"SOMA:  {val1} + {val2} = {res}")
    elif (operador == '-'):
        res = sub(val1, val2)
        print(f"Subtração:  {val1} - {val2} = {res}")
    elif (operador == '*'):
        res = mul(val1, val2)
        print(f"Multiplicacao:  {val1} * {val2} = {res}")
    elif (operador == '/'):
        res = div(val1, val2)
        print(f"Divisao:  {val1} / {val2} = {res}")
    elif (operador == '%'):
        res = por(val1, val2)
        print(f"Porcentagem(%):  {val1}% de {val2} = {res}")
    elif (saida == '0'):
        print("::::::::::::Calculadora Finalizada... Até logo.::::::::::::::")
        exit(0)
