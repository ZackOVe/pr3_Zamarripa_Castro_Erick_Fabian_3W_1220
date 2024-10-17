print("")
print("Zamarripa Castro Erick Fabián 3w 1220")
print("")

#Creacion de diccionario
diccionario = {
    'nombre': ' ',
    'edad': ' ',
    'direccion': ' ',
    'telefono': ' '
}

#Pedira al usuario la introduccion de sus datos
diccionario ['nombre'] = str(input("Introduzca su nombre completo empezando por apellido paterno: "))
print ("")
diccionario['edad'] = str(input("Introduzca su edad: "))
print ("")
diccionario['direccion'] = str(input("Introduzca direccion: "))
print ("")
diccionario['telefono'] = str(input("Introduzca numero de telefono: "))
print ("")

#Imprimira los datos brindados por el usuario
print (diccionario['nombre'])
print ("")
print ("Tiene:")
print (diccionario['edad'])
print ("")
print ("Vive en:")
print (diccionario['direccion'])
print ("")
print ("Su numero es:")
print (diccionario['telefono'])
print ("")