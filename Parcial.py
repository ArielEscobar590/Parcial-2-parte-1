
Dic_candidata={}
class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}- Edad={self.edad}")
class candidata(persona):
    def __init__(self,codigo, nombre, edad,instituto,educativo,municipio):
        super().__init__(nombre, edad)
        self.codigo = codigo
        self.instituto = instituto
        self.educativo = educativo
        self.municipio = municipio

    def mostrar(self):
        print(f"Codigo: {self.codigo}Nombre: {self.nombre}- Edad={self.edad}- Instituto={self.instituto}- Educativo={self.educativo}- Municipio={self.municipio}")


    def ingrear_candidatas(self):
        cod=input("Ingrese el codigo de la candidata: ")
        nombre=input("Ingrese el nombre: ")
        edad=int(input("Ingrese el edad: "))
        instituto=input("Ingrese el instituto: ")
        educativo=input("Ingrese el educativo: ")
        municipio=input("Ingrese el municipio: ")



class jurador:
    def __init__(self,nombre,especialidad,calificar):
        self.nombre = nombre
        self.especialidad = especialidad
        self.calificar = calificar

    def mostrar(self):
        print(f"Nombre: {self.nombre}- Especialidad={self.especialidad}- Calificar={self.calificar}")

