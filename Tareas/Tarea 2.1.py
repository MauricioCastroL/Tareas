#Autor: Mauricio Castro 
#Fecha: 19/08/24

#Funcion que lea los archivos
def lectura(archivo):
    #Listas que contengan los datos
    datos = []
    nombres = []
    valores = []
    #Variable que habra el archivo
    f = open(archivo, 'r', encoding='UTF-8')
    #Ciclo que recorra el archivo
    for linea in f:
        datos.append(linea.rstrip().split('- '))
    #Cierro el archivo
    f.close()
    #Ciclo que obtenga los nombres y tiempos
    for lista in datos:
        for palabra in lista:
            if len(palabra) <= 5:
                valores.append(palabra)
            else:
                nombres.append(palabra)
    #Elimino espacios innesesarios
    del valores[1]
    del valores[2]
    del nombres[0]
    del nombres[1]
    del nombres[2]
    #Returno los datos
    return datos, valores, nombres

#Funcion que calcule el promedio
def promedio(tiempo100, tiempo200):
    #Variables que contengan los dos mejores tiempos
    tiempo100_p = tiempo100[3]
    tiempo100_s = tiempo100[4]
    tiempo200_p = tiempo200[3]
    tiempo200_s = tiempo200[4]
    #Calculo de promedio
    promedio100 = (float(tiempo100_p) + float(tiempo100_s) / 2)
    promedio200 = (float(tiempo200_p) + float(tiempo200_s) / 2)
    #Calculo de diferencias entre los promedios y el world record
    diferencia100wr = str(round(promedio100 - float(tiempo100[0]), 2))
    diferencia200wr = str(round(promedio200 - float(tiempo200[0]), 2))
    #Calculo de diferencias entre los promedios y el world olimpic
    diferencia100wo = str(round(promedio100 - float(tiempo100[1]), 2))
    diferencia200wo = str(round(promedio200 - float(tiempo200[1]), 2))
    #Creo el diccionario
    return diferencia100wr, diferencia200wr, diferencia100wo, diferencia200wo

#Funcion que cree un archivo y muestre los datos
def mostrar(dif100wr, dif200wr, dif100wo, dif200wo, nombres, nombre, tiempo, tiempo200):
    #Variable que cree el archivo
    f = open('record100.txt', 'w', encoding='UTF-8')
    file = open('record200.txt', 'w', encoding='UTF-8')
    #Escribo en record100.txt
    f.write('Año                 Atleta                      Time(s)\n')
    f.write(f'2009  wr    {nombres[0]}    {tiempo[0]}\n')
    f.write(f'2012  w0    {nombres[1]}           {tiempo[1]}\n')
    f.write(f'2024  1     {nombres[2]}          {tiempo[2]}\n')
    f.write(f'2024  2     {nombres[3]}          {tiempo[3]}\n')
    f.write(f'2024  wr    Diferencia media de tiempo           {dif100wr}\n')
    f.write(f'2024  wo    Diferencia media de tiempo           {dif100wo}\n')
    f.close()
    #Escribo en record200.txt
    file.write('Año                 Atleta                      Time(s)\n')
    file.write(f'2009  wr    {nombre[0]}    {tiempo200[0]}\n')
    file.write(f'2012  w0    {nombre[1]}           {tiempo200[1]}\n')
    file.write(f'2024  1     {nombre[2]}         {tiempo200[2]}\n')
    file.write(f'2024  2     {nombre[3]}   {tiempo200[3]}\n')
    file.write(f'2024  wr    Diferencia media de tiempo           {dif200wr}\n')
    file.write(f'2024  wo    Diferencia media de tiempo           {dif200wo}\n')
    file.close()


if __name__ == '__main__':
    datos, valores, nombres = lectura('wr100.txt')
    dato, valor, nombre = lectura('wr200.txt')
    dif100wr, dif200wr, dif100wo, dif200wo = promedio(valores, valor)
    mostrar(dif100wr, dif200wr, dif100wo, dif200wo, nombres, nombre, valores, valor)