#realice un programa que solicite dos numeros por tecladoy
#muestre la suma, resta, multiplicacion y division de los dos numeros
numero1=int(input("ingrese el primer numero:"))
numero2=int(input("ingrese el segundo numero:"))
#realizamos las operaciones solicitadas
suma=numero1+numero2
resta=numero1-numero2
multiplicacion=numero1*numero2
division = numero1/numero2
#mostramos los resultados
print("la suma es:",numero1, " + ", numero2, " = ",suma)
print("la resta es:", numero1, " - ", numero2, " = ", resta)
print("la multiplicacion es:", numero1, " * ", numero2, " = ", multiplicacion)
print("la division es:", numero1, " / ", numero2, " = ", division)