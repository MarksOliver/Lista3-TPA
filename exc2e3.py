num = int(input("Coloque um numero e aparecerá sua tabuada de 0 a 10: "))

while num < 0 or num > 10:
    print()
    print("pls coloque um numero entre 1 e 10!")
    num = num = int(input("Coloque um numero: "))

print("aqui está :)")

vz = 0

while vz <= 10:
    print(num * vz)
    vz += 1