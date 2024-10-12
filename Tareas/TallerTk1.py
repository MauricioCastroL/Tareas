#Autor: Mauricio Castro
#Fecha: 09/09/24

import tkinter as tk
from tkinter import *
from tkinter import ttk
import random as rmd

def descuentos():
    raiz = Toplevel()
    raiz.geometry('300x200')
    raiz.resizable(False, False)
    frame = Frame(raiz, width=500, height=500)
    frame.pack()

    coloresText = Label(frame, text='Descuentos disponibles:').grid(row=0, column=0, pady=5, padx=5)
    colorLista = Label(frame, text='Blanco 0%, Rojo 10%\nAzul 20%\nAmarillo 25%, Verde 50%').grid(row=0, column=1, padx=5, pady=5)
    Total_articulos = Label(frame, text='Total artículos').grid(row=1, column=0, padx=5, pady=5)
    descuento_articulos = Label(frame, text='Descuento por sorteo').grid(row=2, column=0, padx=5, pady=5)
    Tota_pagar = Label(frame, text='Total a pagar').grid(row=3, column=0, padx=5, pady=5)

    Ta = StringVar()
    total_Art = Entry(frame, width=12, state='readonly', textvariable=Ta).grid(row=1, column=1, pady=5, padx=5)
    des = StringVar()
    descuento_art = Entry(frame, width=12, state='readonly', textvariable=des).grid(row=2, column=1, pady=5, padx=5)
    pag = StringVar()
    total_pag = Entry(frame, width=12, state='readonly', textvariable=pag).grid(row=3, column=1, pady=5, padx=5)

    Ta.set(f'{can.get()} unidades')

    if cum.get() == 'Verde':
        des.set(f'50% Desct.')
        if (com.get() == 'Armario'):
            pago = ( 120000 * int(can.get())) * 0.5
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
        elif (com.get() == 'Velador'):
            pago = ( 140000 * int(can.get())) * 0.5
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
        elif (com.get() == 'Lampara'):
            pago = ( 130000 * int(can.get())) * 0.5
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
    elif cum.get() == 'Blanco':
        des.set(f'0% Desct.')
        if (com.get() == 'Armario'):
            pago = ( 120000 * int(can.get()))
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
        elif (com.get() == 'Velador'):
            pago = ( 140000 * int(can.get()))
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
        elif (com.get() == 'Lampara'):
            pago = ( 130000 * int(can.get()))
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
    elif cum.get() == 'Amarillo':
        des.set(f'25% Desct.')
        if (com.get() == 'Armario'):
            pago = ( 120000 * int(can.get())) * 0.75
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
        elif (com.get() == 'Velador'):
            pago = ( 140000 * int(can.get())) * 0.75
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
        elif (com.get() == 'Lampara'):
            pago = ( 130000 * int(can.get())) * 0.75
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
    elif cum.get() == 'Rojo':
        des.set(f'10% Desct.')
        if (com.get() == 'Armario'):
            pago = ( 120000 * int(can.get())) * 0.9
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
        elif (com.get() == 'Velador'):
            pago = ( 140000 * int(can.get())) * 0.9
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
        elif (com.get() == 'Lampara'):
            pago = ( 130000 * int(can.get())) * 0.9
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
    elif cum.get() == 'Azul':
        des.set(f'20% Desct.')
        if (com.get() == 'Armario'):
            pago = ( 120000 * int(can.get())) * 0.8
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
        elif (com.get() == 'Velador'):
            pago = ( 140000 * int(can.get())) * 0.8
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
        elif (com.get() == 'Lampara'):
            pago = ( 130000 * int(can.get())) * 0.8
            pago = f"{pago:,.0f}".replace(",", ".")
            pag.set(f'${pago}')
    raiz.mainloop()

def limpiar():
    com.set('')
    cum.set('')
    can.set('')

if __name__ == '__main__':
    #Creación de la Ventana
    ventana = Tk()
    ventana.title('Descuentos')
    ventana.geometry('300x150')
    ventana.resizable(False, False)
    miFrame = Frame(ventana, width=500, height=500)
    miFrame.pack()

    #Creación de los Label
    CompraText = Label(miFrame, text='Ingrese su compra').grid(row=0, column=0, padx=5, pady=5)
    ColorText = Label(miFrame, text='Ingrese el color la compra').grid(row=1, column=0, padx=5, pady=5)
    CantidadText = Label(miFrame, text='Cantidad').grid(row=2, column=0, padx=5, pady=5)


    com = StringVar()
    Compra = ttk.Combobox(miFrame, width=12, values=['Armario', 'Velador', 'Lampara'], state='readonly', textvariable=com).grid(row=0, column=1)
    cum = StringVar()
    Color = ttk.Combobox(miFrame, width=12, values=['Blanco', 'Rojo', 'Azul', 'Amarillo', 'Verde'], state='readonly', textvariable=cum).grid(row=1, column=1)
    can = StringVar()
    cantidad = Entry(miFrame, width=5, textvariable=can).grid(row=2, column=1, padx=5, pady=5)

    #Creación de los botones
    boton = Button(text='Comprar', width=8, height=1, command=descuentos, bg='green')
    boton.place(x=150, y=100)

    limpiar = Button(text='Limpiar', width=8, height=1, command=limpiar, bg='green')
    limpiar.place(x=70, y=100)

    ventana.mainloop()
