import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("100.96.1.60", 5000))
print("conectado ao servidor")

while True:
    msg=input("digite a sua mensagem: ")
    if msg.lower()=="sair":
        break
    client.send(msg.encode())
client.close()