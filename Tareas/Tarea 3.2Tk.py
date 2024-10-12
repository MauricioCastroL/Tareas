#Autor: Mauricio Castro
#Fecha: 02/09/24

def factorial():
    valor_factorial = int(input('Ingrese un valor entero y positivo: '))
    valor = valor_factorial
    if valor_factorial == 0:
        valor_factorial = 1
    if valor_factorial > 0:
        resultado = 1
        for i in range(1, valor_factorial + 1):
            resultado *= i
    valores = [valor, resultado]
    return valores

def suma(valor):
    suma = 0
    for i in range(1, valor[0] + 1):
        suma += i
    return suma

def mostrar(valor, sumas):
    print(f'El factorial de {valor[0]} es {valor[1]}')
    print(f'La suma de {valor[0]} es {sumas}')

if __name__ == '__main__':
    valor_factorial = factorial()
    sumas = suma(valor_factorial)
    mostrar(valor_factorial, sumas)

  