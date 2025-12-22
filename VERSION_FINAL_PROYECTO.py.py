import random
#importar libreria extra para cifrar las claves en una base de datos (extra del proyecto)
import hashlib
#Funcion de cifrado de contraseña
def cifrar_clave(clave):
    return hashlib.sha256(clave.encode()).hexdigest()

#Creamos una lista con elementos tupla que contengan los caracteres inmutables
caracteres=[("QWERTYUIOPLKJHGFDSAZXCVBNMÑ"),("qwertyuiopasdfghjklzxcvbnmñ".lower()) ,("*?><][{}]+=&%$#@!"),("0123456789")]
nombre = str(input("Bienvenido, cual es su nombre? "))
entrada = input(f"Hola {nombre}, ademas de generar su contraseña, desea incluir su contraseñá cifrada? (si/no) ").lower()

if entrada == "si" or "no":
    longitud = int(input("Ingrese la longitud deseada para su contraseña "))
    mayus = input("Desea incluir mayusculas? (s/n)").lower()
    minus = input("Desea incluir minusculas? (s/n)").lower()
    simbolos = input("Desea incluir simbolos? (s/n)").lower()
    numeros = input("Desea incluir numeros? (s/n)").lower
    base = ""
    if mayus == "s":
        base += caracteres[0]
    if minus == "s":
        base += caracteres[1]
    if simbolos == "s":
        base += caracteres[2]   
    if numeros == "s":
        base += caracteres[3]

    clave = ""
    for i in range(longitud):
        clave += random.choice(base)

# CIFRADO SOLO SI EL CLIENTE DICE "SI"
if entrada == "si":
    clave_cifrada = cifrar_clave(clave)
    print(f"Su contraseña es: {clave}, y su contraseña cifrada con sha256 es: {clave_cifrada}")
elif entrada == "no":
    print(f"Su contraseña generada es: {clave}")