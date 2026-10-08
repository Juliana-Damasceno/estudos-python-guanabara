import random 

print('Seja bem - vindo ao Jogo de ÍMPAR ou PAR:')
l = input('Digite IMPAR se você quer ÍMPAR ou PAR se você quer par[IMPAR/PAR]: ')
nj = int(input('Digite umm número entre 0 e 10: '))
nc = random.randint(0,10)
s = nj + nc

if (s % 2 == 0):
    resultado = "PAR"
else:
    resultado = "IMPAR"

print('Seu número escolhido foi: {}'.format(nj))
print('O número escolhido pelo pc foi: {}'. format(nc))
print('A soma é:',s)

if ( l == resultado):
    print('Parabéns, você ganhouuu!!!')

else:
    print('Poxa, tente mais uma vez!!')