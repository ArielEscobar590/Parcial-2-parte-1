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
                            "Municipio": municipio,
                            "Calificaciones": []
                        }
            print("Candidatas importadas desde candidatas.txt")
        except FileNotFoundError:
            print("No existe el archivo candidatas.txt, se creará uno nuevo al guardar.")

    def guardar_candidatas(self):
        with open("candidatas.txt", "w", encoding="utf-8") as archivo:
            for codigo, datos in self.candidatas.items():
                calif_str = ",".join(";".join(map(str, cal)) for cal in datos["Calificaciones"])
                archivo.write(f"{codigo}:{datos['Nombre']}:{datos['Edad']}:{datos['Instituto']}:{datos['Municipio']}:{calif_str}\n")

    def agregar_candidatas(self, codigo, nombre, edad, instituto, municipio):
        self.candidatas[codigo] = {
            "Nombre": nombre,
            "Edad": edad,
            "Instituto": instituto,
            "Municipio": municipio,
            "Calificaciones": []
        }
        self.guardar_candidatas()
        print(f"Candidata {nombre} agregada y guardada correctamente.")

    def agregar_calificacion(self, codigo, cultura, proyeccion, entrevista):
        if codigo in self.candidatas:
            self.candidatas[codigo]["Calificaciones"].append([float(cultura), float(proyeccion), float(entrevista)])
            self.guardar_candidatas()
            print(f"Calificación registrada para {self.candidatas[codigo]['Nombre']}")

    def puntaje_final(self, codigo):
        if codigo in self.candidatas and self.candidatas[codigo]["Calificaciones"]:
            califs = self.candidatas[codigo]["Calificaciones"]
            promedios = [(c + p + e) / 3 for c, p, e in califs]
            return sum(promedios) / len(promedios)
        return 0


class Jurado:
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
                        self.jurado[nombre] = {"Especialidad": especialidad}
            print("Jurados importados desde jurado.txt")
        except FileNotFoundError:
            print("No existe el archivo jurado.txt, se creará uno nuevo al guardar.")

    def guardar_jurado(self):
        with open("jurado.txt", "w", encoding="utf-8") as archivo:
            for nombre, datos in self.jurado.items():
                archivo.write(f"{nombre}:{datos['Especialidad']}\n")

    def agregar_jurado(self, nombre, especialidad):
        self.jurado[nombre] = {"Especialidad": especialidad}
        self.guardar_jurado()
        print(f"Jurado {nombre} agregado y guardado correctamente.")


class Concurso:
    def __init__(self):
        self.candidata = Candidata()
        self.jurado = Jurado()

        self.ventana = tk.Tk()
        self.ventana.title("Elección Reina de  Independencia 2025")
        self.ventana.geometry("700x400")
        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Evaluación - Independencia 2025",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Registrar Candidata", command=self.registrar_candidata)
        opciones.add_command(label="Registrar Jurado", command=self.registrar_jurado)
        opciones.add_command(label="Agregar Calificación", command=self.agregar_calificacion)
        opciones.add_command(label="Mostrar Ranking", command=self.mostrar_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def registrar_candidata(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Registrar Candidata")

        tk.Label(ventana, text="Código").grid(row=0, column=0)
        codigo = tk.Entry(ventana)
        codigo.grid(row=0, column=1)

        tk.Label(ventana, text="Nombre").grid(row=1, column=0)
        nombre = tk.Entry(ventana)
        nombre.grid(row=1, column=1)

        tk.Label(ventana, text="Edad").grid(row=2, column=0)
        edad = tk.Entry(ventana)
        edad.grid(row=2, column=1)

        tk.Label(ventana, text="Instituto").grid(row=3, column=0)
        inst = tk.Entry(ventana)
        inst.grid(row=3, column=1)

        tk.Label(ventana, text="Municipio").grid(row=4, column=0)
        muni = tk.Entry(ventana)
        muni.grid(row=4, column=1)

        def guardar():
            self.candidata.agregar_candidatas(codigo.get(), nombre.get(), edad.get(), inst.get(), muni.get())
            messagebox.showinfo("Éxito", "Candidata registrada.")
            ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar).grid(row=5, column=0, columnspan=2)

    def registrar_jurado(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Registrar Jurado")

        tk.Label(ventana, text="Nombre").grid(row=0, column=0)
        nombre = tk.Entry(ventana)
        nombre.grid(row=0, column=1)

        tk.Label(ventana, text="Especialidad").grid(row=1, column=0)
        espec = tk.Entry(ventana)
        espec.grid(row=1, column=1)

        def guardar():
            self.jurado.agregar_jurado(nombre.get(), espec.get())
            messagebox.showinfo("Éxito", "Jurado registrado.")
            ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar).grid(row=2, column=0, columnspan=2)

    def agregar_calificacion(self):
        ventana = Toplevel(self.ventana)
        ventana.title("Agregar Calificación")

        tk.Label(ventana, text="Código de Candidata").grid(row=0, column=0)
        codigo = tk.Entry(ventana)
        codigo.grid(row=0, column=1)

        tk.Label(ventana, text="Cultura General").grid(row=1, column=0)
        cultura = tk.Entry(ventana)
        cultura.grid(row=1, column=1)

        tk.Label(ventana, text="Proyección Escénica").grid(row=2, column=0)
        proyeccion = tk.Entry(ventana)
        proyeccion.grid(row=2, column=1)

        tk.Label(ventana, text="Entrevista").grid(row=3, column=0)
        entrevista = tk.Entry(ventana)
        entrevista.grid(row=3, column=1)

        def guardar():
            self.candidata.agregar_calificacion(codigo.get(), cultura.get(), proyeccion.get(), entrevista.get())
            messagebox.showinfo("Éxito", "Calificación registrada.")
            ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, column=0, columnspan=2)

    def mostrar_ranking(self):
        if not self.candidata.candidatas:
            messagebox.showwarning("Atención", "No hay candidatas registradas.")
            return

        ranking = sorted(
            self.candidata.candidatas.items(),
            key=lambda x: self.candidata.puntaje_final(x[0]),
            reverse=True
        )

        texto = "Ranking de Candidatas:\n"
        for i, (codigo, datos) in enumerate(ranking, start=1):
            texto += f"{i}. {datos['Nombre']} ({datos['Instituto']}) - Puntaje: {self.candidata.puntaje_final(codigo):.2f}\n"

        messagebox.showinfo("Ranking", texto)



Concurso()