print('Seja bem - vinda ao Rastreador de Hábitos!!!')
nome = input('Digite seu nome: ')
print('Olá {}! Vamos registrar seus hábitos de hoje:'.format(nome))

p1 = input('1. Você concluiu o bloco de estudos de Python? [S/N]')
p2 = input('2. Você concluiu seu bloco de inglês? [S/N]')
p3 = input('3. Você realizou seus exercicios físicos? [S/N]')

pontos = 0

if p1 == 'S':
    pontos += 1
if p2 == 'S':
    pontos += 1
if p3 == 'S':
    pontos += 1

percentual = (pontos/3) * 100

print('Resumo do dia!!!')
print('Hábitos concluídos: {}/3'.format(pontos))
print('Percentual de hábitos:{:.2f}%'.format(percentual))

if percentual == 100:
    print('Parabéns,{}! Você concluiu tudo!!' .format(nome))
elif percentual >= 50:
     print('Bom trabalho,{}! Você foi muito bem hoje!!'.format(nome))
else :
    print('Tudo bem,{}!! Amanhã é um novo dia!!'.format(nome))


