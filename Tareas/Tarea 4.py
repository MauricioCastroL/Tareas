#Autor: Mauricio Castro/ José Cáseres
#Fecha: 23/08/24

import tkinter as tk
from tkinter import *

#Funcion que clasifique los triangulos
def clasificar_triangulo():
    # Obtener los lados ingresados
    lado1 = float(primer_lado.get())
    lado2 = float(segundo_lado.get())
    lado3 = float(tercer_lado.get())
        
    # Condicion que verifique si los lados no son negativos
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        resultado.set("Los lados deben ser números positivos")
        return

        # Condicion que verifique si los lados corresponden a un triángulo
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 == lado2 == lado3:
                tipo = "Equilátero"
        elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
                tipo = "Isósceles"
        else:
                tipo = "Escaleno"
        resultado.set(f"El triángulo es {tipo}")
    else:
        resultado.set("Los lados no forman un triángulo válido")


#Funcionque cierre el programa
def cerrar():
    ventana.destroy()

#Funcion que limpie los Entry
def limpiar():
    primer_lado.delete(0, END)
    segundo_lado.delete(0, END)
    tercer_lado.delete(0, END)
    resultado.set("")


if __name__ == '__main__':
    #Creacion de la ventana
    ventana = Tk()
    ventana.title('Tpos de Triángulos')
    ventana.resizable(False, False)
    ventana.geometry('350x200')
    miFrame = Frame(ventana, width=500, height=400)
    miFrame.pack()
    ventana.config(bg='white')

    #Cuadros de entrada
    primer_lado = StringVar()
    primer_lado = Entry(miFrame, textvariable=primer_lado)
    primer_lado.grid(row=0, column=1, padx=5, pady=5)

    segundo_lado = StringVar()
    segundo_lado = Entry(miFrame, textvariable=segundo_lado)
    segundo_lado.grid(row=1, column=1, padx=5, pady=5)

    tercer_lado = StringVar()
    tercer_lado = Entry(miFrame, textvariable=tercer_lado)
    tercer_lado.grid(row=2, column=1, padx=5, pady=5)

    #Creacion margenes de texto
    lado1text = Label(miFrame, text='Primer Lado')
    lado1text.grid(row=0, column=0, padx=5, pady=5)

    lado2text = Label(miFrame, text='Segundo lado')
    lado2text.grid(row=1, column=0, padx=5, pady=5)

    lado3text = Label(miFrame, text='Tercer lado')
    lado3text.grid(row=2, column=0, padx=5, pady=5)

    resultadotext = Label(miFrame, text='Resultado')
    resultadotext.grid(row=3, column=0, padx=5, pady=5)

    #Creacion de los botones
    miBoton = Button(text='Preguntar', width=8, height=2, bg='green', command=clasificar_triangulo)
    miBoton.place(x= 75, y=150)

    tuBoton = Button(text='Limpiar', width=8, height=2, bg='green', command=limpiar)
    tuBoton.place(x= 150, y=150)

    nuestroBoton = Button(text='Cerrar', width=8, height=2, bg='green', command=cerrar)
    nuestroBoton.place(x= 225, y=150)

    #Cuadro de texto
    resultado = StringVar()
    cuadro_resultado = Entry(miFrame, textvariable=resultado, state='readonly', width=25)
    cuadro_resultado.grid(row=3, column=1, padx=5, pady=5)
    
    ventana.mainloop()
