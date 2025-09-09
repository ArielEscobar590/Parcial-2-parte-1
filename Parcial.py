
Dic_candidata={}
Dic_jurado={}
class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}- Edad={self.edad}")
class candidata(persona):
    def __init__(self,codigo, nombre, edad,instituto,municipio):
        super().__init__(nombre, edad)
        self.codigo = codigo
        self.instituto = instituto
        self.municipio = municipio

    def mostrar(self):
        print(f"Codigo: {self.codigo}Nombre: {self.nombre}- Edad={self.edad}- Instituto={self.instituto}- Municipio={self.municipio}")


    def ingrear_candidatas(self):
        codigo=input("Ingrese el codigo de la candidata: ")
        nombre=input("Ingrese el nombre: ")
        edad=int(input("Ingrese el edad: "))
        instituto=input("Ingrese el instituto: ")
        municipio=input("Ingrese el municipio: ")

        c=candidata(codigo,nombre,edad,instituto,municipio)
        c.ingrear_candidatas()
        Dic_candidata[codigo]=c




class jurador:
    def __init__(self,nombre,especialidad,calificar):
        self.nombre = nombre
        self.especialidad = especialidad
        self.calificar = calificar

    def mostrar(self):
        print(f"codigo: {self.nombre}- Especialidad={self.especialidad}- Calificar={self.calificar}")

    def ingreso_jurado(self):
        nombre=input("Ingrese el nombre: ")
        especialidad=input("Ingrese el especialidad: ")
        calificar=int(input("Ingrese el calificar: "))

        j=jurador(nombre,especialidad,calificar)
        j.ingreso_jurado()
        Dic_jurado[nombre]=j

class eleccion_c:
    CRITERIOS_VALIDOS = ["Cultura general", "Proyección escénica", "Entrevista"]

    def __init__(self, candidata, categoria):
        self.candidata = candidata
        self._categoria = categoria
        self._puntajes = {}

    def registrar_puntajes(self, puntajes: dict):
        if set(puntajes.keys()) != set(eleccion_c.CRITERIOS_VALIDOS):
            raise ValueError("Faltan o sobran criterios de evaluación.")

        for criterio, valor in puntajes.items():
            if not (0 <= valor <= 10):
                raise ValueError(f"Puntaje inválido en {criterio}. Debe estar entre 0 y 10.")
        self._puntajes = puntajes

    def total(self):
        return sum(self._puntajes.values()) if self._puntajes else 0

    def mostrar_resultado(self):
        print(f"Resultado de {self.candidata.nombre} ({self._categoria}): {self.total()} puntos")