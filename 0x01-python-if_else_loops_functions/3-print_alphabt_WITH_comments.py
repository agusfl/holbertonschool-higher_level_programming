#!/usr/bin/python3
for i in range (97, 123):
    if i == 101 or i == 113: # 101 es la letra 'e' en ascii y 113 la 'q', en caso que sea cualquiera de esas dos letras
        # no quiero que las imprima por eso pongo un continue.
        continue
    else:
        print(f"{chr(i)}", end='')

# Otra opcion era usar el operador: 'not' poniendo: if i is not 101 and i is not 113:
