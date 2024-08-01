def lado1():
    lado_1 = float(input('Digite o lado 1: '))
    return lado_1

def lado2():
    lado_2 = float(input('Digite o lado 2: '))
    return lado_2

def lado3():
    lado_3 = float(input('Digite o lado 3: '))
    return lado_3

def valor_triangolo (lado_1, lado_2, lado_3):
    if lado_1 == lado_2 and lado_1 == lado_3:
        return "equilatero"
    elif lado_1 !== lado_3 and lado_2 !== lado_3 and lado_1 !== lado_2:
        return "escaleno"
    else:
        return "isosceles"

lado_1()
lado_2()
lado3()
resuntado = valor_triangolo(lado1, lado2, lado3)
print(resuntado)