# Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is 
# to figure out information about the number of cubes.
# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, 
# show them to you, and then put them back in the bag. He'll do this a few times per game.
# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue 
# cubes. What is the sum of the IDs of those games?

def recorrer_subsets(subsets):
    for subset in subsets:
        # Separar por color
        colores=subset.split(",")
        # Recorrer cada color para comprobar si supera o no el límite
        erroneo=recorrer_colores(colores)
        if erroneo:
            return True
    return False

def recorrer_colores(colores):
    for col in colores:
        col=(col.strip()).split(" ")
        color=col[1]
        valor=col[0]
        limite=0
        match color:
            case "red": limite=12
            case "blue": limite=14
            case "green": limite=13
        
        if int(valor)>limite:
            return True
    return False
            
suma_ids=0
archivo=open("./Day2/input.txt", "r")
for linea in archivo:
    linea=linea.split(":")
    # Separar id
    id=linea[0].split(" ")[1]
    # Separar por subsets
    subsets=linea[1].split(";")
    # Recorrer los subsets para evaluar juegos correctos e incorrectos
    erroneo=recorrer_subsets(subsets)
    if not erroneo:
        suma_ids+=int(id)
archivo.close()

print("La suma de los ids de los juegos correctos es: "+str(suma_ids))