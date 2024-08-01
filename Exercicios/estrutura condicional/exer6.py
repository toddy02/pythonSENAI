numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
numero3 = int(input("Digite outro numero: "))


if numero1 > numero2 and numero1 > numero3:
    maior = numero1


elif numero2 > numero1 and numero2 > numero3:
    maior = numero2

else:
    maior = numero3

print(f"o maior numero é o{maior}")
