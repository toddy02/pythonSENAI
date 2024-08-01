print("digite um numero para descobrir se ele é negativo ou positivo")
print("")
numero = int(input("digite um numero: "))

if numero > 0:
    print(f"o numero {numero} é positivo")

elif numero == 0:
    print(f"o numero {numero} é negativo")

else:
   print("o numero é neutro ")