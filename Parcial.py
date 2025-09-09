import tkinter as tk
from tkinter import messagebox, Toplevel


class Candidata:
    def __init__(self):
        self.candidatas = {}
        self.cargar_candidatas()

    def cargar_candidatas(self):
        try:
            with open("candidatas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        codigo, nombre, edad, instituto, municipio = linea.split(":")
                        self.candidatas[codigo] = {
                            "Nombre": nombre,
                            "Edad": edad,
                            "Instituto": instituto,
                            "Municipio": municipio
                        }
            print("Candidatas importadas desde candidatas.txt")
        except FileNotFoundError:
            print("No existe el archivo candidatas.txt, se creará uno nuevo al guardar.")

    def guardar_candidatas(self):
        with open("candidatas.txt", "w", encoding="utf-8") as archivo:
            for codigo, datos in self.candidatas.items():
                archivo.write(f"{codigo}:{datos['Nombre']}:{datos['Edad']}:{datos['Instituto']}:{datos['Municipio']}\n")

    def agregar_candidatas(self, codigo, nombre,edad, instituto, municipio):
        self.candidatas[codigo] = {
            "Nombre": nombre,
            "Edad": edad,
            "Instituto": instituto,
            "Municipio": municipio
        }
        self.guardar_candidatas()
        print(f"Candidata {nombre} agregada y guardado correctamente.")

class Concurso:
    candidata = Candidata()
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
        registro_can = tk.Toplevel(self.ventana)
        registro_can.title("Registro Candidata")
        tk.Label(registro_can, text="Codigo").grid(row=0, column=0)
        codigo = tk.Entry(registro_can)
        codigo.grid(row=0, column=1)
        tk.Label(registro_can, text="Nombre").grid(row=1, column=0)
        nombre = tk.Entry(registro_can)
        nombre.grid(row=1, column=1)
        tk.Label(registro_can, text="Edad").grid(row=2, column=0)
        edad = tk.Entry(registro_can)
        edad.grid(row=2, column=1)
        tk.Label(registro_can, text="Instituto").grid(row=3, column=0)
        institucion = tk.Entry(registro_can)
        institucion.grid(row=3, column=1)
        tk.Label(registro_can, text="Municipio").grid(row=4, column=0)
        municipio = tk.Entry(registro_can)
        municipio.grid(row=4, column=1)

        #candidata.agregar_candidatas(codigo.get(),nombre.get(),edad.get(),institucion.get(),municipio.get())

    def registrar_jurado(self):
        print("Se abrió la ventana: Registrar Jurado")
        tk.Toplevel(self.ventana).title("Registrar Jurado")

    def calcular_puntaje(self):
        pass

    def guardar(self):
        pass



class jurador:
    def __init__(self):
        self.jurado = {}
        self.cargar_jurado()

    def cargar_jurado(self):
        try:
            with open("jurado.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nombre, especialidad = linea.split(":")
                        self.jurado[nombre] = {
                            "Especialidad": especialidad,
                        }
            print("Jurado importadas desde candidatas.txt")
        except FileNotFoundError:
            print("No existe el archivo jurado.txt, se creará uno nuevo al guardar.")

    def guardar_jurado(self):
        with open("jurado.txt", "w", encoding="utf-8") as archivo:
            for nombre, datos in self.jurado.items():
                archivo.write(f"{nombre}:{datos['Especialidad']}\n")

    def agregar_jurado(self, nombre, especialidad):
        self.jurado[nombre] = {
            "Especialidad": especialidad,
        }
        self.guardar_jurado()
        print(f"Jurado {nombre} agregada y guardado correctamente.")

Concurso()