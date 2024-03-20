import hashlib
from math import exp, expm1

ROUNDS = 4
BLOCKSIZE = 8
BLOCKSIZE_BITS = 64
SECRET = "3f788083-77d3-4502-9d71-21319f1792b6"


def encrypt_message(key, message):
    ciphertext = ""
    n = BLOCKSIZE  # 8 bytes (64 bits) per block

    # Split mesage into 64bit blocks
    message = [message[i: i + n] for i in range(0, len(message), n)]

    lengthOfLastBlock = len(message[len(message)-1])

    if ( lengthOfLastBlock < BLOCKSIZE):
        for i in range(lengthOfLastBlock, BLOCKSIZE):
            message[len(message)-1] += " "

    print("PlainText: ", message)

    # generate a 256 bit key based of user inputted key
    key = key_256(key)

    for block in message:
        print ("Block: " + block)

        L = [""] * (ROUNDS + 1)
        R = [""] * (ROUNDS + 1)
        L[0] = block[0:BLOCKSIZE//2]
        R[0] = block[BLOCKSIZE//2:BLOCKSIZE]

        print ("L Initial: " + L[0])
        print ("R Initial: " + R[0])

        for i in range(1, ROUNDS+1):
            L[i] = R[i - 1]
            R[i] = xor(L[i - 1], scramble(R[i - 1], i, key))

        ciphertext += (L[ROUNDS] + R[ROUNDS])

    return ciphertext


def decrypt_cipher(key, ciphertext):
    message = ""
    n = BLOCKSIZE  # 8 bytes (64 bits) per block

    # Split message into 64bit blocks
    ciphertext = [ciphertext[i: i + n] for i in range(0, len(ciphertext), n)]

    lengthOfLastBlock = len(ciphertext[len(ciphertext)-1])

    if ( lengthOfLastBlock < BLOCKSIZE):
        for i in range(lengthOfLastBlock, BLOCKSIZE):
            ciphertext[len(ciphertext)-1] += " "

    # generate a 256 bit key based off the user inputted key
    key = key_256(key)

    for block in ciphertext:
        print ("Block: " + block)
        L = [""] * (ROUNDS + 1)
        R = [""] * (ROUNDS + 1)
        L[ROUNDS] = block[0:BLOCKSIZE//2]
        R[ROUNDS] = block[BLOCKSIZE//2:BLOCKSIZE]

        print ("L Initial: " + L[ROUNDS])
        print ("R Initial: " + R[ROUNDS])

        for i in range(ROUNDS, 0, -1):
            R[i-1] = L[i]
            L[i-1] = xor(R[i], scramble(L[i], i, key))
            # print ("RODADA: ", i)
            # print (" - L: " + L[i])
            # print (" - R: " + R[i])

        message += (L[0] + R[0])

    return message


def key_256(key):
    return hashlib.sha256(key + SECRET.encode("ascii")).hexdigest()


def scramble(x, round, key):
    key = str_to_bin(key)
    x = str_to_bin(str(x))

    key = bin_to_int(key)
    x = bin_to_int(x)

    result = pow((x * key), round)
    result = int_to_bin(result)

    return bin_to_str(result)


def xor(str1, str2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2))


def str_to_bin(s):
    return ''.join('{:08b}'.format(ord(c)) for c in s)


def bin_to_int(s):
    return int(s, 2)


def int_to_bin(i):
    return bin(i)


def bin_to_str(b):
    n = int(b, 2)
    return ''.join(chr(int(b[i: i + 8], 2)) for i in range(0, len(b), 8))


message = "teste123"
encoded = message.encode("ascii")
key = "abcdefgh".encode("ascii")

encrypted_message = encrypt_message(key, message)
print("-> ENCRYPTED: ", encrypted_message)
print("------------------------------------------------------")

decrypted_message = decrypt_cipher(key, encrypted_message)
print("-> DECRYPTED: ", decrypted_message)
