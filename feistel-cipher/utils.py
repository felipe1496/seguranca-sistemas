import hashlib

class Utils:
    @staticmethod
    def scramble(x, round, key):
        key = Utils.str_to_bin(key);
        x = Utils.str_to_bin(str(x));

        key = Utils.bin_to_int(key);
        x = Utils.bin_to_int(x);

        result = pow((x * key), round);
        result = Utils.int_to_bin(result);

        return Utils.bin_to_str(result);

    @staticmethod
    def xor(str1, str2):
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2))
    
    @staticmethod
    def str_to_bin(s):
        return ''.join('{:08b}'.format(ord(c)) for c in s)
    
    @staticmethod
    def bin_to_int(s):
        return int(s, 2)
    
    @staticmethod
    def int_to_bin(i):
        return bin(i)
    
    @staticmethod
    def bin_to_str(b):
        n = int(b, 2)
        return ''.join(chr(int(b[i: i + 8], 2)) for i in range(0, len(b), 8))

    @staticmethod
    def key_256(secret, key):
        return hashlib.sha256(key + secret.encode("ascii")).hexdigest()
    