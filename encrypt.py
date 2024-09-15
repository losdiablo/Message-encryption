import random
import string

chars= " " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
print(chars)
print("******************************************************")
print(key)
text=input()
encryptedText=""
for letter in text:
    index=chars.index(letter)
    encryptedText+=key[index]
print("******************************************************")
print(encryptedText)

 