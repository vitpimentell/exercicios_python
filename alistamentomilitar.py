'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou passou do prazo.
'''
from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
if idade == 18:
    print('Você deve se alistar neste ano.')
elif idade > 18:
    print('Seu tempo de alistamento já passou')
else:
    print('Você ainda vai se alistar ao serviço militar')
