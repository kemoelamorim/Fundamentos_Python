"""
Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
"""
from random import shuffle
alunos = []

for i in range(4):
    i = input("Digite o nome do aluno: ")
    alunos.append(i)
(shuffle(alunos))
print(alunos)