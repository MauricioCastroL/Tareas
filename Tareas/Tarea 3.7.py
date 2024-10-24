#Autor: Mauricio Castro L 
#Fecha: 21/10/24

import tkinter as tk
from tkinter import *
from tkinter import ttk

def convertir_temperatura():
    if temperatura.get() == 'Celsius':
        Fahrenheit = (float(temp.get()) * 9/5) + 32
        Kelvin = (float(temp.get()) + 273.15)

        # Crear variables StringVar para actualizar los Entry
        F = StringVar()
        K = StringVar()

        # Crear los Entry solo si no existen previamente
        Entry_Fahrenheit = tk.Entry(ventana, width=12, state='readonly', textvariable=F)
        Entry_Fahrenheit.place(x=20, y=150)

        Entry_Kelvin = tk.Entry(ventana, width=12, state='readonly', textvariable=K)
        Entry_Kelvin.place(x=20, y=180)

        # Actualizar directamente las variables StringVar con los valores correspondientes
        F.set(f'{round(Fahrenheit, 2):,.2f}°F'.replace(',', '.'))
        K.set(f'{round(Kelvin, 2):,.2f}°K'.replace(',', '.'))
    
    if temperatura.get() == 'Fahrenheit':
        Celcius = (float(temp.get()) - 32) * 5/9 
        Kelvin = (float(temp.get()) - 32) * 5/9 + 273.15

        # Crear variables StringVar para actualizar los Entry
        F = StringVar()
        K = StringVar()

        # Crear los Entry solo si no existen previamente
        Entry_Fahrenheit = tk.Entry(ventana, width=12, state='readonly', textvariable=F).place(x=20, y=150)
        Entry_Kelvin = tk.Entry(ventana, width=12, state='readonly', textvariable=K).place(x=20, y=180)

        # Actualizar directamente las variables StringVar con los valores correspondientes
        F.set(f'{round(Celcius, 2):,.2f}°C'.replace(',', '.'))
        K.set(f'{round(Kelvin, 2):,.2f}°K'.replace(',', '.'))

    if temperatura.get() == 'Kelvin':
        Celcius = (float(temp.get()) - 273.15)
        Fahrenheit = float(temp.get()) - 273.15 * 9/5 + 32  

        # Crear variables StringVar para actualizar los Entry
        F = StringVar()
        K = StringVar()

        # Crear los Entry solo si no existen previamente
        Entry_Fahrenheit = tk.Entry(ventana, width=12, state='readonly', textvariable=F).place(x=20, y=150)
        Entry_Kelvin = tk.Entry(ventana, width=12, state='readonly', textvariable=K).place(x=20, y=180)

        # Actualizar directamente las variables StringVar con los valores correspondientes
        F.set(f'{round(Celcius, 2):,.2f}°C'.replace(',', '.'))
        K.set(f'{round(Fahrenheit, 2):,.2f}°F'.replace(',', '.'))

    if presion.get() == 'Pascal':
        Kpascal = float(pres.get()) / 1000

        # Crear variables StringVar para actualizar los Entry
        P = StringVar()
        # Crear los Entry solo si no existen previamente
        Entry_Pascal = tk.Entry(ventana, width=12, state='readonly', textvariable= P).place(x=200, y=150)

        # Actualizar directamente las variables StringVar con los valores correspondientes
        P.set(f'{round(Kpascal, 2):,.2f}Pa'.replace(',', '.'))

    if presion.get() == 'K-Pascal':
        Kpascal = float(pres.get()) * 1000

        # Crear variables StringVar para actualizar los Entry
        P = StringVar()
        # Crear los Entry solo si no existen previamente
        Entry_Pascal = tk.Entry(ventana, width=12, state='readonly', textvariable= P).place(x=200, y=150)

        # Actualizar directamente las variables StringVar con los valores correspondientes
        P.set(f'{round(Kpascal, 2):,.2f}Kpa'.replace(',', '.'))


if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title('Convertidor')
    ventana.geometry('300x300+1000+100')
    ventana.resizable(False, False)
    ventana.configure(background='#0e244e')
    
    tk.Label(ventana, text='Convertidor de Temperatura/Presión', background='#0e244e', fg='#ffc842', font='Arial, 10').place(x=50, y=10)
    tk.Label(ventana, text='Temperatura:', background='#0e244e', fg='#ffc842', font='Arial, 10').place(x=20, y=50)
    tk.Label(ventana, text='Presión:', background='#0e244e', fg='#ffc842', font='Arial, 10').place(x=200, y=50)

    temperatura = StringVar()
    ttk.Combobox(ventana, values=['Celsius', 'Kelvin', 'Fahrenheit'], width=10, height=10, state='readonly', textvariable=temperatura).place(x=20, y=80)
    presion = StringVar()
    ttk.Combobox(ventana, values=['Pascal', 'K-Pascal'], width=10, height=10, state='readonly', textvariable=presion).place(x=200, y=80)

    conversor_T = tk.Button(ventana, text='Convertir', background='#ffc842', fg='Black', command= convertir_temperatura).place(x=120, y=150)
    
    temp = StringVar()
    cantidad_T = tk.Entry(ventana, width='10', textvariable=temp).place(x=30, y=110)
    pres = StringVar()
    cantidad_P = tk.Entry(ventana, width='10', textvariable=pres).place(x=210, y=110)

    ventana.mainloop()