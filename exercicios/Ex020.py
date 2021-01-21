"""
Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
"""
from random import shuffle
alunos = []

for i in range(4):
    item = input("Digite o nome do aluno: ")
    alunos.append(item)
(shuffle(alunos))
print(alunos)
