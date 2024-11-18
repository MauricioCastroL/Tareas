#Autor: Mauricio Castro L.
#Fecha: 11/11/24

def datos_impacto():
    velocidad = float(input('Ingrese la velocidad del proyectil(nudos): '))
    distancia = float(input('Ingrese la distancia del objetivo(Mi. Nautica): '))
    return velocidad, distancia

def calculo_impacto_linea_recta(velocidad, distancia):
    velocidad = cambio_velocidad(velocidad)
    distancia = cambio_distancia(distancia)
    #Suponiendo que el barco siga moviendose en linea recta
    tiempo_linea_recta = distancia / velocidad #segundos
    return tiempo_linea_recta


def cambio_velocidad(velocidad):
    velocidad = velocidad / 1.944
    return velocidad

def cambio_distancia(distancia):
    distancia = distancia * 1852
    return distancia

def mostar(tiempo_linea_recta):
    print(f'Se demora {tiempo_linea_recta}s')

if __name__ == '__main__':
    velocidad, distancia = datos_impacto()
    tiempo_linea_recta = calculo_impacto_linea_recta(velocidad, distancia)
    calculo_impacto_en_movimiento()
    mostar(tiempo_linea_recta), 