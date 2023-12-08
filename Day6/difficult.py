# There's really only one race - ignore the spaces between the numbers on each line.
# How many ways can you beat the record in this one much longer race?

# Se lee el archivo
archivo=open("./Day6/input.txt", "r")
lineas=archivo.readlines()
archivo.close()

# Se sacan tiempo y distancia totales
tiempos = lineas[0].rstrip()
distancias = lineas[1].rstrip()
tiempo_t=int(tiempos.split(":")[1].replace(" ",""))
distancia_t=int(distancias.split(":")[1].replace(" ",""))

# Para sumar las carreras válidas
carreras_validas=0

# Para cada tiempo de 0 a el tiempo de la carrera
for espera in range(int(tiempo_t)):
    # Se calcula la velocidad, el tiempo de la carrera quitando la espera y la distancia recorrida y se contabiliza si es válida
    velocidad=espera
    tiempo_carrera=int(tiempo_t)-espera
    dist_recorrida=int(velocidad*tiempo_carrera)
    if dist_recorrida>distancia_t:
        carreras_validas+=1

print("El número de formas con las que se puede ganar la carrera es: "+str(carreras_validas))   