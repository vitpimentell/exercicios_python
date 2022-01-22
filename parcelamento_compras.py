'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:

- À vista (dinheiro/cheque): 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''


produto = float(input('Digite o valor do produto: R$'))
print('''FORMAS DE PAGAMENTO:
[1] À vista em dinheiro ou cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
formadepagamento = int(input('Digite o número da forma de pagamento: '))
if formadepagamento == 1:
    total = produto - (produto * 0.1)
elif formadepagamento == 2:
    total = produto - (produto * 0.05)
elif formadepagamento == 3:
    total = produto
    parcela = total / 2
    print('O produto custará R${:.2f}, em parcelas de {:.2f}'.format(total,parcela))
elif formadepagamento == 4:
    parcelamento = int(input('Em quantas parcelas você quer pagar?'))
    total = produto * 1.2
    parcela = total / parcelamento
    print('O produto custará R${:.2f}, em {} parcelas de R${:.2f} COM JUROS'.format(total, parcelamento, parcela))
else:
    total = produto
    print('Opção inválida. Digite novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(produto, total))
