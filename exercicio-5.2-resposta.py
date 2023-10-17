def principal():

    teste1 = verifica_senha_1()

    if teste1 == "OK1":

        teste2 = verifica_senha_2()

        if teste2 == "OK2":

            teste3 = verifica_senha_3()

            if teste3 == "OK3":

                parabens()

                return "ACABOU"

def verifica_senha_1():

    print("Digite a primeira senha: ")

    senha1 = input()

    if senha1 == "creiton":

        return "OK1"

    else:

        return "DEURUIM"

def verifica_senha_2():

    print("Digite a segunda senha: ")

    senha2 = input()

    if senha2 == "shaissen":

        return "OK2"

    else:

        return "DEURUIM"

def verifica_senha_3():

    print("Digite a terceira senha: ")

    senha3 = input()

    if senha3 == "panturrilha":

        return "OK3"

    else:

        return "DEURUIM"

def parabens():

    print ("Parabens")

while (0 == 0):

    status = principal()

    if status == "ACABOU":

        break
