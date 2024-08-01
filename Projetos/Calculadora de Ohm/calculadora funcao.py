def calcular_resistencia():
    tensao = float(input("digite o valor da tensao: "))
    corrente = float(input("digite o valor da corrente: "))
    return tensao / corrente
def calcular_tensao():
    corrente = float(input("digite o valor da corrente: "))
    resistencia = float(input("digite o valor da resistencia: "))
    return resistencia * corrente

def calcular_corrente():
    tensao = float(input("digite o valor da tensao: "))
    resistencia = float(input("digite o valor da resistencia: "))
    return tensao / resistencia

def calcular_resistor():
    tensao_fonte = float(input("digite o valor da tensao_fonte: "))
    tensao_dispositivo = float(input("digite o valor da tensa_dispositivo: "))
    corrente_dispositivo = float(input("digite o valor da corrente_fonte: "))
    return (tensao_fonte / tensao_dispositivo) * corrente_dispositivo

print("calculadora de 0hm")
print("**************************************************************")
print("MENU:")
print("0 - sair")
print("1 - resistencia")
print("2 - tensao")
print("3 - corrente")
print("4 - resistencia necessaria para um resistor ")
print("****************************************************************")

while True:
    try:
        calculo = int(input("digite o valor que deseja calcular: "))

        if calculo == "1":
            resistencia = calcular_resistencia()
            print(f"resistencia de  {resistencia}")
        elif calculo == "2":
            tensao = calcular_tensao()
            print(f"tensao de {tensao}")
        elif calculo == "3":
            corrente = calcular_corrente()
            print(f"corrente de {corrente}")
        elif calculo == "4":
            resistor = calcular_resistor()
            print(f"o resistor deve ser de {resistor} 0hm")
        break
    except ValueError:
                       print("por favor, digite apenas numeros")