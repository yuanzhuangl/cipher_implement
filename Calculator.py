# calculate key by p&q (for task 3)
import re
(p,q,M)=(re.compile('\d+').findall(input("input p,q and M : ")))  # 17,31,5
(n,n_) = (int(p) * int(q), (int(p) - 1) * (int(q) - 1))

print("p*q = ",n,"    (p-1)(q-1) = ",n_)
(e,d)= (1,1)
while n_%e == 0: e += 1
while (e*d)%n_ != 1: d +=1
print('e=',e,'\nd=',d)
print("Public Key = (",e,",",n,")\nPrivate Key = (",d,",",n,")\nC = ",int(M)**e%n)