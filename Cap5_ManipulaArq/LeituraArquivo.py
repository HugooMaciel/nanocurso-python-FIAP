with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
print("tipo de dado da variável", type(conteudo))
print("conteúdo do arquivo:", conteudo)

with open("teste.txt", "rb") as arquivo:
    conteudo = arquivo.readlines()  # quebra em listas o conteudo do texto
print("Tipo de dado da variável", type(conteudo))
print("Conteúdo do arquivo:", conteudo)
