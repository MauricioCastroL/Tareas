#Autor: Mauricio Castro l
#Fecha: 07/10/24

def lectura(covid, aviar, porcina):
    #Listas con los datos
    lista_covid = []
    lista_aviar = []
    lista_porcina = []
    #Aperturas de los archivos
    with open(covid, 'r', encoding='UTF-8') as f:
        for linea in f:
            if linea.startswith(4 * ' '):
                lista_covid.append(linea.rstrip('\n').strip())
    lista_covid = [elemento.strip() for elemento in lista_covid]

    with open(aviar, 'r', encoding='UTF-8') as file:
        for linea in file:
            if linea.startswith(4 * ' '):
                lista_aviar.append(linea.rstrip('\n').strip())
    lista_aviar = [elemento.strip() for elemento in lista_aviar]

    with open(porcina, 'r', encoding='UTF-8') as archivo:
        for linea in archivo:
            if linea.startswith(4 * ' '):
                lista_porcina.append(linea.rstrip('\n').strip())
    lista_porcina = [elemento.strip() for elemento in lista_porcina]

    return lista_covid,  lista_aviar, lista_porcina

def comunes(covid, aviar, porcina):
    covid_elementos = []
    aviar_elementos = []
    porcina_elementos = []

    for item in covid:
        # Encuentra el inicio y el final de la lista de elementos
        inicio = item.find('[') + 1
        fin = item.find(']')
        # Extrae los elementos y los divide por comas
        covid_elementos.extend(item[inicio:fin].replace('"', '').split(', '))

    for item in aviar:
        # Encuentra el inicio y el final de la lista de elementos
        inicio = item.find('[') + 1
        fin = item.find(']')
        # Extrae los elementos y los divide por comas
        aviar_elementos.extend(item[inicio:fin].replace('"', '').split(', '))
    
    for item in porcina:
        # Encuentra el inicio y el final de la lista de elementos
        inicio = item.find('[') + 1
        fin = item.find(']')
        # Extrae los elementos y los divide por comas
        porcina_elementos.extend(item[inicio:fin].replace('"', '').split(', '))

    covid_set = set(covid_elementos)
    aviar_set = set(aviar_elementos)
    porcina_set = set(porcina_elementos)

    # Encontrar los elementos comunes
    comunes = covid_set.intersection(aviar_set, porcina_set)
    return comunes

def mostar(comun):
    with open('dictmatchvacuna.txt', 'w', encoding='UTF-8') as f:
        f.write(f'los elementos comunes en las\n') 
        f.write(f'vacunas de las tres epidemias son: \n')
        f.write(f'{comun}')

if __name__ == '__main__':
    covid, aviar, porcina = lectura('covid19.txt', 'aviar.txt', 'porcina.txt')
    comun = comunes(covid, aviar, porcina)
    mostar(comun)
