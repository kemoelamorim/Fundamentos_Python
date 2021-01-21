tabuada = int(input("Digite um número para ver a tabuada: "))
print("\t" + "A buada de ",tabuada)
for numero in range(1, 11, 1):
    print(str(tabuada) + " x " + str(numero) +  " = " + str(tabuada * numero))
    