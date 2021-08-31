def script():
    n1 = int(input('coloque a primeira nota: '))
    n2 = int(input('coloque a segunda nota: '))

    while n1 < 0 or n1 > 10:
        print()
        print('por favor coloque um numero entre 0 e 10: ')
        n1 = int(input('coloque a primeira nota: '))

    while n2 < 0 or n2 > 10:
        print()
        print('por favor coloque um numero entre 0 e 10: ')
        n2 = int(input('coloque a segunda nota: '))

    plus = n1 + n2
    média = plus / 2

    print('aqui está')
    print(média)

    print('gostaria de realizar um novo calculo: ')
    run = int(input('coloque "1" para sim e "2" para não: '))
   
    if run == 1:
        script()
    elif run == 2:
        print('bye bye vlw por ter usado')
script()