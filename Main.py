import Funciones as fnc
import Archivos as arch
datos ={}
fnc.mostrar_bienvenida()
nombre = fnc.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

if arch.existe(nombre):
    print("<<Leyendo datos de usuario", nombre, "desde archivo>>")
    datos = arch.obtenerDatosUsuario(nombre)
else:
    edad = fnc.obtener_edad()
    (estatura_m, estatura_cm) = fnc.obtener_estatura()
    sexo = fnc.obtener_sexo()
    pais = fnc.obtener_pais()
    num_amigos = fnc.obtener_num_amigos()
    amigos = []
    datos = {
        "Nombre": nombre,
        "Edad": edad,
        "Estaturam": estatura_m,
        "Estaturacm":estatura_cm,
        "Sexo": sexo,
        "Pais": pais,
        "Amigos": num_amigos,
        "AmigosMsj": amigos
        }

print("Muy bien. Estos son los datos de tu perfil.")
fnc.mostrar_perfil(datos)
menu = 1
while(menu > 0 and menu < 5):
    menu = fnc.opcion_menu()
    #Si la opción es 2, completo los datos que va a necesitar la función msj_grupal
    if menu == 2:
        cantidad = int(input("A cuantos amigos eviarás el mensaje?"))
        for i in range(cantidad):
            Amigo= input("Ingresa los nombres de tu amigo "+str(i+1)+" : ")
            datos["AmigosMsj"].append(Amigo)
    #Antes de salir, debe guardar el archivo
    if menu == 0:
        print("Has decidido salir.")
        print("<<Guardando perfil en ", nombre + ".user>>")
        arch.guardar(datos, nombre)
        print("<<Archivo", nombre + ".user", "guardado>>")
    #Ejecutamos la función, en el update, devuelve datos así que lo asignamos a una variable
    aux = fnc.switch_demo(menu, datos)
    #Si ya ejecuto el update, debe mostrar los datos actualizados
    if menu == 4:
        print("Tus datos actualizados son")
        fnc.mostrar_perfil(aux)


