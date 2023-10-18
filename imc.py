# Peso e altura
peso=float(input('Digite seu peso:'))
altura=float(input('digite sua altura:'))

# Os calculos entre eles
c=(peso * altura/100)**2

# O resultado entre eles
print('O seu imc é {}'.format(c))

# Resultado
if c < 19:
    print('O seu imc esta muito alto.')
else:
    print('Você esta com o imc na média.')    