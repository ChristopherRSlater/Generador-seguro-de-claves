#Generador seguro de contraseñas
import random

# Conjuntos de caracteres
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnñopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%^&*?"

nombre = input("Bienvenido al generador de contraseñas, cual es su nombre: ")
generar_contraseña = input(f"Hola {nombre}, desea generar una contraseña (s/n): ").lower()

if generar_contraseña == "s":
    longitud = int(input("¿Cuántos caracteres quiere eque tenga su contraseña? "))# El usuario elige la longitud
# El usuario decide qué incluir
    usar_mayus = input("¿Quieres mayúsculas? (s/n): ").lower() == "s"
    usar_minus = input("¿Quieres minúsculas? (s/n): ").lower() == "s"
    usar_numeros = input("¿Quieres números? (s/n): ").lower() == "s"
    usar_simbolos = input("¿Quieres símbolos? (s/n): ").lower() == "s"

# Crear el conjunto de caracteres según lo que elija el usuario
caracteres = ""
if usar_mayus == "s":
    caracteres += mayusculas
if usar_minus:
    caracteres += minusculas
if usar_numeros:
    caracteres += numeros
if usar_simbolos:
    caracteres += simbolos

# Generar la contraseña
contraseña = ""
for i in range(longitud):
    contraseña += random.choice(caracteres)

print("Tu contraseña es:", contraseña)