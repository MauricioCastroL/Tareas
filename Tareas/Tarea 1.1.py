#Autor: M/auricio Castro
#Fecha: 21/08/24

#Funcion que lea los datos
def lectura(archivo):
    #lista que guarde los datos
    datos = []
    captura = False
    caso = []
    #Variable que abra el archivo
    f = open(archivo, 'r', encoding='UTF-8')
    #Ciclo que recorra el archivo
    for linea in f:
        if linea == 'CASO 3688580-4\n':
            datos.append(linea.rstrip().split())
            captura = True
        elif captura and linea.startswith('CASO '):
            captura = False
        elif captura:
            datos.append(linea.rsplit())
    #Ciclos y arreglos de datos
    for listas in datos:
        if listas == []:
            datos.remove(listas)
    del datos[-1]
    #Lista a trabajar 
    for listas in datos:
        if listas[0] == 'CASO':
            caso.append(listas)
        elif listas[0] == 'ITEM':
            caso.append(listas)
        elif listas[0] == 'DESCUENTO':
            caso.append(listas)
    return caso

#Funcion que calcule
def calculos(caso):
    #Variable que almacene los datos
    sumas_cantidades = []
    sumas_unitarios = []
    codigo = []
    #Ciclo que saque el caso y su numeracion
    for listas in caso:
        for palabra in listas:
            if palabra == 'CASO':
                codigo.append(listas)
    #Ciclo que calcule las sumas unitarias
    for listas in caso:
        for palabras in listas:
            if palabras == 'ITEM':
                if listas[1].isdigit() == True:
                    sumas_unitarios.append(float(listas[-1]))
    sumas_unitarios = int(sum(sumas_unitarios))
    #Ciclos que calcule las sumas de las cantidades
    for listas in caso:
        for palabras in listas:
            if palabras == 'ITEM':
                if listas[1].isdigit() == True:
                    sumas_cantidades.append(float(listas[-2]))
    sumas_cantidades = sum(sumas_cantidades)
    cantidades = f"{sumas_unitarios:,.0f}".replace(',', '.')
    unitarios = f"{sumas_cantidades:,.0f}".replace(',', '.')
    for palabra in codigo:
        codigo = palabra
    codigo = codigo.pop(0) + ' ' + codigo.pop(0)
    return cantidades, unitarios, codigo

#Funcion que muestre los datos
def mostrar(cantidades, unitarios, codigo):
    #Variable que cree el archivo
    f = open('caso4.dat', 'w', encoding='UTF-8')
    f.write(f'{codigo}\n')
    f.write(f'Cantidad {cantidades}\n')
    f.write(f'Unitarios {unitarios}')
    f.close()



if __name__ == '__main__':
    caso = lectura('SetDePruebas.txt')
    cantidades, unitarios, codigo = calculos(caso)
    mostrar(unitarios, cantidades, codigo)