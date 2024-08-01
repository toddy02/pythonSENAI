def imc(peso,altura):
    resultado_final = peso / (altura * altura)
    return resultado_final

def categoria_imc(imc):
    if imc < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= imc < 25:
        print('Peso ideal')
    elif 25 <= imc < 30:
        print('Sobrepeso')
    else:
        print('Obesidade')

peso =float(input('Digite o peso: '))
altura =float(input('Digite a altura: '))

imc = imc(peso,altura)
categoria_imc(imc)