from Funcoes.Funcoes import *

usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    opcao = perguntar()
    if opcao == "P":
        pesquisar(usuarios, input("Qual login deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios, input("Qual login deseja excluir? "))
    if opcao == "L":
        listar(usuarios)
else:
    print("Por favor, digite uma das opções")
    opcao = perguntar()
print(usuarios)
