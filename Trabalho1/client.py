# Cliente utilizando a pilha TCP/IP
# Importando a biblioteca socket

from socket import *

# Configurações para estabelecer a conexão com o Servidor
serverHost = 'localhost'
serverPort = 25000

# Mensagem que será levada ao Servidor em bytes
message = [b'Ola server!!']

# Criando o socket e conectando ao Servidor
socket_object = socket(AF_INET, SOCK_STREAM)
socket_object.connect((serverHost, serverPort))

# Enviando a mensagem para o Servidor linha por linha
for line in message:
    socket_object.send(line)

    # Após enviar a linha para o servidor, aguardamos uma resposta
    data = socket_object.recv(1024)
    print ('Cliente recebeu:', data)

# Fechando a conexão
socket_object.close()
