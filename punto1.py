print("")
print("Zamarripa Castro Erick Fabián 3w 1220")
print("")

#Creacion de diccionario con las divisas
diccionario = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥'
}

#Pide al usuario que ingrese la divisa 
qwer = str(input("Ingrese una divisa: "))

#Verifcara o no que la divisa esta dentro del diccionario y mostrara el simbolo
if qwer in diccionario:
    print (diccionario[qwer])
else:
    print ("Ingresa una valida")
    print("")