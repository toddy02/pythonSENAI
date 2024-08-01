#while se usa para repetição, mas necessita de uma condição
#aqui no caso a condição é o true, de verdadeiro
while True:
    #try :serve para resolver os comandos que estam dentro dele caso nao esteja de acordo com o sistema
    try:
        # input
       renda = float(input("Digite o valor R$: "))
       #break serve para sair do while
       break
    #serve para identificar o erro
    except ValueError:
        #print serve para ixibir
             print("o valor é invalido ")
#se for
if renda <= 56072.00:
    print("desconto 0%")
    #and = e
elif renda >= 56072.01 and renda <= 238532.0:
    #desconto é a variavel que recebe o desconto
    desconto =(7.50 / 100) * renda
    print(f"seu desconto é de {desconto}")
elif renda >= 238532.01 and renda <= 522400.0:
    desconto =(15 / 100) * renda
    print(f"seu desconto é de {desconto}")
elif renda >= 522400.01 and renda <= 987600.0:
    desconto =(22.50 / 100) * renda
    print(f"seu desconto é de {desconto}")
elif renda >= 987600.01:
    desconto =(27.50 / 100) * renda
    print(f"seu desconto é de {desconto}")

