import datetime

tempo = datetime.datetime.now()
semana = datetime.datetime.now().isoweekday()
mes = tempo.month
ano = tempo.year
dia = tempo.day
hora = tempo.hour
minuto = tempo.minute
segundo = tempo.second
resposta = ''
ms = ""

if hora < 12:
    comprimento = "Bom dia"
elif hora < 12 and hora < 18:
    comprimento = "Boa tarde"
else:
    comprimento = "Boa noite"


if semana == 1 :
    resposta = "Segunda"
elif semana == 2:
    resposta = "treça"
elif semana == 3:
    resposta = "Quarta"
elif semana == 4:
    resposta = "Quinta"
elif semana == 5:
    resposta = "Sexta"
elif semana == 6:
    resposta = "sabado"
elif semana == 7:
    resposta = "domingo"


if mes == 1:
    ms = "janeiro"
elif mes == 2:
    ms = "fevereiro"
elif mes == 3:
    ms = "março"
elif mes == 4:
    ms = "abril"
elif mes == 5:
    ms = "maio"
elif mes == 6:
    ms = "junho"
elif mes == 7:
    ms = "julho"
elif mes == 8:
    ms = "agosto"
elif mes == 9:
    ms = "setembro"
elif mes == 10:
    ms = "outubro"
elif mes == 11:
    ms = "novembro"
elif mes == 12:
    ms = "dezembro"

print(f"{comprimento}\nhoje é {dia} do mes {mes} de {ms} , do ano {ano}, agora sao {hora}:{minuto}:{segundo}")

