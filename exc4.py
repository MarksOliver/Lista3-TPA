dv1 = int(input('escreva o numero para ser divido: '))
dv2 = int(input('escreva o numero para dividir: '))

while dv2 == 0:
    print()
    print('por favor coloque um número diferente de zero: ')
    dv2 = int(input('escreva o numero para dividir: '))

print('aqui está')
print(dv1 / dv2)