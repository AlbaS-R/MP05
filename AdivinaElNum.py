import random

nom_usu = str(input("Cual es tu nombre:"))
def juego():
    resp_usu = 0
    numRandom = random.randint(1, 100)
    intentos = 1
    contador = 10

    while resp_usu != numRandom and intentos <= contador:
        resp_usu = int(input(f"Hola {nom_usu}, ecoje un número del 1 al 100: "))
        print(f"Te quedan {contador - intentos}.")
        if resp_usu > numRandom:
            print("Este número es demasiado grande, bajale.")
        elif resp_usu < numRandom:
            print("Este número es muy pequeño, subele.")

        intentos += 1

    if resp_usu == numRandom:
        print("Felicidades, lo has conseguido.")
    else:
        print(f"Has fallado, el numero era {numRandom}")

decision = "S"
while decision != "N":  
    juego()
    decision = input("Quieres volver a jugar? S/N: ").upper()

print("Gracias por jugar.")
