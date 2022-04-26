#!/usr/bin/python3
for i in range(0, 10):
    for j in range((i+1), 10):
        print(f"{i}{j}", end='')
        if i is not 8 or j is not 9:
            print(end=', ')
        if i == 8 and j == 9:
            print()

# Use la misma logica que en el ejercicio 100-print_comb3.c del directorio: 0x01-variables_if_else_while del repo
# holbertonschool-low_level_programming.
