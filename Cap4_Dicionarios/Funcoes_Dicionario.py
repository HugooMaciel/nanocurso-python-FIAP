def perguntar():
    resposta = input("O que deseja realizar?\n " +
                     "\t<I> - Para Inserir um usuário;\n" +
                     "\t<P> - Para Pesquisar um usuário;\n" +
                     "\t<E> - Para Excluir um usuário;\n" +
                     "\t<L> - Para Listar um usuário:\n"+"\t").upper()
    return resposta


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada: ").upper()]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])


def excluir(dicionario, chave):
    if dicionario.get(chave) is not None:
        del dicionario[chave]
    print("Objeto Eliminado")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto........")
        print("Login: ", chave)
        print("Dados: ", valor)
