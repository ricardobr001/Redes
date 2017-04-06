# Servidor utilizando a pilha TCP/IP
# versão python 3.5

# Importando a biblioteca Socket

from socket import *

# Criando nome do host (Usando o localhost)
HOST = ''

# Porta que será utilizada no socket para rodar a aplicação e o Servidor
PORT = 25000

# Criando um objeto do tipo socket com a pilha TCP/IP
# AF_INET é o protocolo IP
# SOCK_STREAM é o protocolo TCP
# Combinando teremos a pilha TCP/IP
socket_object = socket(AF_INET, SOCK_STREAM)

# Vinculando o servidor ao número da porta escolhida
socket_object.bind((HOST, PORT))

# O socket irá aguardar por clientes, limitando a 5 clientes
socket_object.listen(1)

while True:
    # Aceitando a nova conexão e devolvendo o seu endereço
    conn, addr = socket_object.accept()
    print ('Server connected by', addr)

    while True:
        # Recebendo dados enviados pelo clientes
        data = conn.recv(1024)
        maiuscula = data.decode()
        maiuscula = maiuscula.upper()
        data = maiuscula.encode()

        # Se não recebermos dados do cliente, paramos o laço
        if not data: break

        # Enviando de volta para o cliente uma resposta do Servidor
        conn.sendall(data)

    # Fechando a conexão estabelecida com o cliente após a resposta ser enviada
    conn.close()
