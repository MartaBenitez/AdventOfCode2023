# The newly-improved calibration document consists of lines of text; each line originally contained a specific 
# calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the 
# first digit and the last digit (in that order) to form a single two-digit number.
# Consider your entire calibration document. What is the sum of all of the calibration values?

sumaCalibraciones=0
archivo=open("./Day1/input.txt", "r")
for linea in archivo:
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
    
    
        
            
            
            


