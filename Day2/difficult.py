# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

def recorrer_subsets(subsets):
    dicc_minimos={"red":0,"blue":0,"green":0}
    for subset in subsets:
        # Separar por color
        colores=subset.split(",")
        # Recorrer cada color y enviar el número de cubos del subset
        dicc_cubos=recorrer_colores(colores)
        # Recorrer cada color y guardar el número de cubos nuevo si es mayor o igual que el guardado
        for color in dicc_cubos:
            if int(dicc_cubos.get(color))>=int(dicc_minimos.get(color)):
                dicc_minimos={**dicc_minimos, color:dicc_cubos.get(color)}
    return dicc_minimos

def recorrer_colores(colores):
    dicc_cubos={}
    for col in colores:
        col=(col.strip()).split(" ")
        color=col[1]
        valor=col[0]
        # Añadir el valor al diccionario
        dicc_cubos={**dicc_cubos, color: valor}
    return dicc_cubos

suma_power=0
archivo=open("./Day2/input.txt", "r")
for linea in archivo:
    linea=linea.split(":")
    # Separar id
    id=linea[0].split(" ")[1]
    # Separar por subsets
    subsets=linea[1].split(";")
    # Recorrer los subsets
    dicc_minimos=recorrer_subsets(subsets)
    power=1
    # Calcular el poder multiplicando cada color y luego sumar el de cada juego
    for color in dicc_minimos:
        power=power*int(dicc_minimos.get(color))
    suma_power+=power
archivo.close()

print("El poder total del juego es: "+str(suma_power))