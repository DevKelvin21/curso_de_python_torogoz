import random
import timeit

TASA_IMPUESTO = .13

transacciones = [random.randrange(100) for _ in range(100000)]

def obtener_precio(transaccion):
    return transaccion * (1 + TASA_IMPUESTO)

def obtener_precios_con_map():
    return list(map(obtener_precio, transacciones))

def obtener_precios_con_comprehension():
    return [obtener_precio(transaccion) for transaccion in transacciones]

def obtener_precios_con_loop():
    precios = []
    for transaccion in transacciones:
        precios.append(obtener_precio(transaccion))
    return precios

print(timeit.timeit(obtener_precios_con_map, number=100))

print(timeit.timeit(obtener_precios_con_comprehension, number=100))

print(timeit.timeit(obtener_precios_con_loop, number=100))
