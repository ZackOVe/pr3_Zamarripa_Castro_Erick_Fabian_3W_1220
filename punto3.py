print("")
print("Zamarripa Castro Erick Fabián 3w 1220")
print("")

#Creacion de diccionario
precio_frutas = {
    'Melon': 5.6,
    'Sandia': 4.4,
    'Platano': 3.2,
    'Pera': 1.4,
    'Mango': 1.2
}

#Pedira la introduccion de la fruta y cuanto va a llevar
frutas = input("Ingrese la fruta de su seleccion: ")
print("")
kilos = float(input("Ingrese la cantidad de kilos que quiere comprar: "))
print("")

#Imprimira si la fruta esta y cuanto dinero sera, en caso de no estar imprimira un mensaje avisando
if frutas in precio_frutas:

    precio_final = precio_frutas[frutas] * kilos

    print(f"{kilos} kilos de {frutas} serán: {precio_final:.2f} de dineros")
    print("")
    print (precio_frutas[frutas])

else:
    print ("No tenemos esa fruta")
    print("")

