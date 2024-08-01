import time
from random import randint


escolha=True
while escolha:
    print("\n")
    print("Jogo Par ou Impar")
    print("""
    1.play
    2.menu/saida
    """)
    escolha= input("Digite a sua escolha para jogar:   ")

    if escolha == "1":
        print('-=' * 40)
        print('Par ou Impar')
        print('-=' * 40)
        opcao = ' '
        while opcao not in 'pi':
            opcao = str(input('Você quer par ou ímpar? (i/p) ')).lower().strip()[0]
        jogador = int(input('Digite um numero: '))
        eu  = randint(0 , 100)
        total = eu + jogador
        print(f'Você jogou {jogador} e eu joguei {eu}. Total {total}.')
        print('Saiu Par.' if total % 2 == 0 else 'Saiu Ímpar.')

        if opcao in 'p':
            if total % 2 == 0:
                print('Parabéns, voce ganhou o jogo.')
            else:
                print('voce perdeu o jogo.')
        if opcao in 'i':
            if total % 2 == 1:
                print('Parabens, voce ganhou o jogo.')
            else:
                print('infelismente,voce perdeu o jogo.')
        time.sleep(3)
    elif escolha == "2":
        print("Fim")
        quit()
    else:
       print("\n nao valido.\n Tente novamente.")