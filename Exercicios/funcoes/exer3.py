def menu_calculadora():
    print("calculadora")
    print("1 adição")
    print("2 subtracão")
    print("3 mutiplicação")
    print("4 divisao")
    print("")

def escolha_numero():
    while True:
        try:
            numero1 = int(input("digite um numero: "))
            return numero1
        except ValueError:
            print("esta incorreto , tente novamente")


def outro_numero():
    while True:
        try:
            numero2 = int(input("digite um numero: "))
            return numero2
        except ValueError:
            print("esta incorreto , tente novamente")

def solicite_escolha():
    while True:
        try:
            escolha = int(input("escolha entre 1,2,3 e 4 :"))
            return escolha
        except ValueError:
            print("esta incorreto , tente novamente")


def soma(numero1, numero2):
    soma = numero1 + numero2
    return soma

def subtracao(numero1, numero2):
    subtracao = numero1 - numero2
    return subtracao

def multiplicacao(numero1, numero2):
    multiplicacao = numero1 * numero2
    return multiplicacao

def divisao(numero1, numero2):
    divisao = numero1 / numero2
    return divisao

valor_a = escolha_numero()
valor_b = outro_numero()
menu_calculadora()
opiao = solicite_escolha()

if opiao == 1:
    print(valor_a + valor_b)
elif opiao == 2:
    print(valor_a - valor_b)
elif opiao == 3:
    print(valor_a * valor_b)
elif opiao == 4:
    print(valor_a / valor_b)




