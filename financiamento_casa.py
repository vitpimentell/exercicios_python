''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai
pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos_pagamento = int(input('Em quantos anos você quer pagar a casa? '))
parcela_mensal = anos_pagamento * 12
prestacao = valor_casa / parcela_mensal
emprestimo_aceito = salario * 0.3 
if prestacao <= emprestimo_aceito:
    print('A prestação mensal da sua casa será de {:.2f}'.format(prestacao))
elif prestacao > emprestimo_aceito:
    print('Infelizmente, você não pode financiar essa casa')
