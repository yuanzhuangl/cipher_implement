#Caesar_cipher
#Copyright Yuan-B00755386
import numpy
def Caesar_encrypt(PT,Key):
    return ''.join([chr((ord(a)+Key-65)%26+65) for a in PT])
def Caesar_decrypt(CT,Key):
    return ''.join([chr((ord(a)-Key-65)%26+65) for a in CT])
def Vigenere_encrypt(PT,Key):
    Gen_Key = [Key[i % len(Key)] for i in range(len(PT))]
    return ''.join([chr((ord(Gen_Key[i])+ord(PT[i])-130)%26+65) for i in range(len(PT))])
def Vigenere_decrypt(CT,Key):
    Gen_Key = [Key[i % len(Key)] for i in range(len(CT))]
    return ''.join([chr((ord(CT[i]) - ord(Gen_Key[i]))%26+65) for i in range(len(CT))])
def Matrix_transposition_encrypt(PT,Key):
    gen_String = [i for i in PT.ljust(len(PT)+len(Key)-len(PT)%len(Key)).replace(' ','%')] #fill with %
    gen_Matrix = numpy.array(gen_String).reshape(int(len(gen_String)/len(Key)),len(Key)).T # map the string into matrix and return its transpose
    return ''.join([''.join(gen_Matrix[int(i)-1]) for i in Key]) # get text follow the key sequence
def Matrix_transposition_decrypt(CT,Key):
    rows = int(len(CT)/len(Key))
    CT = [CT[i:i+rows] for i in range(0,len(CT),rows)] # map string into matrx
    sort =[Key.index(str(i+1)) for i in range(len(Key))]
    PT = [[j for j in CT[i]] for i in sort] # resort follow the sequence of key
    PT = numpy.array(PT).T # get PT's transpose
    return ''.join([''.join(PT[i]) for i in range(len(PT))]).replace('%',' ').strip()
if __name__ == '__main__':
    while True :
            n = input("Please choose a cipher method, 1 for Caesar, 2 for Vigenere, 3 for Matrix transposition, 0 to quit: ")
            if n not in ['1','2','3','0']:
                print('invalid input, please try again.')
                continue
            if n == '0':
                break
            while True:
                Implement = input("Input 'E' for encryption or 'D' for decrption: ")
                if Implement=='E':
                    PT = input("Please input the plaintext: ")
                    key = input("Please input the secret key: ")
                    if n == '1':
                        print("The ciphertext: ",Caesar_encrypt(PT.strip(),int(key)))
                        break
                    elif n == '2':
                        print("The ciphertext: ",Vigenere_encrypt(PT.strip(), key.strip()))
                        break
                    elif n == '3':
                        print("The ciphertext: ",Matrix_transposition_encrypt(PT.strip(), key.strip()))
                        break #"security!security!security!", "54123"
                elif Implement=='D':
                    CT = input("Please input the ciphertext: ")
                    key = input("Please input the secret key: ")
                    if n == '1':
                        print("The plaintext: ",Caesar_decrypt(CT.strip(), int(key)))
                        break
                    elif n =='2':
                        print("The plaintext: ",Vigenere_decrypt(CT.strip(), key.strip()))
                        break
                    elif n == '3':
                        print("The plaintext: ",Matrix_transposition_decrypt(CT.strip(), key.strip()))
                        break #"rsiet%u!rsi%sietcyetcyu!cyu!r%","54123"
                else:
                    print('invalid input, please try again.')
                    continue
