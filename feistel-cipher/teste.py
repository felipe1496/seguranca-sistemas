
def rand_key(p):
     
    import random
    key1 = ""
    p = int(p)
     
    for i in range(p):
         
        temp = random.randint(0,1)
        temp = str(temp)
        key1 = key1 + temp
         
    return(key1)

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
        for i in range(n): 
            if (a[i] == b[i]):
                temp += "0"
            else: 
                temp += "1"
        return temp 

    L1 = PT_Bin[0:n]
    R1 = PT_Bin[n::]
    m = len(R1)

    K1= rand_key(m)

    K2= rand_key(m)
  

    # first round of Feistel
    f1 = exor(R1,K1)
    R2 = exor(f1,L1)
    L2 = R1

    # Second round of Feistel
    f2 = exor(R2,K2)
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
    print("tamanho: ", len(str_data))
    return str_data

message = "felipeakfjlkjfsdlkjfsdfd"
encoded = message.encode("ascii")

print("retorno: ", feistel_cipher(encoded))
