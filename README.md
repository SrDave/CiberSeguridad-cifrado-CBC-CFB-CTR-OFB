# Cifrado AES modo CBC CFB CTR y OFB a partir de ECB

## Puntos abordados:

1. Definir el texto a cifrar. En este punto, hay que escoger un texto cuyo tamaño sea múltiplo del tamaño de bloque de AES (que es de 16 bytes). Además, y puesto que el primer bloque en los diferentes modos de funcionamiento se realiza de manera diferente, el número de bloques a cifrar debe ser de dos como mínimo. Un ejemplo de definición de un mensaje en formato bytes que ocupa justo tres bloques a cifrar por AES es el siguiente:
    
    `x=b’a’*48`

2. Cifrar dicho texto mediante el cifrador AES en modo OFB, CTR, CBC y CFB definido en la biblioteca cryptography de Python.
3. Emplear el cifrador AES en modo ECB definido en cryptography como bloque básico para construir el esquema relativo al cifrado del modo de funcionamiento OFB, CTR, CBC y CFB.

Como se puede observar, OFB consiste en cifrar, para el primer bloque de 16 bytes del texto claro, el vector de inicialización (IV) con AES en modo ECB y con la clave k. El resultado de dicho cifrado (que conviene que almacene en una variable, por ejemplo, s) debe sumarse en módulo 2 con el primer bloque de texto claro, lo que proporciona el primer bloque de texto cifrado. Para los siguientes bloques, el funcionamiento es diferente, en cuanto a que la entrada al cifrador AES en modo ECB debe ser el resultado del cifrado AES ECB del bloque anterior (que se ha almacenado en una variable s). Además, recuerde que para realizar la suma módulo 2 puede emplear la siguiente función:

`
def xor_bytes(key_stream, message):
length = min(len(key_stream), len(message))
return bytes([key_stream[i] ^ message[i] for i in range(length)])
`

5. Comparar los resultados de los pasos 2 y 3.
A continuación, se le proporcionan algunas indicaciones para la realización del modo CTR a partir del modo ECB. Puesto que la implementación de dicho modo en cryptography emplea un IV y a partir de dicho IV inicial va incrementando con un contador dicho valor como entrada al cifrador AES, es necesario conocer la manera para convertir entre valores enteros y bytes, puesto que el incremento no es posible realizarlo sobre bytes sino sobre valores enteros. Esta conversión podemos realizarla mediante las siguientes dos funciones:

`
def int_to_bytes(i):
return i.to_bytes(16, byteorder='big')
def bytes_to_int(b):
return int.from_bytes(b, byteorder='big')
`

Nótese que el valor de 16 en la función `int_to_bytes` se debe a que requerimos que el resultado de transformar un valor a bytes ocupe justo el tamaño de bloque AES, esto es, 16 bytes.
