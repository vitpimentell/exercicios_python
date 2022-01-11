'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
'''
from datetime import date
ano_nascimento = int(input('Insira o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(idade)
if idade <= 9:
    input('Você é da categoria MIRIM')
elif idade > 9 and idade < 15:
    print('Você é da categoria INFANTIL')
elif idade >= 15 and idade <= 19:
    print('Você é da categoria JUNIOR')
elif idade == 20:
    print('Você é da categoria SENIOR')
elif idade > 20:
    print('Você é da categoria MASTER')
