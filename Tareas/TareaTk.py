#Autor: Mauricio Castro
#Fecha: 26/08/24

import tkinter as tk
from tkinter import *    

#Funcion que calcule las dimensiones de los trosos
def calculo_trozos():
    #Variable con dimensiones de la placa
    area_placa = 94428
    perdida = 0.4

    #Saco las variables de los entry
    cantidad_trozo = float(cantidad.get())
    largo_trozo = float(largo.get())
    ancho_trozo = float(ancho.get())
    area_pedida = largo_trozo * ancho_trozo * 1.8 * cantidad_trozo
    #Ciclo de comparacion
    if area_placa == area_pedida:
        precios = 29900
        superfici = 0
        #Lo pedio es la placa
        precio.set(f'{precios}')
        superficie.set(f'{superfici}')

    elif area_placa > area_pedida:
        precios = 29900
        superficie_perdida_area = (area_placa - area_pedida) - (perdida * cantidad_trozo)
        superficie_perdida_area = superficie_perdida_area / 1.8
        precio.set(f'${precios}')
        superficie.set(f'{round(superficie_perdida_area, 2)}cm**2')
        
    elif area_placa < area_pedida:
        contador = 1
        while area_placa < area_pedida:
            area_placa = area_placa * (contador + 1)
        precios = 29900 * contador
        superficie_perdida_area = (area_placa - area_pedida) - (perdida * cantidad_trozo)
        superficie_perdida_area = superficie_perdida_area / 1.8
    precio.set(f'${precios}')
    superficie.set(f'{round(superficie_perdida_area, 2)}cm**2')

#Funcion que limpie
def limpia():
    cantidad.delete(0, END)
    largo.delete(0, END)
    ancho.delete(0, END)
    precio.set('')
    superficie.set('')


if __name__ == '__main__':
    #Creo La ventana de la interfaz
    ventana = Tk()
    ventana.title('Trozos de madera')
    ventana.resizable(False, False)
    ventana.geometry('300x300')
    ventana.config(bg='white')
    miFrame = Frame(ventana, width=500, height=500)
    miFrame.pack()

    #Creacion de los Label
    cantidadtext = Label(miFrame, text='Cantidad de trozos')
    cantidadtext.grid(row=0, column=0, padx=5, pady=5)

    largotext = Label(miFrame, text='Ingrese el largo del corte')
    largotext.grid(row=1, column=0, padx=5, pady=5)

    anchotext = Label(miFrame, text='Ingrese el ancho del corte')
    anchotext.grid(row=2, column=0, padx=5, pady=5)

    altotext = Label(miFrame, text='Precio a pagar')
    altotext.grid(row=3, column=0, padx=5, pady=5)

    superficietext = Label(miFrame, text='Superficie sobrante (cm**2)')
    superficietext.grid(row=4, column=0, padx=5, pady=5)

    trozostext = Label(miFrame, text='Corte de trozos')
    trozostext.grid(row=5, column=0, padx=5, pady=5)

    #Creaciones de los Entry
    cantidad = StringVar()
    cantidad = Entry(miFrame,width=5, textvariable=cantidad)
    cantidad.grid(row=0, column=1, padx=5, pady=5)

    largo = StringVar()
    largo = Entry(miFrame, width=10, textvariable=largo)
    largo.grid(row=1, column=1, padx=5, pady=5)

    ancho = StringVar()
    ancho = Entry(miFrame, width=10, textvariable=ancho)
    ancho.grid(row=2, column=1, padx=5, pady=5)

    #Cuadro de texto
    precio = StringVar()
    precio_trozo = Entry(miFrame, textvariable=precio, width=10, state='readonly')
    precio_trozo.grid(row=3, column=1, padx=5, pady=5)

    superficie = StringVar()
    superficie_sobrante = Entry(miFrame, textvariable=superficie, width=10, state='readonly')
    superficie_sobrante.grid(row=4, column=1, padx=5, pady=5)

    trozos = StringVar()
    trozos_a = Entry(miFrame, textvariable=trozos, width=10, state='readonly')
    trozos_a.grid(row=5, column=1, padx=5, pady=5)

    #Creo los botones
    boton = Button(text='Comprar', width=8, height=2, command=calculo_trozos, bg='green')
    boton.place(x=75, y=200)

    botonlimpia = Button(text='Limpiar', width=8, height=2, command=limpia, bg='green')
    botonlimpia.place(x=150, y=200)



    ventana.mainloop()