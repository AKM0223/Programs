n=int(input("enter prime number(n)"))
g=int(input("enter base prime number(g)"))
alicesecret=int(input("enter Alice secret key(x)"))
bobsecret=int(input("enter Bob secret key(y)"))
print("publicly shared prime(n):",n)
print("publicly shared prime(g):",g)
print("Alice Secret key:",alicesecret)
print("Bob Secrete key:",bobsecret)
#Alice sends number A to Bob A=g^x mod n
A=(g**alicesecret)% n
print("\n Alice sends (A) to Bob:",A)
#Bob sends number B to Alice B=g^y mod n
B=(g**bobsecret)% n
print("\n Bob sends (B) to Alice:",B)
#Alice computes shared secret key K1=B^x mod n
alicesecretkey=(B**alicesecret)%n
print("\n Alice shared secret:",alicesecretkey)
#Bob computes shared secret key K2=A^y mod n
bobsecretkey=(A**bobsecret)%n
print("\n Bob shared secret:",bobsecretkey)