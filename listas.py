# Crea una lista de números cuadrados usando un for loop
cuadrados = []
for numero in range(10):
    cuadrados.append(numero * numero)
# print(cuadrados)

# Crea una lista de transacciones con impuestos calculados utilizando map() y usando en metodo list() para convertir a lista el resultado
transacciones = [1.09, 23.56, 57.84, 4.56, 6.78]
TASA_IMPUESTOS = .13

def obtener_precio_con_impuesto(transaccion):
    return transaccion * (1 + TASA_IMPUESTOS)

precio_final = map(obtener_precio_con_impuesto, transacciones)
# print(list(precio_final))

#Crea una lista  de números cuadrados usando list comprehension
lista_numeros_con_comprehesion = [numero * numero for numero in range(10)]
print(lista_numeros_con_comprehesion)

#sintaxis basica de list comprehension
#nueva_lista = [expresion for miembro in iterable]

#Crea una lista de transacciones con impuestos calculados usando list comprehension
precio_final_list_comprehesion = [ obtener_precio_con_impuesto(transaccion) for transaccion in transacciones]
# print(precio_final_list_comprehesion)

#agregando poderes a nuestras listas usando list comprehension
#nueva_lista = [expresion for miembro in iterable if condicion == True]

oracion = 'el cohete regreso de marte'
vocales = [letra for letra in oracion if letra in 'aeiou']
print(vocales)

precios_originales = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# nuevos_precios = [cantidad if cantidad > 0 else 0 for cantidad in precios_originales]
# print(nuevos_precios)

def obtener_precio(precio):
    return precio if precio > 0 else 0

nuevos_precios = [obtener_precio(cantidad) for cantidad in precios_originales]
# print(nuevos_precios)
