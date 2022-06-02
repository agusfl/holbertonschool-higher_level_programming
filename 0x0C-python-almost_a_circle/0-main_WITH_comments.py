#!/usr/bin/python3
""" 0-main """
from models.base import Base
# Aca lo que se hace es importar la calse "Base" desde el
# la carpeta "models" ya que nuestro archivo "base.py" esta dentro de la 
# carpeta models, para importarlo hay que ponerle: models.base y
# despues ponemos el nombre de la clase que queremos importar, en este caso es Base.

if __name__ == "__main__":

    b1 = Base() 
    # Este es un caso en el que no le pasamos ningun argumento, por lo tanto "id" es None
    # entonces queremos que se le asigne el incremento que se ponga en el atributo privado
    # que definimos para la clase Base que se llama: __nb_objects.
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    # En este caso si le pasamos un argumento, por lo tanto no es None, entonces queremos que
    # se le asigne el id que le hayamos pasado, en este caso puntual seria: 12
    print(b4.id)

    b5 = Base()
    print(b5.id)
