# Cliente utilizando a pilha TCP/IP
# Importando a biblioteca socket

from socket import *

# Configurações para estabelecer a conexão com o Servidor
HOST = 'localhost'
PORT = 25000

# Mensagem que será levada ao Servidor em bytes
message = input("Mensagem a ser enviada: ")

# Criando o socket e conectando ao Servidor
socket_object = socket(AF_INET, SOCK_STREAM)
socket_object.connect((HOST, PORT))

# Enviando a mensagem para o Servidor linha por linha
socket_object.sendall(message.encode())

# Após enviar a linha para o servidor, aguardamos uma resposta
data = socket_object.recv(1024)
print ('Cliente recebeu:', data.decode())

# Fechando a conexão
socket_object.close()
