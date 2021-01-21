nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_contagiosa = input("Doença infecto contagiosa? ").upper()

if idade >= 65:
    print(f"O paciente {nome} tem prioridade no atendimento!")

elif doenca_contagiosa == "SIM":
    print(f"O paciente {nome} deve ser conduzido a sala de espera!")

else:
    print(f"O paciente {nome} NÃO tem prioridade no atendimento!")