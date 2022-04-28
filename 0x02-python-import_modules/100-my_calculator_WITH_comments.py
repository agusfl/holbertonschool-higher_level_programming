#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div # importamos el modulo que creamos como hicimos en los ejs anteriores
    from sys import argv # importamos el argv del modulo sys
    if (len(argv) - 1) != 3: # Ponemos -1 ya que te cuenta la posicion 0 que seria el ejecutable y como no queremos
        # que se cuente le restamos 1. La condicion la ponemos si es distinto de 3 ya que se le tienen que pasar
        # como comandos en linea a nuestro programa solo 3 argumentos, van a ser: el primer argumento va a ser el
        # primer numero que queres operar luego el operador que queres usar siendo: +, -, *, / y el tercer argumento
        # va a ser el tercer numero a operar.
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1) # Con esto le indicamos que salga con valor de 1 (para saber que fue un error) para ver en la consola
        # con que valor salio se usa: echo $? | en este caso hay que poner: ./100-my_calculator.py ; echo $? (con el
        # ; (punto y coma) se le pasa mas de un comando a la shell.
    a = int(argv[1]) # casteamos el primer argumento (que va a ser el primer numero que se pase) a int para que tmb
    # nos tome si se pasa: '5' (que seria un string pero lo casteamos a int (es como que lo transformamos)).
    b = int(argv[3]) # aca casteamos el tercer argumento ya que este seria el segundo numero porque el segundo argumento
    # va a ser el operador que se pase (+, - , * o /).
    operator = argv[2]
    if operator == "+":
        print(f"{a} {operator} {b} = {add(a,b)}")
    elif operator == "-":
        print(f"{a} {operator} {b} = {sub(a,b)}")
    elif operator == "*":
        print(f"{a} {operator} {b} = {mul(a,b)}")
    elif operator == "/":
        print(f"{a} {operator} {b} = {div(a,b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
