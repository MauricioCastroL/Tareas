#Autor: Mauricio Castro
#Fecha: 20/08/24

#Funcion que abra y lea el archivo
def lectura(archivo):
    #Lista que almacene los datos
    datos = []
    #Variable que abra los archivos
    f = open(archivo, "r", encoding= "UTF-8")
    #Ciclo que recorra el archivo
    for linea in f:
        datos.append(linea.rstrip("\n").split("\t"))
    #Elimino el encabezado de la lista
    del datos[0]
    #Ciclo que borre los parentesis
    for listas in datos:
        for caracter in range(len(listas)):
            listas[caracter] = listas[caracter].replace('(', '').replace(')', '')
    #returno la lsita con los datos
    return datos

#Funcion que calcule el ajuste
def calculo(ajuste, precios, productos):
    #Listas que tengan los datos con los que se trabaje
    precio = []
    porcentajes = []
    precios_ajustados = []
    producto = []
    indices = []
    #Creo un cilo que recorra el listado
    for i in ajuste:
        porcentajes.append(float(i[1]))
    for i in precios:
        precio.append(float(i[1]))
    for i in productos:
        producto.append(i[1])
    for i in ajuste:
        indices.append(i[0]) 
    #Calculos de reajuste
    for valor, ajustes in zip(precio, porcentajes):
        if ajustes != 0:
            precios_ajustados.append(valor * (1 + (ajustes/100)))
        else:
            precios_ajustados.append(valor)
    #Arreglos de reajuste en descuentos 
    precios_ajustados[7] = float(precios[7][1]) * 0.95
    precios_ajustados[11] = float(precios[11][1]) * 0.95
    suma = sum(precios_ajustados)
    #returno la lista con los valores ya ajustados
    return precio, porcentajes, precios_ajustados, producto, indices, suma
    
#Funcion que muestre los resultados
def mostrar(precio, porcentaje, precio_ajustado, producto, indices, suma):
    #Junto todas las listas para mostrar los resultados
    combinado = zip(indices, producto, precio, porcentaje, precio_ajustado)
    print(f'Codigo    Producto                     Precio               Ajuste                Pventa')
    #Ciclo que muestra todos los datos
    for indices, producto, precio, porcentaje, precio_ajustado in combinado:
        print(f'{indices}          {producto}                      {precio}                {porcentaje}                  {precio_ajustado}')
    print(f'            Totales                                                                     ${suma}')



if __name__ == "__main__":
    ajuste = lectura("ajuste.txt")
    productos = lectura("productos.txt")
    precios = lectura("precios.txt")
    precio, porcentajes, precios_ajustados, producto, indices, suma = calculo(ajuste, precios, productos)
    mostrar(precio, porcentajes, precios_ajustados, producto, indices, suma)
