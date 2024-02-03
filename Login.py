numero=0
while numero < 3:
    user = input("Ingrese el usuario: ")
    passw = input("Ingrese la contraseña: ")
    if user == "admin" and passw == "123":
        print("Bienvenido")
        break
    numero = numero + 1