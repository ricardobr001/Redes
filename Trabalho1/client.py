# Cliente utilizando a pilha TCP/IP
# Versão python 3.5

# Importando a biblioteca socket
from socket import *

# Configurações para estabelecer a conexão com o Servidor
HOST = 'localhost'
PORT = 25000

# Menu com as opções possiveis
print ('1 - Enviar um arquivo')
print ('2 - Recuperar um arquivo')

# Lendo a opção
opcao = input('Digite uma opção: ')

if (opcao == '1'):
    # Criando o socket e conectando ao Servidor
    socket_object = socket(AF_INET, SOCK_STREAM)
    socket_object.connect((HOST, PORT))

    # Enviando qual opção o cliente quer
    socket_object.send(opcao.encode())

    # Abrindo o arquivo
    nome = input('Nome do arquivo a ser enviado: ')
    # Enviando o nome do arquivo
    socket_object.send(nome.encode())
    arquivo = open(nome, 'r')
    texto = arquivo.read()

    # Enviando o arquivo para o Servidor
    socket_object.sendall(texto.encode())
    arquivo.close()

    # Fechando a conexão
    socket_object.close()

elif (opcao == '2'):
    # Criando o socket e conectando ao Servidor
    socket_object = socket(AF_INET, SOCK_STREAM)
    socket_object.connect((HOST, PORT))

    # Enviando qual opção o cliente quer
    socket_object.send(opcao.encode())

    # Lendo o nome do arquivo
    nome = input('Nome do arquivo a ser recebido: ')

    # Enviando o nome do arquivo para o Servidor
    socket_object.sendall(nome.encode())

    # Abrindo o arquivo para escrita
    arquivo = open(nome, 'w')

    while True:
        # Recebendo dados enviados pelo clientes
        data = socket_object.recv(1024)
        texto = data.decode()
        arquivo.write(texto)

        # Se não recebermos dados do cliente, paramos o laço
        if not data: break
    arquivo.close()

    # Fechando a conexão
    socket_object.close()
else:
    print ('Opção inválida!!')
