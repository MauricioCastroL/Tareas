#Autor: Mauricio Castro
#Fecha: 22/08/24

#Funcion que lea el archivo
def lectura(archivo):
    #Listas que tengan los datos
    votos = []
    coaliciones = []
    coa = []
    coalicion = []
    voto = []
    #Variable que habra el archivo
    f = open(archivo, 'r', encoding='UTF-8')
    #Ciclo que agregue a las listas los datos
    for linea in f:
        coaliciones.append(linea.rstrip().split(';'))
        votos.append(linea.rstrip().split('$'))
    #Omito datos innecesarios
    del coaliciones[1]
    del votos[0]
    #Ciclos que ayuden a separar 
    for linea in coaliciones:
        for palabra in linea:
            coa.append(palabra.split(':'))
    for lista in coa:
        for palabra in lista:
            coalicion.append(palabra.split('-'))
    for i in votos:
        for j in i:
            voto.append(j)
    #returno los datos
    return coalicion, voto

#Funcion que cuente los votos
def cantidad_votos(votos):
    cant_votos = []
    voto = set()
    votacion = []
    #Ciclo que cuente los votos
    for i in votos:
        if i not in voto:
            cant_votos.append(votos.count(i))
            voto.add(i)
            votacion.append(i)
    #Lista con los partdos y sus votos juntos
    lista = list(zip(votacion, cant_votos)) 
    #returno la cantidad de votos
    return cant_votos, votacion, lista

def diccionario(coaliciones, partidos_votos, cant_votos, votacion):
    diccionario = {}
    diccionario_final = {}
    clave = None
    valores = dict(partidos_votos)
    #Creo el diccionario
    for lista in coaliciones:
        if len(lista) == 1:
            clave = lista[0]
            diccionario[clave] = []
        else: 
            if clave is not None:
                diccionario[clave].extend(lista)
    #Creo el sugundo diccionario agregando la cantidad de votos           
    for clave, valor in diccionario.items():
        diccionario_final[clave] = {partido: valores.get(partido, 0) for partido in valor}
    #returno el diccionario final con el que mostrare los datos
    return diccionario_final

#Funcion que cree el archivo 
def mostrar(diccionario):
    coalicion_ganadora = None
    votos_ganadora = 0
    #Diccionario que muestre los resultados del ganador
    diccionario_coal_ganadora = {}
    #Creo variable que cree el archivo
    f = open('resultado_elección.txt', 'w', encoding='UTF-8')
    #Ciclo que saque la cuenta 
    for coalicion, partidos in diccionario.items():
        suma_votos = 0
        f.write(f'Coalición: {coalicion}\n')
        for partido, valor in partidos.items():
            f.write(f'{partido}: {valor}\n')
            suma_votos += valor
        diccionario_coal_ganadora[coalicion] = suma_votos
        f.write(f'Total coalición {coalicion}: {suma_votos}\n')
        f.write('\n')
        f.write('\n')
        
    
    #Ciclo que encuentre la coalicion ganadora
    for coalicion, votos in diccionario_coal_ganadora.items():
        if votos > votos_ganadora:
            votos_ganadora = votos
            coalicion_ganadora = coalicion
    f.write(f'La coalición ganadora es {coalicion_ganadora} con {votos_ganadora} votos.\n')




if __name__ == '__main__':
    coaliciones, votos = lectura('elección.txt')
    cant_votos, votacion, partidos_votos = cantidad_votos(votos)
    dic = diccionario(coaliciones, partidos_votos, cant_votos, votacion)
    mostrar(dic)