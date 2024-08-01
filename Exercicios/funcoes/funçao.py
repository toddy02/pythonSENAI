 #datetime = hora de agr

from datetime import datetime

#def = chamar função
def menu_calculadora():
    print("calculadora")
    print("1 adição")
    print("2 subtracão")
    print("3 mutiplicação")
    print("4 divisao")



def ola_nome(nome):
    print (f"ola {nome}")


def return_ola_nome(nome):
    return f"ola {nome}"

def calcular_idade (ano_de_nascimento):
   ano_atual = datetime.now().year
   idade = ano_atual - ano_de_nascimento
   return idade



def mostrar_idade (ano_de_nascimento):
   ano_atual = datetime.now().year
   idade = ano_atual - ano_de_nascimento
   print("a sua idade é",idade,"anos")

print("a sua idade é",mostrar_idade(ano_de_nascimento = 1997))


mostrar_idade(1997)

def solicita_ano_nascimento():
while True:
    try:
     ano_de_nascimentp = int(input("digite seu ano de nascimento "))
     if ano_de_nascimentp > datetime.now().year:
         print("degite um ano valido")
else
    return solicita_ano_nascimento
    except ValueError
        print("digite um valor inteiro. Ex: 1997")


#print(calcular_idade(ano_de_nascimento = 1997

#exibir_idade(1997)

#exibe o menu da calculadora
menu_calculadora()

#exibe o print com "ola emily"
ola_nome("emily")

#retorna ao texto com ola "ola emily"
print("boa tarde ",return_ola_nome("emily"))

