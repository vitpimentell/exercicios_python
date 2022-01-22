import random
escolhausuario = str(input('Digite pedra, papel ou tesoura: ')).upper()
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
escolhapc = random.choice(jokenpo)
print(escolhapc)
if escolhapc == escolhausuario:
    print('Empatou! Nós dois jogamos {}'.format(escolhapc))
elif escolhapc == 'PEDRA' and escolhausuario == 'PAPEL':
    print('Eita, você ganhou! Joguei {} :('.format(escolhapc))
elif escolhapc == 'PEDRA' and escolhausuario == 'TESOURA':
    print('Hahaha! Eu ganhei. Joguei {}'.format(escolhapc))
elif escolhapc == 'PAPEL' and escolhausuario == 'PEDRA':
    print('Hahaha! Eu ganhei. Joguei {}'.format(escolhapc))
elif escolhapc == 'PAPEL' and escolhausuario == 'TESOURA':
    print('Eita! Você ganhou. Joguei {} :('.format(escolhapc))
elif escolhapc == 'TESOURA' and escolhausuario == 'PAPEL':
    print('Hahaha! Eu ganhei. Joguei {}!'.format(escolhapc))
elif escolhapc == 'TESOURA' and escolhausuario == 'PEDRA':
    print('Eita! Você ganhou. Joguei {} :('.format(escolhapc))
else:
    print('Opção inválida. Digite novamente!')
