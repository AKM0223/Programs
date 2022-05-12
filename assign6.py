from Crypto.Cipher import AES
def paddedKey(key):
    while len(key) % 8 !=0:
        key +=' '
    return key
def paddedText(text):
    while len(text) % 16 != 0:
        text += ' '
    return text
plain_input = input("Enter the text to be encrypted: ")
print(plain_input)
print(len(plain_input))
plain = paddedText(plain_input)
print(plain)
print(len(plain))
key_input = input("Enter in a key between 16 and 32 characters: ")
print(key_input)
print(len(key_input))
key = paddedKey(key_input)
print(key)
print(len(key))
cipher = AES.new(key.encode('utf8'),AES.MODE_ECB)
ciphertext = cipher.encrypt(plain.encode('utf8'))
print("Cipher Text:%r"%ciphertext)
cleartext = cipher.decrypt(ciphertext),
print("Clear Text:%r"%cleartext)