nombre1 = input("Hola jugador 1, ¿cómo te llamas?: ")
nombre2 = input("Hola jugador 2, ¿cómo te llamas?: ")

input1 = "¿qué elegis, piedra, papel o tijera?: "

jugador1 = input(f"{nombre1}, {input1}")
jugador2 = input(f"{nombre2}, {input1}")

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 == "papel"

hay_empate = True
hay_empate = (jugador1 == jugador2)

while hay_empate == True:
    print("ha sido un empate!")
    jugador1 = input(f"{nombre1}, {input1}")
    jugador2 = input(f"{nombre2}, {input1}")
    hay_empate = (jugador1 == jugador2)
    
condicion1
condicion2 
condicion3 

if condicion1 or condicion2 or condicion3:
    print(f"ha ganado {nombre1} !")
else:
    print(f"ha ganado {nombre2} !")

    
    
    
