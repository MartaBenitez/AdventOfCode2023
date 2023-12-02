# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 
# one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
# Equipped with this new information, you now need to find the real first and last digit on each line.

def reemplazar_numeros(linea):
    diccionario_numeros={"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    for num in diccionario_numeros:
        # busca todas las ocurrencias del número en la cadena
        posiciones = [i for i in range(len(linea)) if linea.startswith(num, i)]
        a_restar=0
        for pos in posiciones:
            # posicion final
            pos_f=len(num)+(pos-1)-a_restar
            # posicion inicial
            pos_i=(pos+1)-a_restar
            # reemplaza el texto excepto el primer y ultimo caracter para tener el cuenta el solapamiento
            linea = linea[:pos_i] + diccionario_numeros.get(num) + linea[pos_f:]
            # tamaño del numero menos 3 posiciones: una por el numero y dos por el caracter anterior y posterior
            a_restar=len(num)-3
    return linea

sumaCalibraciones=0
archivo=open("./Day1/input.txt", "r")
for linea in archivo:
    linea=reemplazar_numeros(linea)
    listaCaracteres = list(linea)
    terminado=False
    i=0
    valorCalibracion=None
    while terminado==False:
        if listaCaracteres[i].isdigit() and valorCalibracion == None:
            valorCalibracion=listaCaracteres[i]
            listaCaracteres.reverse()
            i=0
        if listaCaracteres[i].isdigit() and valorCalibracion != None:
            valorCalibracion+=listaCaracteres[i]
            terminado=True
        i += 1
    sumaCalibraciones+=int(valorCalibracion)
archivo.close()
    
print("El resultado de la suma es: "+str(sumaCalibraciones))

