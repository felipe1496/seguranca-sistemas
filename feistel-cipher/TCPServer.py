from socket import *

serverPort = 12000
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
#Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

def shift(string):
    if len(string) <= 1:
        return string
    e = [string[-1]]
    e.extend(string[:-1])
    return e

def divide_in_groups(string):
    grupos = []
    while len(string) >= 3:
        grupos.append(string[:3])
        string = string[3:]
    if string:  
        grupos.append(string)
    return grupos

def ints_to_ascii(lista_inteiros):
    ascii_string = ''.join(chr(num) for num in lista_inteiros)
    return ascii_string.encode('ascii')

def feistel_cipher(text):
    def feistel_round(text):
        left, right = text[:len(text)//2], text[len(text)//2:]
        
        groups = divide_in_groups(right)
    
        e = []
        for g in groups:
            shifted = shift(g)
            e.extend(shifted)
        
        new_right = ints_to_ascii(e)

        new_right = bytes([x ^ y for x, y in zip(left, new_right)])
        return right + new_right

    for _ in range(4):
        text = feistel_round(text)
    return text

while 1:
        #Cria um socket para tratar a conexao do cliente
     connectionSocket, addr = serverSocket.accept()
     sentence = connectionSocket.recv(1024)
     capitalizedSentence = feistel_cipher(sentence)
     connectionSocket.send(capitalizedSentence)
     connectionSocket.close()