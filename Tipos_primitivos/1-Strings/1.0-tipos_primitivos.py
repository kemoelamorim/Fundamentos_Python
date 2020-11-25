# Variaveis e Tipos 
nome = 'kemoel'  # valor com o tipo string ou 'str'
idade = 26  # valor com o tipo inteiro ou 'int'
salario = 4.728  # valor com o tipo ponto flutuante ou 'float'
masculino = True  # valor com tipo boleano 'bool'

# Função type() mostra o tipo que valor da variável possui
print(type(nome)) # tipo string
print(type(idade)) # tipo inteiro
print(type(salario)) # tipo ponto flutuante
print(type(masculino)) # tipo boleano

# Criando variáveis vazias
inteiro = 0
real = 0.0
texto = ""

print(type(inteiro))
print(type(real))
print(type(texto))

# O None é um valor nulo. Não tem tipo e muito menos valor
nulo = None
print(type(nulo))

""" O caractere de sublinhar (_) pode aparecer em um nome de variável. Muitas vezes é usado em nomes com várias palavras, como seu_nome ou data_de_nascimento.

Se você der um nome ilegal a uma variável, recebe um erro de sintaxe:

>>>76trombones = 'big parade' (76trombones é ilegal porque começa com um número.)
SyntaxError: invalid syntax

>>>more@ = 1000000 (more@ é ilegal porque contém um caractere @.)
SyntaxError: invalid syntax

>>>class = 'Advanced Theoretical Zymurgy'
SyntaxError: invalid syntax
Mas o que há de errado com class?

A questão é que class é uma das palavras-chave do Python. O interpretador usa palavras-chave para reconhecer a estrutura do programa e elas não podem ser usadas como nomes de variável.

O Python 3 tem estas palavras-chave:


and         del         from        None        True
as          elif        global      nonlocal    try
assert      else        if          not         while
break       except      import      or          with
class       False       in          pass        yield
continue    finally     is          raise
def         for         lambda      return

Você não precisa memorizar essa lista. Na maior parte dos ambientes de desenvolvimento, as palavras-chave são exibidas em uma cor diferente; se você tentar usar uma como nome de variável, vai perceber.

 """