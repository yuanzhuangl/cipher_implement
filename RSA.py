#calculate the ciphertext by RSA
#copywright Yuan B00755386
import re
(M,e,n)=(re.compile(r'\d+').findall(input("Please input message M and secret key (e,n): ")))
#get input message
print("C = ", int(M)**int(e)%int(n))