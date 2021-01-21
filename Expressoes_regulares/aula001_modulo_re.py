import re

string = "Este é um teste , para buscar expressoes testes regulares"

print(re.search(r'teste', string))  # o metodp search retorna a primeira ocorrencia
print(re.findall(r'teste', string))  # o metodo fundall retorna todas as ocorrencias
print(re.sub(r'teste', 'teste-substituido', string))  # O metodo sub subistitui a expressao

print("\n")
# aqui iremos compilar apenas uma vez a expressao
regexp = re.compile("teste")
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub("teste-sub2", string))
