#Autores: Mauricio Castro / Benjamin Flores
#Fecha: 22/10/24 

#Función que abra y lea el archivo a trabajar
def lectura(archivo):
    #Lista que almacene las secuencias completas
    secuencias = []
    #Apertura del archivo
    file = open(archivo, 'r', encoding='ascii')
    #Ciclo que recorra los datos
    for linea in file:
        numeros = linea.strip().split()
        for numero in numeros:
            if numero.isdigit():
                secuencias.append(int(numero))
    #Cierre del archivo
    file.close()
    #Returno la lista con todas las secuenicias 
    return secuencias

'''Función que identifique las secuencias contenidas
en la lista obtenida por la función lectura''' 
def identificar_secuencias(secuencia):
    secuencias = []
    secuencia_por_recorrer = []
    for i in range(len(secuencia)):
        if secuencia[i] != 0: 
            secuencia_por_recorrer.append(secuencia[i]) 
        else:
            if len(secuencia_por_recorrer) > 0:
                secuencias.append(secuencia_por_recorrer)  
                secuencia_por_recorrer = [] 
    #Returno la lista de listas con las secuencias
    return secuencias

#Función que verifique la validez de una secuencia 
def verificar_secuencias(secuencias):
    #Ciclo que elimine las secuencias que no cumplan con la serie 
    secuencias = [secuencia for secuencia in secuencias if len(secuencia) > 2]
    return secuencias

#Función para encontrar cimas en cada secuencia de una lista de secuencias
def encontrar_cimas(secuencias):
    #Lista donde se guarden las cimas(tuplas)
    todas_las_cimas = []
    for secuencia in secuencias:
        cimas = []
        n = len(secuencia)
        inicio_cima = 1
        while inicio_cima < n - 1:
            if secuencia[inicio_cima - 1] < secuencia[inicio_cima]: 
                fin_cima = inicio_cima
                while (fin_cima < n - 1) and (secuencia[fin_cima] == secuencia[fin_cima + 1]): 
                    fin_cima += 1
                if (fin_cima < n - 1) and (secuencia[fin_cima] > secuencia[fin_cima + 1]):  
                    cimas.append((inicio_cima + 1, fin_cima - inicio_cima + 1))  
                inicio_cima = fin_cima 
            inicio_cima += 1
        todas_las_cimas.append(cimas)
    #Devuelve todas las cimas de cada secuencia
    return todas_las_cimas


#Función que cree el archivo de salida
def archivo_salida(cimas):
    #Creación el archivo
    file = open('cimas.txt', 'w', encoding='ascii')
    #Ciclo que escriba en el archivo las cimas
    for cima in cimas:
        for par in cima:
            file.write(f'{par[0]} {par[1]}\n')
        file.write('***\n')
    #Cierre del archivo 
    file.close() 

if __name__ == '__main__':
    secuencias = lectura('datos.txt') 
    secuencias = identificar_secuencias(secuencias)
    secuencias = verificar_secuencias(secuencias)
    cimas = encontrar_cimas(secuencias)
    archivo_salida(cimas)
