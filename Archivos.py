import os

def existe(pArchivo):
   return os.path.isfile(pArchivo + ".user")

def obtenerDatosUsuario(pNombre):
    # Esto lo hacemos si ya habÃ­a un usuario con ese nombre

    archivo_usuario = open(pNombre + ".user", "r")
    nombre = archivo_usuario.readline().rstrip("\n")
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int((estatura - estatura_m) * 100)
    sexo = archivo_usuario.readline().rstrip("\n")
    pais = archivo_usuario.readline().rstrip("\n")
    num_amigos = int(archivo_usuario.readline())

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
def guardar(pDatos):
    archivo_usuario = open(pDatos["Nombre"]+ ".user", "w")
    archivo_usuario.write(str(pDatos["Nombre"]) + "\n")
    archivo_usuario.write(str(pDatos["Edad"]) + "\n")
    archivo_usuario.write(str(pDatos["Estaturam"] + pDatos["Estaturacm"] / 100) + "\n")
    archivo_usuario.write(pDatos["Sexo"] + "\n")
    archivo_usuario.write(pDatos["Pais"] + "\n")
    archivo_usuario.write(str(pDatos["Amigos"]) + "\n")
    #archivo_usuario.write(estado + "\n")
    # Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
    archivo_usuario.close()