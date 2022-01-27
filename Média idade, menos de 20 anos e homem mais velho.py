velho = 0
mediaidade = 0
somaidade = 0
somamulheres = 0
nomehomem = ''
for p in range(1,5):
    print(f'{p}ª PESSOA')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade += idade
    if sexo == 'F' and idade < 20:
        somamulheres += 1
    if p == 1 and sexo == 'M':
        velho = idade
    if sexo == 'M' and idade > velho:
        velho = idade
        nomehomem = nome
mediaidade = somaidade / p
print(f'A média da idade do grupo é {mediaidade} anos')
print(f'{somamulheres} mulheres tem menos de 20 anos')
print(f'O homem mais velho é {nomehomem}, ele tem {velho} anos')
