#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv # importo argv de sys
    suma = 0 # Se tiene que "incializar" suma aca porque sino sale un error cuando hacemos: suma += (int(argv[i]))
    for i in range(1, len(argv)): # Se hace un for para que se sume apartir de la posicion 1 hasta el la cantidad de argumentos
        # que se pasen como comandos en linea.
        suma += (int(argv[i])) # Se va almacenando el valor de la suma en la variable "suma".
    print(f"{suma}") # El pint no esta indentado al bloque del for ya que cuando no se pasa ningun argumento tmb quiero que
    # imprima, en ese caso va a imprimir 0.
