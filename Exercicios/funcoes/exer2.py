def solicite_temperatura():
    celsius = int(input('Informe a temperatura em Celsius: '))
    return celsius

def retorne_fahrenheit(celsius):
    f = celsius * 1.8 + 32
    return f

def retorne_kelvin(celsius):
    k = celsius + 273
    return k

celsius = solicite_temperatura()

k = retorne_kelvin(celsius)
f = retorne_fahrenheit(celsius)
print("graus Fahrenheit  ", f)
print("graus Kelvin  " ,k)