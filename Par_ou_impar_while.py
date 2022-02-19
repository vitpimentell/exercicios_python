'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''

from random import randint
s = c = 0
while True:
    v = int(input('Digite um valor: '))
    opção = str(input('Par ou ímpar? [P/I]: ')).upper().strip()
    if opção != 'P' and opção != 'I':
        print('Opção inválida. Tente novamente.')
        break
    computador = randint(0,10)
    s = computador + v
    print(f'Você escolheu {v} e eu {computador}. A soma foi {s}.')
    if opção == 'P' and s % 2 == 0:
        print('DEU PAR! Você venceu')
        c += 1
    if opção == 'I' and s % 2 != 0:
        print('DEU ÍMPAR! Você venceu')
        c += 1
    if opção == 'P' and s % 2 != 0:
        print('DEU ÍMPAR! Você perdeu')
        break
    if opção == 'I' and s % 2 == 0:
        print('DEU PAR! Você perdeu!')
        break
print(f'FIM DO PROGRAMA. Você venceu {c} vezes.')
