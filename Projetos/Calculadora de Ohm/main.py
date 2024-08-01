print("selecione um numero para calcular a resistencia ou a tensão ou a corrente eletrica ou resistência de resistor.")

print("1 - resitencia\n2 - tensão\n3 - corrente\n4 - resistencia de resistor")
resistencia = 1
tensao = 2
corrente = 3
resistor = 4

selecao = int(input("digite oque voce deseja calcular "))

if selecao == resistencia:
    tensao = float(input("digite o valor da tensao em V "))
    corrente = float(input("digite o valor da corrente em A"))
    calculo = tensao / corrente
    print("o resultado da resisitencia é", calculo, "em Ώ")

elif selecao == tensao:
    resistencia = float(input("digite o valor da resistencia em Ώ"))
    corrente = float(input("digite o valor da corrente em A"))
    conta = resistencia * corrente
    print("resultado da tensao é", conta, "em V")

elif selecao == corrente:
   tensao = float(input("digite o valor da tensao em V "))
   resistencia = float(input("digite o valor da resistencia em Ώ"))
   valor = tensao / resistencia
   print("resultado da corrente", valor, "em A")

elif selecao == resistor:
  tensao1 = float(input("digite o valor da tensao da fonte  em V "))
  tensao2 = float(input("digite o valor da tensao  em V "))
  corrente = float(input("digite o valor da corrente em A"))
  resistencia = tensao1 - tensao2 / corrente

else:
   print("deu erro tente novamente")


