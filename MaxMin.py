"""realice un programa que calcule el mayor y menor, 
de 5 numeros ingresados por teclado"""
#inicializamos las variables
menor = None
mayor = None
#pedimos al usuario que ingrese 5 numeros
for i in range(5):
    numero = int(input("Ingrese un numero: "))
    if menor is None or numero < menor:
        menor = numero
    if mayor is None or numero > mayor:
        mayor = numero
#Imprimimos el menor y el mayor
print("El menor es: ", menor)
print("El mayor es: ", mayor)
