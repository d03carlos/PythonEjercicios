"""Realice un programa que cuente del 1 al 100 e 
imprima los numeos que son divisibles por 3 y 5"""
for numero in range(1, 101):
    if numero % 5 == 0 and numero % 3 == 0:
        print(numero)