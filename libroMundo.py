import json
import os

def agregarAutor():
    with open("biblioteca.json", mode="w") as libreria:
        leerjson = json.load(libreria)
        agregarjason= {
            "autorID": int(input("ingrese una id: ")),
            "nombre": input("ingrese un nombre: "),
            "Nacionalidad": input("ingrese la nacionalidad: ")
        }
        
    return leerjson, agregarjason

def ActualizarAutor():
    with open("biblioteca.json", mode="r") as libreria:
            nombre = input("ingrese el nombre para actualizar: ")
            leerjson = json.load(libreria)
            nacinalidad = input("ingrese el pais para actualizar: ")
            for ind in len(leerjson):
                if leerjson["Nombre"] == nombre:
                    input("ingrese su nuevo nombre: ")
                else:
                     print("usuario no encontrado")
                if leerjson["Nacionalidad"] == nacinalidad:
                    input("ingrese su nueva nacionalida: ")
                break
                     
    return leerjson, ind




while True:
    print("****************************")
    print("*        MUNDO LIBRO       *")
    print("****************************")
    print("[1] - Mantenedores de autores")
    print("[2] - reportes ")
    print("[3] - salir ")

    opc= int(input("elija una opción: "))
    match opc:
        case 1:  
            print("****************************")
            print("*    MANTENEDOR AUTORES    *")
            print("****************************")
            print("[1] - Agregar Autor")
            print("[2] - Editar autor")
            print("[3] - Eliminar autor ")
            print("[4] - Buscar autor")
            print("[5] - Volver")
            int(input("elija una opción: "))
        case 2:
            print()

        case 3:
            break