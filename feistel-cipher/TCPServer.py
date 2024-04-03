from socket import *
from cipher import Cipher

serverPort = 12000
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
#Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

cipher = Cipher()

while 1:
    #Cria um socket para tratar a conexao do cliente
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    encrypted = cipher.encrypt(sentence.decode("ascii"))
    decrypted = cipher.decrypt(encrypted)
    response = "\n" + "- criptografado: " + encrypted + "\n" + "- decriptografado: " + decrypted
    connectionSocket.send(bytes(response.encode("utf-8")))
    connectionSocket.close()