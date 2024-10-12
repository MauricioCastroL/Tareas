#Autor: Mauricio Castro
#Fecha: 23/09/24

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
import os

archivo_json = 'clientes.json'

def cargar_clientes():
    if os.path.exists(archivo_json):
        with open(archivo_json, 'r', encoding='UTF-8') as archivo:
            return json.load(archivo)
    return {}

def guardar_clientes(clientes):
    with open(archivo_json, 'w', encoding='UTF-8') as archivo:
        json.dump(clientes, archivo)

clientes = cargar_clientes()

def anadir():
    crear_cuenta = Toplevel()
    try:
        icono = PhotoImage(file='menu.png')
        crear_cuenta.iconphoto(False, icono)
    except Exception as e:
        print(f'File not found {e}')
    crear_cuenta.configure(background='#0a1937')
    crear_cuenta.resizable(False, False)
    crear_cuenta.geometry('300x300+1000+100')
    crear_cuenta.configure(background='#0a1937')

    tk.Label(crear_cuenta, text='Ingrese su RUT', fg='#ffc842', bg='#0a1937').place(x=20, y=30)
    ide = StringVar()
    rut = Entry(crear_cuenta, width=15, textvariable=ide).place(x=110, y=30)

    tk.Label(crear_cuenta, text='Nombre', fg='#ffc842', bg='#0a1937').place(x=50, y=60)
    user = StringVar()
    nombre = Entry(crear_cuenta, width=15, textvariable=user).place(x=110, y=60)

    tk.Label(crear_cuenta, text='Email', fg='#ffc842', bg='#0a1937').place(x=60, y=90)
    email = StringVar()
    correo = Entry(crear_cuenta, width=15, textvariable=email).place(x=110, y=90)

    tk.Label(crear_cuenta, text='Teléfono', fg='#ffc842', bg='#0a1937').place(x=50, y=120)
    fono = StringVar()
    telefono = Entry(crear_cuenta, width=15, textvariable=fono).place(x=110, y=120)

    tk.Label(crear_cuenta, text='Tipo Cliente', fg='#ffc842', bg='#0a1937').place(x=35, y=150)
    cliente = StringVar()
    tipo_cliente = Entry(crear_cuenta, width=15, textvariable=cliente).place(x=110, y=150)

    tk.Label(crear_cuenta, text='Actividad', fg='#ffc842', bg='#0a1937').place(x=50, y=180)
    actividad = StringVar()
    tipo_cliente_actividad = Entry(crear_cuenta, width=15, textvariable=actividad).place(x=110, y=180)

    ingresar = Button(crear_cuenta, width=10, height=1, bg='#ffc842', text='Ingresar', command= lambda: agregar(clientes, ide.get(), 
                                                                                                                user.get(), email.get(),
                                                                                                                fono.get(), cliente.get(), actividad.get())).place(x=105, y=210)

    crear_cuenta.mainloop()

def agregar(clientes, rut, nombre, email, fono, tipo_cliente, actividad):

    # Validaciones
    if not rut or not nombre or not email or not fono or not tipo_cliente or not actividad:
        print("Todos los campos son obligatorios.") #xxx
        return
    
    if rut in clientes:
        print("El RUT ya existe.")
        return
    
    # Intenta convertir tipo_cliente a int
    try:
        tipo_cliente = int(tipo_cliente)
    except ValueError:
        print("Tipo Cliente debe ser un número.")
        return
    
    clientes[rut] = {
        'nombre': nombre, 'email': email, 'teléfono': fono,'tipocli': tipo_cliente,'estado':actividad
    }
    guardar_clientes(clientes)
    messagebox.showinfo("Éxito", "Cliente añadido correctamente.")

def eliminar():
    eliminar_cuenta = Toplevel()
    try:
        icono = PhotoImage(file='menu.png')
        eliminar_cuenta.iconphoto(False, icono)
    except Exception as e:
        print(f'File not found {e}')

    eliminar_cuenta.configure(background='#0a1937')
    eliminar_cuenta.resizable(False, False)
    eliminar_cuenta.geometry('300x200+1000+100')


    tk.Label(eliminar_cuenta, text='Elimine cuenta', fg='#ffc842', bg='#0a1937').place(x=105, y=20)
    dele = StringVar()
    delete = Entry(eliminar_cuenta, width=15, textvariable=dele).place(x=100, y=50)

    boton_eliminar = Button(eliminar_cuenta, text='Eliminar', bg='#ffc842', command= lambda: quitar(clientes, dele.get())).place(x=120, y=80)

    eliminar_cuenta.mainloop()

def quitar(clientes, eliminar):
    if eliminar in clientes:
        del clientes[eliminar]
        guardar_clientes(clientes)
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
    else:
        messagebox.showerror("Error", "El RUT ingresado no existe.")

def mostrar():
    mostrar = Toplevel()
    try:
        icono = PhotoImage(file='menu.png')
        mostrar.iconphoto(False, icono)
    except Exception as e:
        print(f'File not found {e}')
    mostrar.resizable(False, False)
    mostrar.geometry('300x200')
    mostrar.configure(background='#0a1937')
    
    tk.Label(mostrar, text='Ingrese el Rut del usuario al que busca', fg='#ffc842', bg='#0a1937').place(x=40, y=10)
    rut = StringVar()
    ide = Entry(mostrar, textvariable=rut, width=15).place(x=100, y=40)

    buscar = Button(mostrar, text='Buscar', width=8, bg='#ffc842', command=lambda: mostrar_usuario(clientes, rut.get())).place(x=115, y=70)

    mostrar.mainloop()

