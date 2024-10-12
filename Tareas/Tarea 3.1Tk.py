#Autor: Mauricio Castro
#Fecha: 02/09/24

def potencia(computadorW, cafeteriaW, hieleraW):
    computadorW = computadorW * 15
    consumoW = {'Laboratorio': computadorW, 'Cafeteria': cafeteriaW, 'Hielera': hieleraW}
    return consumoW

def amperios(computadorW, cafeteriaW, hieleraW):
    tension = 220
    computadorA = round(computadorW * 15 / tension, 2)
    cafeteriaA = round(cafeteriaW / tension, 2)
    hieleraA = round(hieleraW / tension, 2)
    consumoA = {'Laboratorio': computadorA, 'Cafeteria': cafeteriaA, 'Hielera': hieleraA}
    return consumoA

def mostrar_consum_watts(consumow, consumoa):
    for clave, valor in consumow.items():
        print(f'El consumo en watts de {clave} es de {valor}W')
    print()
    for clave, valor in consumoa.items():
        print(f'El consumo en Amperios de {clave} es de {valor}A')

if __name__ == '__main__':
    consumow = potencia(800, 500, 500)
    consumoa = amperios(800, 500, 500)
    mostrar_consum_watts(consumow, consumoa)
