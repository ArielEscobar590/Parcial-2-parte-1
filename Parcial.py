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
        self.clientes[codigo] = {
            "Nombre": nombre,
            "Edad": edad,
            "Instituto": instituto,
            "Municipio": municipio
        }
        self.guardar_candidatas()
        print(f"Candidata {nombre} agregada y guardado correctamente.")

    def mostrar_todos(self):
        if self.clientes:
            print("\nLista de clientes:")
            for codigo, datos in self.candidatas.items():
                print(f"\nCodigo: {codigo}")
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
        else:
            print("No hay Candidatas registrados.")


class Concurso:
    #candidata = Candidata()
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
    def __init__(self,nombre,especialidad,calificar):
        self.nombre = nombre
        self.especialidad = especialidad
        self.calificar = calificar

    def mostrar(self):
        print(f"Nombre: {self.nombre}- Especialidad={self.especialidad}- Calificar={self.calificar}")

Concurso()