import os

def existe(pArchivo):
   return os.path.isfile(pArchivo + ".user")

def obtenerDatosUsuario(pNombre):
    # Esto lo hacemos si ya habÃ­a un usuario con ese nombre

    archivo_usuario = open(pNombre + ".user", "r")
    nombre = archivo_usuario.readline()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int((estatura - estatura_m) * 100)
    sexo = archivo_usuario.readline()
    pais = archivo_usuario.readline()
    num_amigos = int(archivo_usuario.readline())
    #estado = archivo_usuario.readline()
    # Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    datos = {
        "Nombre": nombre,
        "Edad": edad,
        "Estaturam": estatura_m,
        "Estaturacm":estatura_cm,
        "Sexo": sexo,
        "Pais": pais,
        "Amigos": num_amigos,
        "AmigosMsj": []
        }
    return datos
def guardar(pDatos, pNombre):

    archivo_usuario = open(pNombre + ".user", "w")
    archivo_usuario.write(pNombre + "\n")
    archivo_usuario.write(str(pDatos["Edad"]) + "\n")
    archivo_usuario.write(str(pDatos["Estaturam"] + pDatos["Estaturacm"] / 100) + "\n")
    archivo_usuario.write(pDatos["Sexo"] + "\n")
    archivo_usuario.write(pDatos["Pais"] + "\n")
    archivo_usuario.write(str(pDatos["Amigos"]) + "\n")
    #archivo_usuario.write(estado + "\n")
    # Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
    archivo_usuario.close()