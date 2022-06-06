#!/usr/bin/python3
"""
Module for creating a class: Base
"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increment class attribute __nb_objects if there is
        no id and set it as id.
        This class will be the “base” of all other classes in this project.
        The goal of it is to manage id attribute in all your future classes and
        to avoid duplicating the same code (by extension, same bugs)"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON is one of the standard formats for sharing data representation.
        Update the class Base by adding the static method
        def to_json_string(list_dictionaries -> dictionary): that returns the
        JSON string representation of list_dictionaries static method es un
        metodo que se puede usar por fuera de la clase, es parecido a definir
        una funcion normal.
        """
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = [] # si es None o esta vacia, ponemos lo que nos indica la condicion de letra devolver el string dentro de []
        return json.dumps(list_dictionaries) # esto retorna el objeto json en formato string

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation of list_objs
        to a file.
        A classmethod it can access class attributes, but not the instance
        attributes.
        Lo que se hace en esta funcion es cargar los objetos dentro de una
        lista, convertir esa lista de objetos en una lista de diccionarios
        y mandar dicha lista como argumento a la funcion "to_json_string"
        que creamos mas arriba, luego guardamos esto en el filename.
        """
        # El argumento "cls" hace referencia a la clase del objeto y el argumento "list_objs" es una lista de objetos (isntancias)
        # que heredan de la clase Base, por lo tanto pueden ser de clase: Rectangle o Square.
        filename = f"{cls.__name__}.json" # Le asignamos el nombre de la clase al filename (tal cual nos pide la letra)
        new_list = [] # Se crea una lista vacia para cargar los datos o para devolver la lista vacia en caso de que list_objs sea None.

        if list_objs is not None:
            for object in list_objs:
                new_list += [object.to_dictionary()]
        
        # Se hace primero un if para chequear que la lista que se pasa como argumento (list_objs) no sea None ni este vacia.
        # En dicho caso se hace un for para por cada objeto se vaya agregando a la nueva lista (new_list) en forma de diccionario,
        # por eso usamos el metodo "to_dictionary()" que creamos tanto en la clase Rectangle como en la clase Square.

        json_list_dict = Base.to_json_string(new_list)
        # Aca creamos una variable "json_list_dict" donde usamos la funcion creada "to_json_string" en la task anterior.

        with open(filename, "w", encoding="UTF-8") as f:
            f.write(json_list_dict)
        # Ahora abrimos el archivo (filename) en modo escritura y le escribimos en el filename lo que acabamos
        # de guardar dentro de la variable "json_list_dict".
    
    @staticmethod
    def from_json_string(json_string):
        """
        Create a static method that returns the list of the JSON string
        representation "json_string".
        Aca se pasa de un json_string a una lista de python.
        Se devuelve una lista de Python.
        """
        import json

        if json_string is None or len(json_string) == 0:
            json_string = "[]" # En caso de que json_string este vacio o sea None se devuelve una lista vacia.
        return json.loads(json_string) # De lo contrario devolvemos lo que este en json_string pasado a una lista de Python.

    @classmethod
    def create(cls, **dictionary):
        """
        This is a class method that returns an instance (object) with all
        attributes already set.
        Inside "**dictionary" are the keys and values to set to the new
        instance.
        We are going to use the method "update" that was created in the other
        classes (Rectangle and Square).
        """
        if "size" in dictionary:
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        real_values = dummy
        return real_values

# En la task 18 se nos pide que agregemos a la clase "Base" un class method para crear
# objetos de la clase Square o Rectangle y setearle los atributos que se le pase como argumento
# en **dictionary (que seria **kwargs), para hacer esto vamos a usar el metodo "update" que creamos
# tanto en la clase Rectangle como en la clase Square.
# Primero que nada hacemos un if para chequear si el atributo "size" esta dentro del diccionario que nos pasen
# como argumento, en caso de que "size" se encuentre en "dictionary" ya sabemos que lo que se quiere crear
# va a ser una clase de tipo Square (ya que esta es la que tiene el atributo "size").
# Por lo tanto dentro del if creamos una variable "dummy", la variable podria tener cualquier nombre, se suele decir
# que es de tipo dummy cuando es una variable "ficticia" "simple" "tonta", como en este caso que se usa solo para crear
# la instancia con los atributos mandatorios que hay que pasar si o si para crear una clase, en el caso
# de Square se le tiene que pasar el "size" (le puse 1 como valor pero se podria poner cualquier otro numero) ya que las otras
# variables tienen valores asignados que van a tomar a no ser que se le pasen otros valores cuando se crea la clase, este es el
# init de la clase Square: def __init__(self, size, x=0, y=0, id=None):
# Podemos ver que la 'x' y la 'y' tomarian el valor 0 si no se pasa otro y la id el valor 'None' en caso que no se pase otro.
# Para crear la clase se llama con "cls" ya que cls representa la clase correspondiente que quieren crear (Rectangle o Square) que indiquen
# en el main cuando van a llamar al metodo "create".
# Necesitamos hacer todo esto de crear la variable "dummy" para poder usar el metodo update() ya que dicho metodo lo definimos como un "instance method"
# dentro de las clases: Rectangle y Square, y como son metodos de instancia para poder llamarlos necesitamos tener una isntancia (objeto) de dicha clase primero.
# Continuando con la explicacion del resto del codigo, se entraria en el "else" en caso de que no este el atributo "size" dentro
# del "dictionary", por lo tanto en este caso estariamos hablando de crear una clase de tipo "Rectangle" y como a la misma hay que
# pasarle los atributos "width" y "height" se los seteo en 1 a ambos inicialmente, despues con el update se los va a modificar a los
# valores que le pase el usuario dentro del argumento "dictionary". esto funciona igual para la clase Square.
# El resto de la explicacion para Rectangle es igual que lo que ya explique para Square.
# Por ultimo se retorna la variable "real_values" que tiene los valores que se le asignaron en el main y no los valores de la variable dummy, claramente podria
# retornar directo --> dummy.update(**dictionary) - en lugar de guardarlo dentro de la variable "real_values" pero de esta forma me parece que queda mas claro
# el codigo.

    @classmethod
    def load_from_file(cls):
        """
        class method that returns a list of instances.
        - The filename must be: <Class name>.json - example: Rectangle.json
        - If the file doesn’t exist, return an empty list
        - Otherwise, return a list of instances - the type of these instances
        depends on cls (current class using this method).
        - You must use the from_json_string and create methods (implemented
        previously).
        """
        filename = f"{cls.__name__}.json" # Se crea el archivo con el nombre de la clase correspondiente que se pase como argumento y la extension .json (tal cual indica la letra).
        instances_list = [] # Creamos una lista vacia donde vamos a ir guardando la lista de instancias (objetos) que vamos a retornar.

        # Se hace un try y except por si el archivo que se pasa no se encuentra (FileNotFoundError), en la exception pongo "Exception" porque es el generico que "agarra" cualquier excepcion que se levante.
        try:
            with open(filename, mode="r+", encoding="UTF-8") as f:
                raw_json = f.read()
            list_of_dicts = cls.from_json_string(raw_json)
            for instance in list_of_dicts:
                instances_list.append(cls.create(**instance))
        except Exception:
            pass
        return instances_list

        # Primero en el try, abrimos el archivo con open (usamos tmb "with" para que se encargue de cerrar el archivo correctamente una vez que lod ejemos de usar)
        # lo abrimos al "filename" (que va a ser la clase que pasen, con la extencion .json, ejemplo: Rectangle.json) en modo lectura (r)
        # y usamos el metodo "read()" para leer lo que tenga adentro, eso lo guardamos en una variable llamada "raw_json" (que seria informacion sin procesar).
        # Luego creamos una variable llamada "list_of_dicts" a la cual le vamos a asignar mediante el uso de la funcion que creamos anteriormente "from_json_string"
        # lo que este en "raw_json" lo pasamos a una lista de python para poder trabajar con esa data.
        # Despues se hace un for donde se va a iterar cada "instancia" que se encuentre en la lista que creamos recien "list_of_dicts" y en cada iteracion
        # vamos a ir creando y guardando con el metodo append las instancias con el metodo que creamos anteriormente "create" y las guardamos en la lista vacia
        # que habiamos creado "instances_list", la creamos vacia ya que si el archivo no existe en la letra nos pedian que retornemos una lista vacia, en caso de
        # que se pase un archivo que no existe, va a ir al except y como tiene un pass, no va a hacer nada y va a ir al return y devolver la lista vacia.
        # Por ultimo retornamos la lista con todas las instancias.

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        class method that writes the JSON string representation of list_objs
        to a csv file.
        We use the csv module to work with a csv file.
        """
        import csv # importamos el modulo csv, ver info del mismo en: https://docs.python.org/3/library/csv.html

        filename = f"{cls.__name__}.csv" # se define al filename como el nombre de la clase pero con la extension: csv en lugar de json

        with open(filename, "w", newline='') as f:
            writer = csv.writer(f)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height, obj.x,
                                        obj.y])

    # En el with y open indicamos que vamos a abrir el "filename" en modo escritura, lo del newline='' se pasa para que no quede una linea en blanco entre textos y solo al final.
    # Luego hacemos una variable "writer" en la cual le asignamos para que use el metodo "writer" del modulo "csv" para poder escribir dentro del archivo "filename".
    # Validamos que la lista de objetos (list_objs) que pasen como argumento no sea None y hacemos un for para escribir cada objeto (obj) que este dentro de list_objs usando la
    # variable que creamos "writer", despues diferenciamos entre si el nombre de la clase es "Square" o " Rectangle" ya que Square solo tiene "size" y Rectangle "width" y "height".
    # Para cada clase le ponemos el orden que nos indicane en la letra para el format del csv, que seria:
    # Rectangle: <id>,<width>,<height>,<x>,<y>
    # Square: <id>,<size>,<x>,<y>
    
    @classmethod
    def load_from_file_csv(cls):
        """
        class method that returns a list of instances in csv format.
        Aca vamos a serializar y deserializar archivos con formatos csv en lugar de JSON.
        """
        import csv # importamos el modulo csv, ver info del mismo en: https://docs.python.org/3/library/csv.html

        filename = f"{cls.__name__}.csv"
        objs_list = []

        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            if filename is not None:
                for row in reader:
                    if cls.__name__ == "Square":
                        dic = {"id": int(row[0]), "size": int(row[1]),
                               "x": int(row[2]), "y": int(row[3])}
                    if cls.__name__ == "Rectangle":
                        dic = {"id": int(row[0]), "width": int(row[1]),
                               "height": int(row[2]), "x": int(row[3]),
                               "y": int(row[4])}
                    obj = cls.create(**dic)
                    objs_list.append(obj)
        return objs_list

    # Tanto esta funcion como la de "save_to_file_csv" son muy parecidas en lo que respecta a la logica con las que ya habiamos creado para formato JSON.
    # En este caso vamos a usar el metodo "reader" del modulo csv para poder leer del archivo "filename".
    # Igual que en el caso anterior, le indicamos dependiendo de si la clase es "Square" o "Rectangle" como es que va a tener que cargar (load) la informacion.
    # Casteamos los valores a "int" ya que antes estaban en formato "str" y usamos el metodo "create" que habiamos hecho anteriormente para crear una lista de instancias (objetos).
    # Luego lo vamos agregando con append() en la lista vacia que habiamos creado "objs_list" y que vamos a retornar.