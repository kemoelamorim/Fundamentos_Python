"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a babuada.
"""
numero = int(input('Digite um número para ver a tabuada: '))
print('-'*10)
for i in range(1, 11):
    resultado = i * numero
    print(f'{i} x {numero} = {resultado}')
print('-'*10)

