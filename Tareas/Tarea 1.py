#Autor: Mauricio Castro
#Fecha: 21/08/24

#Funcion que reciba los datos a trabajar
def datos():
    #Diccionario con los datos
    estudiantes = {"Ana": [8, 9, 7, 10],
                   "Julia": [8, 9, 7, 10],
                   "Adriana": [8, 9, 7, 10],
                   "Benjamín": [8, 9, 7,10],
                   "Diego": [8, 9, 7, 10], 
                   "Juan": [8, 9, 7, 10],
                   "María": [9, 10, 9, 8],
                   "Pedro": [7, 8, 6, 9]
                   }
    return estudiantes

#Funcion que calcule los promedios
def promedios(diccionario):
    promedio = {}
    #Ciclo que recorra el diccionario
    for clave, valor in diccionario.items():
        promedio[clave] = sum(valor) / len(valor)
    #returno diccionario con los promedios
    return promedio

#Funcion que calcule la nota máx.
def nota_max(dicccioanrio):
    nota_maxima = {}
    #Ciclo que recorra el diccionario
    for clave, valor in dicccioanrio.items():
        nota_maxima[clave] = max(valor)
    #returno diccionario con las notas más altas
    return nota_maxima

#Funcion que calcule la nota mín
def nota_min(diccionario):
    nota_minima = {}
    #Ciclo que recorra el diccionario
    for clave, valor in diccionario.items():
        nota_minima[clave] = min(valor)
    #returno el diccionario con la nota más baja
    return nota_minima

#Funcion que imprima los resultados
def mostrar(promedio, nota_maxima, nota_minima):
    #Ciclo que imprima los resultados
    for clave, promedios in promedio.items():
        print(f'El promedio de {clave} es: {promedios}')
    print()
    #Ciclo que imprima las notas más altas
    for clave, nota in nota_maxima.items():
        print(f'La nota más alta de {clave} es: {nota}')
    print()
    #Ciclo que imprima las notas más bajas
    for clave, valor in nota_minima.items():
        print(f'La nota más baja de {clave} es: {valor}')


if __name__ == '__main__':
    diccionario = datos()
    promedio = promedios(diccionario)
    nota_maxima = nota_max(diccionario)
    nota_minima = nota_min(diccionario)
    mostrar(promedio, nota_maxima, nota_minima)