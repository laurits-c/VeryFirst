from datetime import date
def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)
def esEntero(numero):
    try:
        numero = int(numero)
        return numero
    except ValueError:
        return False
def esFloat(numero):
    try:
        numero=float(numero)
        return numero
    except ValueError:
        return False
def esVacioOEspacio(cadena):
    if cadena.isspace() or cadena == "":
        return True
    else:
        return False

def obtener_nombre():
    correcto = False
    while not correcto:
        nombre = input("Para empezar, dime como te llamas. ")
        if not esVacioOEspacio(nombre):
            correcto = True
        else:
            nombre = input("Dato no válido. Por favor ingresa tu nombre:")
    return nombre

def obtener_edad():
    correcto = False
    agno = 0
    while not correcto:
        agno = input("Dime en qué año naciste. ")
        agno = esEntero(agno)
        if esEntero(agno) and len(str(agno)) == 4:
            correcto = True
        else:
            print(">>>Error, introduce un número entero de 4 cifras")
    return date.today().year - agno - 1


def obtener_estatura():
    correcto = False
    while not correcto:
        estatura = input("¿Cuánto mides? Dímelo en metros. ")
        estatura = esFloat(estatura)
        if estatura and estatura > 0 and estatura <3:
            metros = int(estatura)
            centimetros = int((estatura - metros) * 100)
            correcto = True
        else:
            print('>>>Error, introduce un número distinto de cero con formato m.cm')
    return (metros, centimetros)

def obtener_sexo():
    sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    while sexo != 'M' and sexo != 'F':
        sexo = input(">>> Error, por favor, ingresa una de estas opciones -> M=Masculino, F=Femenino: ")
    return sexo

def obtener_pais():
    correcto = False
    while not correcto:
        pais = input("Indica tu país de nacimiento: ")
        if not esVacioOEspacio(pais):
            correcto = True
        else:
            pais = input(">>> Dato no válido. Por favor ingresa tu país de nacimiento:")
    return pais

def obtener_num_amigos():
    correcto = False
    amigos = 0
    while not correcto:
        amigos = input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. ")
        amigos = esEntero(amigos)
        if esEntero(amigos):
            correcto = True
        else:
            print(">>>Error, introduce un número entero")
    return amigos

def obtener_datos():
    e = obtener_edad()
    (em, ec) = obtener_estatura()
    s = obtener_sexo()
    p= obtener_pais()
    na = obtener_num_amigos()
    return (e,em,ec,s,p,na)

def mostrar_perfil(datos):
    print("--------------------------------------------------")
    print("Nombre:   ", datos["Nombre"])
    print("Edad:     ", datos["Edad"])
    print("Estatura: ", datos["Estaturam"], "m y ", datos["Estaturacm"], "centímetros")
    print("Sexo:     ", datos["Sexo"])
    print("País:     ", datos["Pais"])
    print("Amigos:   ", datos["Amigos"])
    print("--------------------------------------------------")

def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 4:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion
def obtener_mensaje():
    mensaje = input("Qué mensaje deseas enviar?")
    return mensaje

def mensaje_publico(datos):
    mensaje = obtener_mensaje()
    print("--------------------------------------------------")
    print(datos["Nombre"], "dice:", mensaje)
    print("--------------------------------------------------")

def msj_grupal(datos):
    print("--------------------------------------------------")
    mensaje = obtener_mensaje()
    for i in range(len(datos["AmigosMsj"])):
        print(datos["Nombre"], "->",  datos["AmigosMsj"][i], ":", mensaje)
    print("--------------------------------------------------")

def salir(datos):
    print("Gracias, vuelva prontos")

def actualizar_perfil(datos):
    print("--------------------------------------------------")
    print(datos["Nombre"], "Vamos a actualizar tus datos:")
    (e,em,ec,s,p,na)=obtener_datos()
    update = {
        "Edad": e,
        "Estaturam": em,
        "Estaturacm": ec,
        "Sexo": s,
        "Pais":  p,
        "Amigos": na,
        "AmigosMsj": None
    }

    datos.update(update)
    print("--------------------------------------------------")
    return datos

def switch_demo(opcion, datos):
    switcher = {
        0: salir,
        1: mensaje_publico,
        2: msj_grupal,
        3: mostrar_perfil,
        4: actualizar_perfil
    }
    func = switcher.get(opcion)
    return func(datos)

