import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as er:
        print("A conexão falhou")
        print(f"Erro: {er}")
        sys.exit()

    print("Socket criado com sucesso")

    hostAlvo = input("Digite o Host ou IP: ")
    portaAlvo = input("Digite a porta a ser acessada: ")

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("Cliente TCP conectado com sucesso no Host " + hostAlvo + " E na porta " + portaAlvo)
        s.shutdown(2)
    except socket.error as er:
        print("A conexão falhou")
        print(f"Error: {er}")
        sys.exit()

if __name__ == "__main__":
    main()

