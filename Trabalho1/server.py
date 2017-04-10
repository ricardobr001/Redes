# -*- coding: utf-8 -*-
# Servidor utilizando a pilha TCP/IP
# versão python 3.5

# Importando a biblioteca Socket
# Importando o objeto Arquivo

from socket import *
# from arquivo import Arquivo

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

    # Recebendo a opção do cliente
    data = conn.recv(1024)
    opcao = data.decode()

    if (opcao == '1'):
        # Abrindo o arquivo para escrita
        arquivo = open('backup.txt', 'w')

        while True:
            # Recebendo dados enviados pelo clientes
            data = conn.recv(1024)
            texto = data.decode()
            arquivo.write(texto)

            # Se não recebermos dados do cliente, paramos o laço
            if not data: break

    elif (opcao == '2'):
        # Recebendo dados enviados pelo clientes
        data = conn.recv(1024)
        nome = data.decode()

        # Abrindo o arquivo para leitura
        arquivo = open(nome, 'r')
        texto = arquivo.read()

        # Enviando o conteúdo do arquivo para o cliente
        conn.sendall(texto.encode())

    # Fechando a conexão estabelecida com o cliente e o arquivo
    arquivo.close()
    conn.close()
