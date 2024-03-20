from socket import *

serverPort = 12000
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
#Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

key1 = "5ioR4iDvs4IQuEvUyjbhd"
key2 = "m2H0PFYLYOiio0guP8vpj"
key3 = "ZvgcwXjLXTUmWIMgRLsJw"
key4 = "FVJnQtZvQgKeRcCnJc1Xh"

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

# Defining BinarytoDecimal() function 
def BinaryToDecimal(binary): 
       
    # Using int function to convert to 
    # string    
    string = int(binary, 2) 
       
    return string


# Text vem no formato ascii
def feistel_cipher(plaintext, rounds=4):
    # Converting the ASCII to 
    # 8-bit binary format
    PT_Bin = [format(y,'08b') for y in plaintext]
    PT_Bin = "".join(PT_Bin)
    n = int(len(PT_Bin)//2)

    def exor(a,b):
        temp = "" 
        for i in range(n-1): 
            if (a[i] == b[i]):
                temp += "0"
            else: 
                temp += "1"
        return temp 

    L1 = PT_Bin[0:n]
    R1 = PT_Bin[n::]
    m = len(R1)

    # first round of Feistel
    f1 = exor(R1,key1)
    R2 = exor(f1,L1)
    L2 = R1

    # Second round of Feistel
    f2 = exor(R2,key2)
    R3 = exor(f2,L2)
    L3 = R2

    # Cipher text
    bin_data = L3 + R3
    str_data =' '
    for i in range(0, len(bin_data), 7): 
        # slicing the bin_data from index range [0, 6] 
        # and storing it in temp_data 
        temp_data = bin_data[i:i + 7] 
            
        # passing temp_data in BinarytoDecimal() function 
        # to get decimal value of corresponding temp_data 
        decimal_data = BinaryToDecimal(temp_data) 
            
        # Decoding the decimal value returned by  
        # BinarytoDecimal() function, using chr()  
        # function which return the string corresponding  
        # character for given ASCII value, and store it  
        # in str_data 
        str_data = str_data + chr(decimal_data) 

    print("str_data: ", str_data)
    return str_data
    
    
while 1:
        #Cria um socket para tratar a conexao do cliente
     connectionSocket, addr = serverSocket.accept()
     sentence = connectionSocket.recv(1024)
     capitalizedSentence = feistel_cipher(sentence)
     connectionSocket.send(capitalizedSentence)
     connectionSocket.close()