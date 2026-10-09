print('----Seja bem - vindo a CALCULADORA DE SONO----')
horas = float(input('Digite quantas horas você dormiu esta noite: '))

min= horas * 60
seg = min * 60

print('Você dormiu: {:.2f}h'.format(horas))
print('Que em minutos é: {:.0f} minutos '.format(min))
print('E equivale a {:.0f} segundos'.format(seg))


if horas < 6:
    print('\nStatus: Bateria fraca! Priorize o descanso hoje! 🌙')
else:
    print('\nStatus: Sono em dia! Pronta para o combate! 🚀')