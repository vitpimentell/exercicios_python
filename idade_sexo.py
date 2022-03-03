''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa devrá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos
B) quantos homens foram cadastrados
C) quantas mulheres com menos de 20 anos foram cadastradas'''

soma = cont_idade = cont_homens = cont_mulheres = cont_total = 0
while True:
    i = int(input('Idade: '))
    cont_total += 1
    if i >= 18:
        cont_idade += 1
    s = str(input('Sexo [F/M]: ')).upper().strip()
    while s != 'F' and s != 'M':
        s = str(input('Sexo [F/M]: ')).upper().strip()
    if s == 'M':
        cont_homens += 1
    if s == 'F' and i < 20:
        cont_mulheres += 1
    p = str(input('Quer continuar? [S/N] ')).upper().strip()
    while p != 'S' and p != 'N':
        p = str(input('Quer continuar? [S/N] ')).upper().strip()
    if p == 'N':
        break
print(f'Fim do programa. Foram cadastradas {cont_total} pessoas. Destas, {cont_idade} eram maiores de 18 anos, {cont_homens} eram homens e {cont_mulheres} eram mulheres com menos de 20 anos')

