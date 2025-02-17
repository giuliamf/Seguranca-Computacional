import os


def iniciar_servidor():
    os.system("python server.py")


def iniciar_cliente():
    os.system("python client.py")


def main():
    while True:
        print("\n===== Sistema HTTPS =====")
        print("1 - Iniciar Servidor")
        print("2 - Iniciar Cliente")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            iniciar_servidor()
        elif opcao == "2":
            iniciar_cliente()
        elif opcao == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()


