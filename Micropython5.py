# Micropython: NO.5
#Juego de los palitos
import random
#Funciones
#Creamos un array vacio para los jugadores limitado a 5
def agregar_jugadores():
    player_list = []
    while len(player_list) < 5:
        player = input("Ingrese el nombre del jugador: ")
        if isinstance(player, str) and player:
            player_list.append(player)
        else:
            print("Ingrese un nombre valido")
        if len(player_list) == 5:
            print("Ya se han ingresado los 5 jugadores")
            break
    return player_list
#Creamos un array vacio para los palitos limitado al numero de jugadores
def crear_palitos():
    palitos_list = []
    for _ in range (5):
        longitud = random.randint(1,5)
        palitos = "-" * longitud
        palitos_list.append(palitos)
    return palitos_list
#Asignamos los palitos a los jugadores
def asignar_palitos(player_list, palitos_list):
    player_palitos = {}
    for i in range(5):
        player_palitos[player_list[i]] = palitos_list[i]
    return player_palitos
#Determinamos el "ganador" o el palito mas corto
def winner (player_palitos):
    min_lenght = min (len(palitos) for palitos in player_palitos.values())
    for player,palitos in player_palitos.items():
        if len(palitos) == min_lenght:
            print (f"El perdedor es {player}")
            return player
    else:
        print("No hay perdedor")
        return None
#Inicio del juego
print("Bienvenido al juego de los palitos")
jugadores = agregar_jugadores()
palitos = crear_palitos()
jugadores_palitos = asignar_palitos(jugadores, palitos)
ganador = winner(jugadores_palitos)
print("\nAsignación de palitos a jugadores:")
for player, palitos in jugadores_palitos.items():
    print(f"{player}: {palitos}")
