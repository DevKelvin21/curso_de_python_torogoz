#Creando un set con list comprehension
frase = "el cohete regreso de marte"
vocales_unicas = {letra for letra in frase if letra in 'aeiou'}
# print(vocales_unicas)

#Creando un diccionario con list comprehension
cuadrados = {numero: numero * numero for numero in range(10)}
# print(cuadrados)

my_diccionario = {
    "numero": 888
}


mis_contactos = {
    "Miguel": {
        "telefono": 12345678,
        "esfavorito": True,
    },
    "Jose": {
        "telefono": 87654321,
        "esfavorito": False,
    },
    "Milton": {
        "telefono": 12345678,
        "esfavorito": True,
    },
    "Diego": {
        "telefono": 87654321,
        "esfavorito": False,
    },
    "Carlos": {
        "telefono": 12345678,
        "esfavorito": True,
    },
    "Juan": {
        "telefono": 87654321,
        "esfavorito": False,
    },
    "Pedro": {
        "telefono": 12345678,
        "esfavorito": True,
    },
    "Luis": {
        "telefono": 87654321,
        "esfavorito": False,
    },
    "Jorge": {
        "telefono": 12345678,
        "esfavorito": True,
    },
    "Mario": {
        "telefono": 87654321,
        "esfavorito": False,
    },
    "Jaime": {
        "telefono": 12345678,
        "esfavorito": True,
    },
}

# print(mis_contactos["Miguel"]["telefono"])

#Creando un diccionario con list comprehension partiendo de mis contactos solo si son favoritos
contactos_favoritos = {llave: contacto for llave, contacto in mis_contactos.items() if contacto["esfavorito"]}
print(contactos_favoritos)