print("oi, escolha um número positivo e irei mostar todos os numeros pares entre 1 e o número escolhido :)")

num = int(input("insira um número positivo: "))

while num < 0:
    print("número inváido")
    num = int(input("insira um número positivo: "))

bgn = 2

while bgn <= num:
    print(bgn)
    bgn += 2
print("obrigado por ter usado ;)")