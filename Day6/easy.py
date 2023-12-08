# Holding down the button charges the boat, and releasing the button allows the boat to move. Boats move faster if their button 
# was held longer, but time spent holding the button counts against the total race time. You can only hold the button at the start
# of the race, and boats don't move until the button is released.
# Your toy boat has a starting speed of zero millimeters per millisecond. For each whole millisecond you spend at the beginning of 
# the race holding down the button, the boat's speed increases by one millimeter per millisecond.
# Determine the number of ways you can beat the record in each race. What do you get if you multiply these numbers together?

# Se lee el archivo
archivo=open("./Day6/input.txt", "r")
lineas=archivo.readlines()
archivo.close()

# Se sacan en dos arrays los tiempos y las distancias
tiempos = lineas[0].rstrip()
distancias = lineas[1].rstrip()
lista_tiempos=tiempos.split(":")[1].split(" ")
lista_distancias=distancias.split(":")[1].split(" ")
lista_t_fil=[elemento_lista for elemento_lista in lista_tiempos if elemento_lista != ""]
lista_d_fil=[elemento_lista for elemento_lista in lista_distancias if elemento_lista != ""]

# Variable para multiplicar las carreras validas
x_carreras_validas=1

# Se recorre la lista de tiempos
for tiempo in lista_t_fil:
    distancia=int(lista_d_fil[lista_t_fil.index(tiempo)])
    # Se inicializan las carreras válidas
    carreras_validas=0
    # Para cada tiempo de 0 a el tiempo de cada carreras
    for espera in range(int(tiempo)):
        # Se calcula la velocidad, el tiempo de la carrera quitando la espera y la distancia recorrida y se contabiliza si es válida
        velocidad=espera
        tiempo_carrera=int(tiempo)-espera
        dist_recorrida=velocidad*tiempo_carrera
        if dist_recorrida>distancia:
            carreras_validas+=1
    if carreras_validas>0:
        x_carreras_validas*=carreras_validas

# Si no hubiera carreras válidas cambiamos este valor a 0
if x_carreras_validas==1:
    x_carreras_validas=0
    
print("La multiplicación del número de formas total con el que ganar las carreras es: "+str(x_carreras_validas))      