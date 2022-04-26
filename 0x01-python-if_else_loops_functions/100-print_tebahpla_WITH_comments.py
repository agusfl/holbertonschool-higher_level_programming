#!/usr/bin/python3
for i in range(0, 26):
    ch = ord('z') - i
    if i % 2 == 1:
        ch = chr(ch - ord('a') + ord('A'))
    else:
        ch = chr(ch)
    print(f"{ch}", end='')

# Hacemos un for para que se itere por todas las letras del abecedario, despues creamos una variable llamada 'ch'
# a la misma la definimos como ord('z') - i -> ord('z') como ya vimos es una funcion que trae el numero ascii correspondiente
# al valor del caracter 'z' y le restamos la variable 'i' para que vayamos teniendo todas las letras del abecedario de la 'z'
# a la 'a' ya que al principio ch seria = 122 (valor de 'z') - 0 (ya que i al principio arranca en 0) y despues en la proxima
# iteracion seria: ch = 122 - 1 = 121 que es la: 'y'.
# Despues indicamos que si el modulo de 'i' es 1 siginifica que no es par por lo tanto queremos que se imprima en mayuscula
# por eso pasamos la variable 'ch' a mayuscula.
