from utils import Utils

ROUNDS = 4
BLOCKSIZE = 8
SECRET = "1PVDqIGvPgkwbKPcgwwBm"
KEY = "jMlEA2zYbtnh4i7wpvpVa".encode("ascii")

class Cipher:
    def __init__(self, rounds = ROUNDS, blocksize = BLOCKSIZE, secret = SECRET, key = KEY):
        self.rounds = rounds
        self.blocksize = blocksize
        self.secret = secret
        self.key = key
    
    def encrypt(self, message):
        ciphertext = ""
        n = self.blocksize

        message = [message[i: i + n] for i in range(0, len(message), n)]

        lengthOfLastBlock = len(message[len(message)-1])

        if ( lengthOfLastBlock < self.blocksize):
            for i in range(lengthOfLastBlock, self.blocksize):
                message[len(message)-1] += " "

        key = Utils.key_256(self.secret, self.key)

        for block in message:
            L = [""] * (self.rounds + 1)
            R = [""] * (self.rounds + 1)
            L[0] = block[0:self.blocksize//2]
            R[0] = block[self.blocksize//2:self.blocksize]

            for i in range(1, self.rounds+1):
                L[i] = R[i - 1]
                R[i] = Utils.xor(L[i - 1], Utils.scramble(R[i - 1], i, key))

            ciphertext += (L[self.rounds] + R[self.rounds])

        return ciphertext
    
    def decrypt(self, chiper_text):
        message = ""
        n = self.blocksize

        chiper_text = [chiper_text[i: i + n] for i in range(0, len(chiper_text), n)]

        last_block_len = len(chiper_text[len(chiper_text)-1])

        if ( last_block_len < self.blocksize):
            for i in range(last_block_len, self.blocksize):
                chiper_text[len(chiper_text)-1] += " "

        key = Utils.key_256(self.secret, self.key)

        for block in chiper_text:
            L = [""] * (self.rounds + 1)
            R = [""] * (self.rounds + 1)
            L[self.rounds] = block[0:self.blocksize//2]
            R[self.rounds] = block[self.blocksize//2:self.blocksize]

            for i in range(self.rounds, 0, -1):
                R[i-1] = L[i]
                L[i-1] = Utils.xor(R[i], Utils.scramble(L[i], i, key))

            message += (L[0] + R[0])

        return message
