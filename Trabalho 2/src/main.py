import subprocess
import webbrowser
import time

# Armazena o processo do servidor
server_process = None


def iniciar_servidor():
    global server_process
    if server_process is None:
        # Inicia o servidor em um processo separado
        server_process = subprocess.Popen(["python", "server.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Servidor iniciado em segundo plano!")
        time.sleep(2)  # Espera alguns segundos para garantir que o servidor esteja rodando


def iniciar_cliente():
    url = "https://127.0.0.1:4433"  # URL do servidor
    print(f"Abrindo o navegador em {url}...")
    webbrowser.open(url)  # Abre a URL no navegador padrão


def main():
    global server_process
    while True:
        print("\n===== Sistema HTTPS =====")
        print("1 - Iniciar Servidor")
        print("2 - Iniciar Cliente (Abrir navegador)")
        print("3 - Parar Servidor")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            iniciar_servidor()
        elif opcao == "2":
            iniciar_cliente()
        elif opcao == "3":
            if server_process is not None:
                server_process.terminate()
                server_process = None
                print("Servidor parado!")
        elif opcao == "4":
            if server_process is not None:
                server_process.terminate()
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
