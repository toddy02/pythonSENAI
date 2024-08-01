numero1 = int(input('Digite o primero numero: '))
numero2 = int(input('Digite o segundo numero: '))

resultado_media =((numero1+numero2)/2)

print("resultado da media : ",resultado_media)

if resultado_media >= 70:
    print(f"o aluno foi aprovado")

elif resultado_media < 70:
    print("o aluno foi reprovado")

else:
    print(f"nota nao identificada ")