def mostrar_usuario(clientes, rut):
    if rut in clientes:
        usuario_info = clientes[rut]
        mensaje = (f"Nombre: {usuario_info['nombre']}\nEmail: {usuario_info['email']}\n Teléfono: {usuario_info['teléfono']}\n tipocli: {usuario_info['tipocli']}\n Estado: {usuario_info['estado']}")
        # Muestra el mensaje
        messagebox.showinfo('Usuario', mensaje)
    else:
        messagebox.showwarning('Usuario no encontrado', 'El RUT ingresado no está registrado.')

def listar_clientes():
    listado_clientes = Toplevel()
    try:
        icono = PhotoImage(file='menu.png')
        listado_clientes.iconphoto(False, icono)
    except Exception as e:
        print(f'File not found {e}')
    listado_clientes.resizable(False, False)
    listado_clientes.geometry('300x200')
    listado_clientes.configure(background='#0a1937')

    tk.Label(listado_clientes, text='Seleccione el listado por estado de actividad', fg='#ffc842', bg='#0a1937').place(x=30, y=10)
    seleccion = StringVar()
    combo = ttk.Combobox(listado_clientes, values=['Frecuentes', 'Activos', 'No-Frecuentes', 'Inactivos', 'Todos'], state='readonly', textvariable=seleccion).place(x=70, y=40)
    boton = Button(listado_clientes, text='Mostrar', bg='#ffc842', command= lambda: mostar_estado_clientes(clientes, seleccion.get())).place(x=110, y=80)

    listado_clientes.mainloop()

def mostar_estado_clientes(clientes, seleccion):
    if seleccion not in ['Frecuentes', 'No Frecuentes', 'Todos', 'Activos', 'Inactivos']:
        messagebox.showwarning('Selección no válida', 'Por favor selecciona una opción válida.')
        return

    # Crear un Toplevel para mostrar los resultados
    top = Toplevel()
    top.title(f'Clientes - {seleccion}')
    try:
        icono = PhotoImage(file='menu.png')
        top.iconphoto(False, icono)
    except Exception as e:
        print(f'File not found {e}')
    top.geometry('400x300')

    # Crear un cuadro de texto con scrollbar
    text_area = Text(top, wrap='word')
    text_area.pack(expand=True, fill='both')

    scrollbar = Scrollbar(top, command=text_area.yview)
    scrollbar.pack(side='right', fill='y')
    text_area['yscrollcommand'] = scrollbar.set

    # Variable para comprobar si se encontraron clientes
    clientes_encontrados = False

    for rut, usuario_info in clientes.items():
        mostrar_cliente = False
        if seleccion == 'Frecuentes' and usuario_info['tipocli'] == 'F':
            mostrar_cliente = True
        elif seleccion == 'No Frecuentes' and usuario_info['tipocli'] == 'No-F':
            mostrar_cliente = True
        elif seleccion == 'Todos':
            mostrar_cliente = True
        elif seleccion == 'Activos' and usuario_info['estado'] == 'A':
            mostrar_cliente = True
        elif seleccion == 'Inactivos' and usuario_info['estado'] == 'I':
            mostrar_cliente = True

        # Agregar la información al cuadro de texto si se cumple la condición
        if mostrar_cliente:
            clientes_encontrados = True
            mensaje = (f"Nombre: {usuario_info['nombre']}\n"
                       f"Email: {usuario_info['email']}\n"
                       f"Teléfono: {usuario_info['teléfono']}\n"
                       f"Tipo de Cliente: {usuario_info['tipocli']}\n"
                       f"Estado: {usuario_info['estado']}\n\n")
            text_area.insert(tk.END, mensaje)

    if not clientes_encontrados:
        text_area.insert(tk.END, 'No se encontraron clientes para la selección realizada.')

    text_area.config(state=tk.DISABLED)
        
def terminar():
    menu.quit()


if __name__ == '__main__':
    menu = tk.Tk()
    menu.resizable(False, False)
    menu.geometry('300x200')
    try:
        icono = PhotoImage(file='menu.png')
        menu.iconphoto(False, icono)
    except Exception as e:
        print(f'File not found {e}')
    menu.configure(background='#0a1937')

    anadir = Button(menu, text='Añadir cliente', width=12, height=1, bg='#ffc842', command=anadir).place(x=100, y=40)
    eliminar = Button(menu, text='Eliminar cliente', width=12, height=1, bg='#ffc842', command=eliminar).place(x=100, y=70)
    mostar = Button(menu, text='Mostrar cliente', width=12, height=1, bg='#ffc842', command=mostrar).place(x=100, y=100)
    Listado = Button(menu, text='Listado clientes', width=12, height=1, bg='#ffc842', command=listar_clientes).place(x=100, y=130)
    Exit = Button(menu, text='Terminar', width=12, height=1, bg='#ffc842', command=terminar).place(x=100, y=160)

    tk.Label(menu, text='Menú', bg='#0a1937', fg='#ffc842').place(x=120, y=10)

    menu.mainloop()