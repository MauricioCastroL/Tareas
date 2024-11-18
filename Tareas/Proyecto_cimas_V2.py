

def lectura(archivo):
    datos = []
    file = open(archivo, 'r', encoding='ASCII')
    for i in file:
        linea = i.rstrip().split()
        for j in linea:
            datos.append(int(j))
    return datos
        
def iden_secuencias(datos):
    secuencia = []
    list_secuencia = []
    for numero in datos:
        if numero != 0:
            list_secuencia.append(numero)
        else:
            secuencia.append(list_secuencia)
            list_secuencia = []
    return secuencia

def validez_secuencias(secuencias):
    secuencias = [secuencia for secuencia in secuencias if len(secuencia) > 2]
    print(secuencias)
    return secuencias

def iden_cimas(secuencias):
    cimas = []
    for secuencia in secuencias:
        n = len(secuencia)
        for i in range(n - 1):
            if (secuencia[i - 1] < secuencia[i]) and (secuencia[i] > secuencia[i + 1]): 
                cimas.append((i + 1, 1))
            elif (secuencia[i - 1] < secuencia[i]) and (secuencia[i] == secuencia[i + 1]):
                j = i
                while (j < n - 1) and (secuencia[j] == secuencia[j + 1]): 
                        j += 1
                if (j < n - 1) and (secuencia[j] > secuencia[j + 1]):  
                    cimas.append((i + 1, j - i + 1))
    return cimas

def salida(cimas):
    file = open('cimas_V2.txt', 'w', encoding='ASCII')
    for cima in cimas:
        file.write(f'{cima[0]} {cima[1]}\n')
    file.close()


if __name__ == '__main__':                  
    datos = lectura('datos.txt')
    secuencias = iden_secuencias(datos)
    secuencias = validez_secuencias(secuencias)
    cimas = iden_cimas(secuencias)
    salida(cimas)