import numpy
class Cipher:
    (text,key,n) = ('','','')
    def __init__(self):# input number to choose a cipher methed
        while True:
            self.n =input("Please choose a cipher method, 1 for Caesar, 2 for Vigenere, 3 for Matrix transposition, 0 to quit:  ")
            if self.n not in ['0','1','2','3']:
                print('invalid input, please try again.')
                continue
            elif self.n == '0': break
            else: self.choose_cipher()

    def choose_cipher(self):# choose to encrypt or decrupt
        while True:
                sign = input("Input 'E' for encryption or 'D' for decrption, '0' to quit: ")
                dict = {'E': 'the plaintext:  ', 'D': 'the ciphertext:  ','0':''}
                if sign not in dict:
                    print('invalid input, please try again.')
                    continue
                if sign == '0': break
                self.text = input("Please input %s"%dict[sign])
                self.key = input("Please input the secret key: ")
                if sign == 'E':
                    if self.n == '1': print(dict['D'],self.Caesar_encrypt())
                    elif self.n == '2': print(dict['D'],self.Vigenere_encrypt())
                    elif self.n == '3': print(dict['D'],self.Matrix_transposition_encrypt())
                elif sign == 'D':
                    if self.n == '1': print(dict['E'],self.Caesar_decrypt())
                    elif self.n == '2': print(dict['E'],self.Vigenere_decrypt())
                    elif self.n == '3': print(dict['E'],self.Matrix_transposition_decrypt())

    def Caesar_encrypt(self):
        return  ''.join([chr((ord(item) +int(self.key) - 65) % 26 + 65) for item in self.text])
        # use the related askII code to calculate
    def Caesar_decrypt(self):
        return ''.join([chr((ord(item) - int(self.key) - 65) % 26 + 65) for item in self.text])

    def Vigenere_encrypt(self):
        Gen_Key = [self.key[i % len(self.key)] for i in range(len(self.text))]
        # repeat letter of key to the length of plain text
        return ''.join([chr((ord(Gen_Key[i]) + ord(self.text[i]) - 130) % 26 + 65) for i in range(len(self.text))])
        # use askII code to calculate swift times

    def Vigenere_decrypt(self):
        Gen_Key = [self.key[i % len(self.key)] for i in range(len(self.text))]
        return ''.join([chr((ord(self.text[i]) - ord(Gen_Key[i])) % 26 + 65) for i in range(len(self.text))])

    def Matrix_transposition_encrypt(self):
        gen_String = [i for i in self.text.ljust(len(self.text) + len(self.key) - len(self.text) % len(self.key)).replace(' ', '%')]
        # fill space with %
        gen_Matrix = numpy.array(gen_String).reshape(int(len(gen_String) / len(self.key)), len(self.key)).T
        # map the string into matrix and return its transpose
        return ''.join([''.join(gen_Matrix[int(i) - 1]) for i in self.key])
        # get text follow the key sequence

    def Matrix_transposition_decrypt(self):
        rows = int(len(self.text) / len(self.key))
        CT = [self.text[i:i + rows] for i in range(0, len(self.text), rows)]  # map string into matrx
        sort = [self.key.index(str(i + 1)) for i in range(len(self.key))]
        PT = [[j for j in CT[i]] for i in sort]  # resort follow the sequence of key
        PT = numpy.array(PT).T  # get PT's transpose
        return ''.join([''.join(PT[i]) for i in range(len(PT))]).replace('%', ' ').strip()

if __name__ == '__main__':
    a = Cipher()
