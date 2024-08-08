# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 17:46:49 2023

@author: colmi
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os


def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])
# Definir el texto claro

text = b'a'*48

# Generar una clave y un vector de inicialización (IV) aleatorios
key = os.urandom(16)
iv = os.urandom(16)




cipherCBC = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor_CBC = cipherCBC.encryptor()
decryptor_CBC = cipherCBC.decryptor()
print(encryptor_CBC.update(text).hex())



# Crear el cifrador AES en modo ECB
cipher = Cipher(algorithms.AES(key), modes.ECB())
cifrador = cipher.encryptor()
#print(cifrador.update(text).hex())

y = iv
ciphertextCFB = ''

# Dividir el texto claro en bloques de 16 bytes y cifrarlos en modo CBC
for i in range(0, len(text), 16):
    block = text[i:i + 16]
    t = xor_bytes(y,block)
    y = cifrador.update(t)  
    ciphertextCFB += y.hex()
    

print(ciphertextCFB)


