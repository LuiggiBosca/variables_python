#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Operadores con números decimales
    print('Ingrese el primer número decimal a operar:')
    numero_1 = float(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = float(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)
    print(numero_1, numero_2)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    suma = numero_1 + numero_2
    print('el resultado de sumar', numero_1, 'y', numero_2, 'es', suma)
    
    # Resta
    resta = numero_1 - numero_2
    print('el resultado de restar', numero_1, 'y', numero_2, 'es', resta)

    # División
    cociente = numero_1 / numero_2
    print('el resultado del cociente', numero_1, 'y', numero_2, 'es', cociente)

    # Multiplicación
    producto = numero_1 * numero_2
    print('el resultado del producto', numero_1, 'y', numero_2, 'es', producto)

    print('hola')




def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números reales
    print('Ingrese el primer número real a operar:')
    numero_3 = float(input())

    print('Ingrese el segundo número real a operar:')
    numero_4 = float(input())

    # Alumno: Imprima en pantalla los dos números reales solicitados
    # print(....)
    print(numero_3, numero_4)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_3, numero_4
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    suma = numero_3 + numero_4
    print('el resultado de sumar', numero_3, 'y', numero_4, 'es', suma)

    # Resta
    resta = numero_3 - numero_4
    print('el resultado de restar', numero_3, 'y', numero_4, 'es', resta)

    # División
    cociente = numero_3 / numero_4
    print('el resultado del cociente', numero_3, 'y', numero_4, 'es', cociente)

    # Multiplicación
    producto = numero_3 * numero_4
    print('el resultado del producto', numero_3, 'y', numero_4, 'es', producto)

    print('hola')




def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo
    print('mi nombre completo es', nombre, '', apellido)

    # Almacenar su nombre completo en una variable
    # nombre_completo = .....
    nombre_completo = 'luis fragueda'

    # Imprimir la cantidad de letras que posee su nombre completo
    luis_fragueda_len = len(nombre_completo)
    print(nombre_completo, 'tiene', luis_fragueda_len, 'caracteres')

    print('hola')




def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Palaras elegidas = yacimientos petroliferos fiscales

    caracter_inicial = palabra_1[0]
    print(caracter_inicial)

    caracter_inicial = palabra_2[0]
    print(caracter_inicial)

    caracter_inicial = palabra_3[0]
    print(caracter_inicial)
    
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla

    print('%s,%s,%s' % (palabra_1[0], palabra_2[0], palabra_3[0]))

    print('hola')


    

def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    # Palabra_1 = guitarra, palabra_2 = bateria
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    sub_text_1 = palabra_1[:3] 
    
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    sub_text_2 = palabra_2[4:]
    # Formar una nueva palabra con los recortes solicitados
    nueva_palabra = sub_text_1 + sub_text_2
    # Imprima en pantalla los resultados
    print(nueva_palabra)

    print('hola')



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
