# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
ano = int(input('Digite um ano: '))
if (ano % 4) == 0:
    print('Este é um ano bissexto')
else:
    print('Este não é um ano bissexto')
