class Error(Exception):
    pass


class PersonalizadoError(Error):
    def __init__(self, mensage):
        self.mensage = mensage


while True:
    try:
        x = int(input("Entre com uma nota de 0  10: "))
        print(x)
        if x > 10:
            raise PersonalizadoError("Não pode ser maior que 10")
        elif x < 0:
            raise PersonalizadoError("não pode ser menor que 0")
        break
    except ValueError:
        print("Valor invalido; deve-se digitar apenas numeros.")
    except PersonalizadoError as ex:
        print(ex)
