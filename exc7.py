print('quer que eu te mostre os numeros impares de 1 a 100?')
sn = int(input('Coloque 1 para sim e 2 para não: '))

while sn < 1 or sn > 2:
    print('coloque uma resposta valida')
    sn = int(input('Coloque 1 para sim e 2 para não: '))

i = 1

if sn == 1:
    while i <= 100:
        print(i)
        i += 2        
elif sn == 2:
    print("ah, então tá bom T-T")