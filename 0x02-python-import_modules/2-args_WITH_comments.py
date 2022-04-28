#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv # El modulo "sys" tiene la funcion "argv" que tiene como una "lista" con todos los comandos
    # en linea que se pasen.
    # Hago las distintas condiciones para imprimir tal cual nos indican en la letra.
    if len(argv) == 1:
        print(f"0 arguments.")
    elif len(argv) == 2:
        print(f"{len(argv) - 1} argument:") # len(argv) nos da la cantidad de argumentos pasados en linea.
        # Aca se le resta 1 porque lo que va en la posicion 0 te lo pone como 1.
        print(f"{len(argv) - 1}: {argv[1]}")
    elif len(argv) > 2:
        print(f"{len(argv) - 1} arguments:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")
