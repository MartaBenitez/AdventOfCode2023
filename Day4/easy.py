# The Elf leads you over to the pile of colorful cards. There, you discover dozens of scratchcards, all with their opaque 
# covering already scratched off. Picking one up, it looks like each card has two lists of numbers separated by a vertical bar 
# (|): a list of winning numbers and then a list of numbers you have. You organize the information into a table (your puzzle input).
# As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appear in the list 
# of winning numbers. The first match makes the card worth one point and each match after the first doubles the point value of 
# that card.
# How many points are they worth in total?

sum_premio=0
archivo=open("./Day4/input.txt", "r")
for linea in archivo:
    # Separar nombre carta
    lista_carta=linea.split(":")
    # Separar ganadores y juego
    cartas=lista_carta[1].split("|")
    ganadores=[elemento_lista for elemento_lista in cartas[0].split(" ") if elemento_lista != ""]
    juego=[elemento_lista for elemento_lista in cartas[1].split(" ") if elemento_lista != ""]
    # Número de números ganadores en la carta
    num_ganadores=0
    # Recorrer los números del juego
    for numero in juego:
        num_limpio=(numero.replace('\n','')).strip()
        if num_limpio in ganadores:
            num_ganadores+=1
    # Si hay al emnos un número ganador por carta se suma al premio
    if num_ganadores!=0:
        sum_premio+=pow(2, (num_ganadores-1))  
archivo.close()

print("La suma de las cartas ganadoras es: "+str(sum_premio))
