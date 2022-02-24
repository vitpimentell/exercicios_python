'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''

print('SEJA BEM-VINDO AO CAIXA BOX')
saque = int(input('Quanto você deseja sacar?'))
cedulas20 = cedulas10 = cedulas1 = 0
cedulas50 = int(saque / 50)
saque = saque - cedulas50 * 50
print(f'Total de {cedulas50:.0f} cédulas de R$50,00')
if saque != 0:
    cedulas20 = int(saque/20)
    saque = saque - cedulas20 * 20
    print(f'Total de {cedulas20:.0f} cédulas de R$20,00')
if saque != 0:
    cedulas10 = int(saque/10)
    saque = saque - cedulas10 * 10
    print(f'Total de {cedulas10:.0f} cédulas de R$10,00')
if saque != 0:
    cedulas1 = int(saque/1)
    print(f'Total de {cedulas1:.0f} cédulas de R$1,00')
