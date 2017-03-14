p = 17
q = 31
M = 5
n = p*q
tmp = (p-1)*(q-1)
print("n=",n)
print("tmp=",tmp)
e = 1
while tmp%e == 0:
       e += 1
print('e=',e)

d=1
while (e*d)%tmp != 1:
    d +=1
print('d=',d)

print("Public Key = (",e,",",n,")")
print("Public Key = (",d,",",n,")")

C=M**e%n
print('C=',C)

exit()


# print(M**e%n)