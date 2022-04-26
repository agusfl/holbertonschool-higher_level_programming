#!/usr/bin/python3
for i in range(0, 10):
    for j in range((i+1), 10):
        print(f"{i}{j}", end='')
        if i != 8 or j != 9:
            print(end=', ')
        if i == 8 and j == 9:
            print()
