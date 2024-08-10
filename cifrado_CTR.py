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

def int_to_bytes(i):
    return i.to_bytes(16, byteorder='big')

def bytes_to_int(b):
    return int.from_bytes(b, byteorder='big')

# Definir el texto claro
text = b'a'*48

# Generar una clave y un vector de inicialización (IV) aleatorios
key = os.urandom(16)
iv = os.urandom(16)




cipherCTR = Cipher(algorithms.AES(key), modes.CTR(iv))
encryptor_CTR = cipherCTR.encryptor()
print(encryptor_CTR.update(text).hex())



# Crear el cifrador AES en modo ECB
cipher = Cipher(algorithms.AES(key), modes.ECB())
cifrador = cipher.encryptor()
#print(cifrador.update(text).hex())

# Generar un contador inicial
contador = iv

ciphertextCTR = ''

# Dividir el texto claro en bloques de 16 bytes y cifrarlos en modo CTR
for i in range(0, len(text), 16):

    keystream = cifrador.update(contador)
    block = text[i:i + 16]
    ciphertext_block = xor_bytes(keystream, block)
    contador = bytes_to_int(contador)
    ciphertextCTR += ciphertext_block.hex()
    contador += 1
    contador = int_to_bytes(contador)


print(ciphertextCTR)


