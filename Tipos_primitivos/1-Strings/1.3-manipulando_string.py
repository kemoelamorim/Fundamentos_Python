# Salvando a variável nome
nome = 'kemoel'
idade = '26'

# Mostrando mensagem com a variável nome
print('Seja bem vindo',nome,'sua idade é:',idade) # note que a vírgula já possibilita um espaço entre a string e a variável 

# Concatenação de string
print('Seja bem vindo '+nome+' sua idade é: '+idade)

# interpolação de strings
print('Seja bem vindo {}, sua idade é: {}'.format(nome, idade))
print(f'Seja bem vindo {nome}, sua idade é: {idade}')
print('Seja bem vindo %s, sua idade é: %s' %(nome,idade))