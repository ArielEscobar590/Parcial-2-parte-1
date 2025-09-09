import tkinter as tk
from tkinter import messagebox

class Concurso:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Eleccion de la Reina de la Independencia 2025")
        self.ventana.geometry("500x300")
        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Evaluacion de la Independencia 2025",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Registrar candidatas", command=self.registrar_candidata)
        opciones.add_command(label="Registrar Jurado", command=self.registrar_jurado)
        opciones.add_command(label="Listar Bandas", command=self.calcular_puntaje)
        opciones.add_command(label="Guardar", command=self.guardar)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def registrar_candidata(self):
        print("Se abrió la ventana: Registrar Candidata")
        tk.Toplevel(self.ventana).title("Registrar Candidata")

    def registrar_jurado(self):
        print("Se abrió la ventana: Registrar Jurado")
        tk.Toplevel(self.ventana).title("Registrar Jurado")

    def calcular_puntaje(self):
        pass

    def guardar(self):
        pass

if __name__ == '__main__':
    Concurso()

class candidata(persona):
    def __init__(self,codigo, nombre, edad,instituto,educativo,municipio):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.instituto = instituto
        self.educativo = educativo
        self.municipio = municipio

    def mostrar(self):
        print(f"Codigo: {self.codigo}Nombre: {self.nombre}- Edad={self.edad}- Instituto={self.instituto}- Educativo={self.educativo}- Municipio={self.municipio}")

class jurador:
    def __init__(self,nombre,especialidad,calificar):
        self.nombre = nombre
        self.especialidad = especialidad
        self.calificar = calificar

    def mostrar(self):
        print(f"Nombre: {self.nombre}- Especialidad={self.especialidad}- Calificar={self.calificar}")

