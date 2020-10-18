"""
Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3 
raiz = int(numero **(1/2))
print('O número {} tem o dodro {} o triplo {} e a raiz quadrada {}'. format(numero, dobro,triplo, raiz))
