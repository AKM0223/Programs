import pyDes
data=input("enter plain text for encryption")
key=input("enter 16/24 byte string for key generation")
k=pyDes.triple_des(key,padmode=pyDes.PAD_PKCS5)
e=k.encrypt(data)
print("cipher text:%r"%e)
print("plain text:%r"%k.decrypt(e))