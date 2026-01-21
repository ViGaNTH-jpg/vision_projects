print(name)

# Built-in method input(argument) - se utiliza para que el usuario ingrese datos
user_name = input("¿Cómo te llamas?: ")
edad_txt = input("¿Cuál es tu edad?: ")

# Built-in method type(1 argument) - Nos dice el tipo de variable
print(user_name)
print(type(user_name))

print(edad_txt)
print(type(edad_txt))

# Método built-in int(1-argument) - Convierte un string a un número entero
try:
    edad = int(edad_txt)
    print(edad)
    print(type(edad))

except ValueError:

    print("Error; la conversion no se pudo realizar")
    print("Debes ingresar un numero entero")

print("Fin del programa chavo")