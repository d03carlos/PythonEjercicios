"""
Realice un programa que solicite un color por teclado e
imprima puede pasar si el color ingresado es verde,
precausion si el color ingresado es amarillo, no puede
pasar si ele color ingresado es rojo
"""
color = input("Ingrese un color: ")
if color == "verde":
    print("Puede pasar")
elif color == "amarillo":
    print("Precausion")
elif color == "rojo":
    print("No puede pasar")
print('------------------------')
