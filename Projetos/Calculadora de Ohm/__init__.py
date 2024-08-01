# O while repete tudo que esta dentro dele
while True:
    # O try vai tentar executar esse bloco de codigo
     try:
         idade = int(input("Digite sua idade: "))

     # O  if verifica a idade valida
     if idade > 0 and idade <= 100:
        print("idade :", idade)
        #O break sai do while
        break:
     else:
        print("idade invalida")
    except ValueError:
          #caso der erro executa aqui
          print("digite sua idade em numero. Ex:26")

