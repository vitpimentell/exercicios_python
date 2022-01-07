""" Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. 
Para inferiores ou iguais, o aumento é de 15%"""

salario = float(input('Qual é o seu salário? '))
if salario > 1250:
    print('Seu salário será de R$ {}'.format(salario * 0.1 + salario))
if salario <=  1250:
    print('Seu salário será de R$ {}'.format(salario * 0.15 + salario))
