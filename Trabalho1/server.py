# Servidor utilizando a pilha TCP/IP
# Importando a biblioteca socket

from socket import *

# Criando nome do host (Usando o localhost)
myHost = ''

# Porta que será utilizada no socket para rodar a aplicação e o Servidor
myPort = 25000

# Criando um objeto do tipo socket com a pilha TCP/IP
# AF_INET é o protocolo IP
# SOCK_STREAM é o protocolo TCP
# Combinando teremos a pilha TCP/IP
socket_object = socket(AF_INET, SOCK_STREAM)

# Vinculando o servidor ao número da porta escolhida
socket_object.bind((myHost, myPort))

# O socket irá aguardar por clientes, limitando a 5 clientes
socket_object.listen(5)

while True:
    # Aceitando a nova conexão e devolvendo o seu endereço
    connection, address = socket_object.accept()
    print ('Server connected by', address)

    while True:
        # Recebendo dados enviados pelo clientes
        data = connection.recv(1024)

        # Se não recebermos dados do cliente, paramos o laço
        if not data: break

        # Enviando de volta para o cliente uma resposta do Servidor
        connection.send(b'Eco=>' + data)

    # Fechando a conexão estabelecida com o cliente após a resposta ser enviada
    connection.close()
