estudiantes = []
#Creé una lista vacía para almacenar los estudiantes

def buscar_estudiante(ID_estudiante):
    return next((e for e in estudiantes if e["ID"] == ID_estudiante), None)

def pedir_entero(mensaje):
    return int(input(mensaje))

def pedir_texto(mensaje):
    return input(mensaje).strip()

#Definí las funciones para buscar, pedir números y textos para la busqueda de estudiantes y la entrada de datos


# ESTUDIANTES
def agregar_estudiante():
    ID_estudiante = pedir_entero("ID: ")

    if buscar_estudiante(ID_estudiante):
        print("Ya existe un estudiante con ese ID.")
        return

    estudiante = {
        "ID": ID_estudiante,
        "nombre": pedir_texto("Nombre: "),
        "edad": pedir_entero("Edad: "),
        "grupo": pedir_texto("Grupo: "),
        "cursos": {}
    }

    estudiantes.append(estudiante)
    print("Estudiante agregado correctamente.")

#Con esta funcion puedo agregar estudiantes pidiendo su ID, nombre, edad y grupo. Si el ID ya existe, no se agrega el estudiante. Además crea un diccionario con los datos del estudiante y los guarda en la lista.

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for e in estudiantes:
        print(f"\nID: {e['ID']}")
        print(f"Nombre: {e['nombre']}")
        print(f"Edad: {e['edad']}")
        print(f"Grupo: {e['grupo']}")
        print(f"Cursos: {e['cursos']}")

#Con esta función puedo mostrar todos los estudiantes registrados, mostrando su ID, nombre, edad, grupo y cursos. Si no hay estudiantes registrados, muestra un mensaje indicando que no hay estudiantes.

def actualizar_estudiante():
    ID_estudiante = pedir_entero("ID: ")
    estudiante = buscar_estudiante(ID_estudiante)

    if not estudiante:
        print("No encontrado.")
        return

    estudiante["nombre"] = pedir_texto("Nuevo nombre: ")
    estudiante["edad"] = pedir_entero("Nueva edad: ")
    estudiante["grupo"] = pedir_texto("Nuevo grupo: ")

    print("Actualizado correctamente.")

#Con esta función puedo actualizar los datos de cada estudiante, pidiendo su ID y luego los nuevos datos, si el estudiante no se escucentra muestra un mensaje que no se encuentra el estudiante.

def eliminar_estudiante():
    ID_estudiante = pedir_entero("ID: ")
    estudiante = buscar_estudiante(ID_estudiante)

    if estudiante:
        estudiantes.remove(estudiante)
        print("Eliminado correctamente.")
    else:
        print("No encontrado")

#Con esta función puedo eliminar un estudiante, pidiendo su ID y si se encuentra lo elimina de la lista, si no se encuentra muestra un mensaje que no se encuentra el estudiante.
 
# CURSOS
def asignar_curso():
    ID_estudiante = pedir_entero("ID: ")
    estudiante = buscar_estudiante(ID_estudiante)

    if not estudiante:
        print("No encontrado.")
        return

    curso = pedir_texto("Curso: ")

    if curso not in estudiante["cursos"]:
        estudiante["cursos"][curso] = []
        print("Curso asignado")
    else:
        print("El curso ya existe")

#Con esta función asigno un curso a un estudiante, pidiendo su ID y el nombre del curso. Si el estudiante no se encuentra, muestra un mensaje que no se encuentra el estudiante. Si el curso ya existe para ese estudiante, muestra un mensaje indicando que el curso ya existe.

def agregar_calificacion():
    ID_estudiante = pedir_entero("ID: ")
    estudiante = buscar_estudiante(ID_estudiante)

    if not estudiante:
        print("No encontrado.")
        return

    curso = pedir_texto("Curso: ")

    if curso not in estudiante["cursos"]:
        print("El estudiante no está en ese curso.")
        return

    calificacion = float(input("Calificación: "))
    estudiante["cursos"][curso].append(calificacion)

    print("Calificación agregada.")

#Con esta función agrego una calificación a un curso de un estudiante, pidiendo su ID, el nombre del curso y la calificación. Si el estudiante no se encuentra, muestra un mensaje que no se encuentra el estudiante. Si el curso no existe para ese estudiante, muestra un mensaje indicando que el estudiante no está en ese curso.

def promedio_estudiante():
    ID_estudiante = pedir_entero("ID: ")
    estudiante = buscar_estudiante(ID_estudiante)

    if not estudiante:
        print("No encontrado.")
        return

    total = 0
    cantidad = 0

    for notas in estudiante["cursos"].values():
        total += sum(notas)
        cantidad += len(notas)

    if cantidad == 0:
        print("Sin calificaciones.")
    else:
        print(f"Promedio: {total / cantidad:.2f}")

#Finalmente con esta función puedo calcular el promedio de todas las calificaciones de un estudiante, pidiendo su ID. Si el estudiante no se encuentra, muestra un mensaje que no se encuentra el estudiante. Si no tiene calificaciones, muestra un mensaje indicando que no tiene calificaciones. Si tiene calificaciones, muestra el promedio de todas las calificaciones.

# MENÚ
def menu():
    while True:
        print("\n--GESTION DE ESTUDIANTES DE ANGIE--")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Asignar curso")
        print("6. Agregar calificación")
        print("7. Ver promedio")
        print("8. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            actualizar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            asignar_curso()
        elif opcion == "6":
            agregar_calificacion()
        elif opcion == "7":
            promedio_estudiante()
        elif opcion == "8":
            print("Programa finalizado")
            break
        else:
            print("Opción inválida")

#Con esta función puedo mostrar un menú con las opciones disponibles para gestionar los estudiantes, permitiendo al usuario elegir la opción deseada y ejecutando la función correspondiente. Si el usuario elige salir, el programa finaliza.

menu()
#Es la instrucción que inicia el programa y ejecuta el menú principal