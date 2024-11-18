import random

# Función ajustada para incluir menos cimas consecutivas y agregar ceros consecutivos
def generar_secuencia_ajustada():
    secuencia = []
    for _ in range(random.randint(1, 10)):  # Genera entre 1 y 10 números al azar
        if random.random() < 0.15:  # 15% de probabilidad de generar una cima
            cima = str(random.randint(50, 100))  # La cima será un número alto
            repeticiones = random.randint(2, 5)  # Repeticiones de la cima (máximo 5 ahora)
            secuencia.extend([cima] * repeticiones)
        elif random.random() < 0.1:  # 10% de probabilidad de generar ceros consecutivos
            secuencia.extend(['0'] * random.randint(2, 4))  # Entre 2 y 4 ceros consecutivos
        else:
            secuencia.append(str(random.randint(1, 100)))  # Número aleatorio normal
    return ' '.join(secuencia)

# Función actualizada para generar el archivo con menos cimas consecutivas y ceros consecutivos
def generar_archivo_tester_ajustado(nombre_archivo, num_secuencias):
    with open(f'{nombre_archivo}', 'w', encoding='ascii') as file:
        for _ in range(num_secuencias):
            if random.random() < 0.2:  # 20% de probabilidad de insertar una línea en blanco
                file.write('\n')
            elif random.random() < 0.2:  # 20% de probabilidad de insertar un cero aislado
                file.write('0\n')
            else:
                num_lineas = random.randint(1, 3)  # Una secuencia puede ocupar entre 1 y 3 líneas
                for _ in range(num_lineas):
                    secuencia = generar_secuencia_ajustada()
                    # Agregar ceros entre medio en lugar de solo al final de las líneas
                    if random.random() < 0.2:  # 20% de probabilidad de insertar un cero en medio
                        secuencia += ' 0'
                    file.write(secuencia + '\n')

# Generar nuevo archivo de prueba ajustado
nombre_archivo_ajustado = "datos.txt"
generar_archivo_tester_ajustado(nombre_archivo_ajustado, 500)  # Generar 200 secuencias para el archivo ajustado