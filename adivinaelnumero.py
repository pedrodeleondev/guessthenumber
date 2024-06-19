import random
numero_aleatorio=random.randint(1,100)
nombre=input("¿Cuál es tu nombre?: ")
print(f"“Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número”.")

for i in range(1,9):
    numero=int(input("\nElige un numero: "))
    if numero<1 or numero>100:
        print("El número no está permitido.")
    elif numero<numero_aleatorio:
        print("El número es menor al número que eligió el programa.")
    elif numero>numero_aleatorio:
        print("El número es mayor al número que eligió el programa.")
    else:
        print(f"El número es correcto, te tomó {i} intentos.")
        break
