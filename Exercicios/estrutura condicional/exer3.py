ano = int(input("digite seu ano de nascimento: "))
idade = 2024 - ano

if idade > 18:
   saudacao = "adulto"

elif idade == 18:
     saudacao = "maior de idade"

elif idade < 18:
    saudacao = "menor de idade"

print("voce tem",idade,"anos,",saudacao)