print("****BIENVENIDOS****")

import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

def pedir_nombre_equipo(numero):
    while True:
        nombre = input(f"Ingrese el nombre del equipo {numero}: ").strip()
        if nombre != "":
            return nombre
        print("El nombre no puede estar vacío. Intente de nuevo.")

def RegistraSet(equipo_ganador_num):
    if equipo_ganador_num == 1:
        equipo1.setGanados += 1
    elif equipo_ganador_num == 2:
        equipo2.setGanados += 1

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarSet():
    puntos_equipo1 = Puntos()
    puntos_equipo2 = Puntos()

    if puntos_equipo1 >= 25 or puntos_equipo2 >= 25:
        if puntos_equipo1 > puntos_equipo2:
            return 1
        elif puntos_equipo2 > puntos_equipo1:
            return 2
        else:
            while puntos_equipo1 == puntos_equipo2 or (puntos_equipo1 < 25 and puntos_equipo2 < 25):
                puntos_equipo1 += PuntosExtras()
                puntos_equipo2 += PuntosExtras()
            if puntos_equipo1 > puntos_equipo2 and puntos_equipo1 >= 25:
                return 1
            elif puntos_equipo2 > puntos_equipo1 and puntos_equipo2 >= 25:
                return 2
    else:
        while puntos_equipo1 < 25 and puntos_equipo2 < 25:
            puntos_equipo1 += PuntosExtras()
            puntos_equipo2 += PuntosExtras()
        if puntos_equipo1 > puntos_equipo2 and puntos_equipo1 >= 25:
            return 1
        elif puntos_equipo2 > puntos_equipo1 and puntos_equipo2 >= 25:
            return 2
        else:
            while puntos_equipo1 == puntos_equipo2 or (puntos_equipo1 < 25 and puntos_equipo2 < 25):
                puntos_equipo1 += PuntosExtras()
                puntos_equipo2 += PuntosExtras()
            if puntos_equipo1 > puntos_equipo2 and puntos_equipo1 >= 25:
                return 1
            elif puntos_equipo2 > puntos_equipo1 and puntos_equipo2 >= 25:
                return 2

def JugarPartido():
    equipo1.setGanados = 0
    equipo2.setGanados = 0

    while equipo1.setGanados < 3 and equipo2.setGanados < 3:
        ganador_set = JugarSet()
        RegistraSet(ganador_set)

    if equipo1.setGanados == 3:
        equipo1.partidosGanados += 1
        equipo2.partidosPerdidos += 1
    elif equipo2.setGanados == 3:
        equipo2.partidosGanados += 1
        equipo1.partidosPerdidos += 1

def ResultadoTorneo():
    print("\nResultados del Torneo:")
    print(f"{equipo1.nombre}: Partidos Ganados = {equipo1.partidosGanados}, Partidos Perdidos = {equipo1.partidosPerdidos}")
    print(f"{equipo2.nombre}: Partidos Ganados = {equipo2.partidosGanados}, Partidos Perdidos = {equipo2.partidosPerdidos}")

def main():
    nombre1 = pedir_nombre_equipo(1)
    nombre2 = pedir_nombre_equipo(2)

    global equipo1, equipo2
    equipo1 = Equipo(nombre1)
    equipo2 = Equipo(nombre2)

    total_partidos = 0
    while True:
        entrada = input("¿Cuántos partidos deben jugar los equipos? (Número entero positivo): ")
        if entrada.isdigit():
            total_partidos = int(entrada)
            if total_partidos > 0:
                break
        print("Entrada inválida. Por favor ingrese un número entero positivo.")

    for _ in range(total_partidos):
        JugarPartido()

    ResultadoTorneo()
print(" ")
if __name__ == "__main__":
    main()


