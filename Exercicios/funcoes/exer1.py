from datetime import datetime


def solicite_nome():
 nome = input('Qual o seu nome? ')
  return nome



def define_saudacao(hora_atual)
if hora_atual >= 0 and hora_atual <= 5:
     saudacao = "boa madrugada"
elif hora_atual  <= 12:
 saudacao = "bom dia "
elif hora_atual > 19:
 saudacao = "boa tarde"
else
 saudacao = "boa noite"

   return saudacao


def exibir_mensagem(nome,saudacao)
 print(saudacao + nome)




