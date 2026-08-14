import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(("0.0.0.0", 5000))

servidor.listen(1)

print("Servidor iniciado!")
print("Esperando a conexão...")

conexao, endereco = servidor.accept()

print()
print("================================")
print("CONEXÃO RECEBIDA!")
print("IP:", endereco[0])
print("PORTA:", endereco[1])
print("================================")

while True:
    dados = conexao.recv(1024)

    if not dados:
        break

    mensagem = dados.decode()

    print("Mensagem recebida:", mensagem)

conexao.close()
servidor.close()