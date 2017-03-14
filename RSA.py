#calculate the ciphertext by RSA
#copywright Yuan B00755386
import re
m = int(input("Please input an integer as message M: "))
key = input("please input the secret key (e,n): ")
pattern = re.compile(r'\d+')
f = lambda x:int(x)
(e,n)=(pattern.findall(key))
print("C = ", m**f(e)%f(n))