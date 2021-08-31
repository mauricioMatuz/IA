#importo las bibliotecas necesarias
# from random import random
# from PySide2.QtWidgets import QWidget
# from View.Main import Ui_MainFrom
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import math


import random
import math 
import matplotlib.pyplot as plt
import numpy as np

tamañoPoblacion = 0
maximoPoblacion = 0
minimo = 0
maximo = 0
generaciones = 0
allFitness = []

listaSeleccion = []
listaCruza  = []
listaMutacion = []
listaFitness = []

contador_gens = 0
contadorControl = 0
mejores_gen = []
peores_gen = []
mejoresFit = []
promedio_gen = []
# class Genetic(QWidget, Ui_MainFrom):
    
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.pushButtonEnviar.clicked.connect(self.GenerarGrafico)
# x*((np.cos(y)))
        
def CalcularFitness(x,y):
    fitness = y*((np.cos(x))**2*(np.sin(y)))+x*(((np.cos(y))**2)*(np.sin(x)))
    allFitness.append(fitness)
    return fitness
    
def GenerarIndividuo(tamaño_poblacion, cadena_bits):
    individuo = ''
    listIndividuos = []
    for i in range(tamaño_poblacion):
        individuo = '' 
        for j in range(cadena_bits):
            individuo += str(random.randint(0,1))
        listIndividuos.append(individuo)
    return listIndividuos


    
def DeltaX(maximo,minimo,error):
    rangoX = abs(maximo - minimo)
    error = error*2
    rangoX = (rangoX / error)+1
    binario = DecimalBinario(rangoX) 
    tamanio = len(str(binario))
    decimalito = (2**tamanio)-1
    deltaX = rangoX / decimalito

    return deltaX
    
def DeltaY(parametroY2,parametroY1,error):
    rangoY = (parametroY2 - parametroY1)
    error = error*2
    rangoY = (rangoY / error)+1
    binario = DecimalBinario(rangoY)
    tamanio = len(str(binario))
    decimalito = (2**tamanio)-1
    deltaY = rangoY / decimalito
    
    return deltaY
      
def DecimalBinario(datos):
    binario = ""
    bin = ""
    decimal =datos
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
        datos = int(binario)
    
    return datos

def BinarioDecimal(datos):
    suma = 0
    i = 0
    datos = int(datos)
    while(datos >= 1):
        d = datos %10
        datos = datos//10
        suma = suma + d*pow(2,i)
        i = i+1
    return suma

def GenerarPoblacion(tamaño_poblacion, cadena_bits):
    global contadorControl
    poblacionInicial = GenerarIndividuo(tamaño_poblacion, cadena_bits)
    
    for i in range(tamaño_poblacion):
        tablaSeleccion =  { 'Indice' : i, 'Poblacion Inicial': poblacionInicial[i], 'Valor de x': 0, 'Valor de y':0,'Fitness': 0, 'Prob i': 0, 'Prob acumulada': 0, 'Conteo esperado': 0, 'Conteo actual': 0 },
        tablaCruza = {'Indice' : i, 'Mating pool': poblacionInicial[i], 'Punto de cruza' : 0, 'Despues de cruza': 0, 'Valor' : 0, 'Fitness' : 0},
        tablaMutacion ={'Indice' : i, 'Cruzado': 0,  'Mutado': 0, 'Valor de X' : 0,'Valor de Y' : 0, 'Fitness' : 0},
        tablaFitness = { 'Padre':0, 'Fitness padre':0, 'Hijo':0, 'Fitness hijo':0, 'Mejor fitness':0, 'Cadena de bits':0 },
        
        listaSeleccion.extend(tablaSeleccion)
        listaCruza.extend(tablaCruza)
        listaMutacion.extend(tablaMutacion)
        listaFitness.extend(tablaFitness)
        contadorControl +=1
  
    # seleccion(tamañoPoblacion, cadena_bits, minimo, maximo)


def seleccion(tamañoPoblacion, cadenaBits, minimo, maximo,error):
    global listaSeleccion
    global listaCruza
    global listaCruza
    
    sumaFitness = 0
    promedioFitness = 0
    peorFitness = 0
    minimoFitness = 0
    probAcumulada = 0
    
    for i in range(len(listaSeleccion)):
        cadena = listaSeleccion[i].get('Poblacion Inicial')
        individuoDecimal = BinarioDecimal(cadena)
        deltaX = DeltaX(maximo,minimo,error)
        valorX = individuoDecimal+(i*deltaX)
        listaSeleccion[i].update({'Valor de x':valorX})
        deltaY = DeltaY(maximo,minimo,error)
        valorY = individuoDecimal+(i*deltaY)
        listaSeleccion[i].update({'Valor de y':valorY})
        fitness = CalcularFitness(valorX,valorY)
        listaSeleccion[i].update({'Fitness':fitness})
        sumaFitness += fitness
    promedioFitness = sumaFitness / len(listaSeleccion)
    
    for i in range(len(listaSeleccion)):
        if(i == 0):
            peor_fitness = listaSeleccion[0].get('Fitness')
            valor_equis = listaSeleccion[0].get('Valor de x')
            valor_ye = listaSeleccion[0].get('Valor de y')
            minimo_fitness = listaSeleccion[0].get('Fitness')
        else:
            if(peor_fitness < listaSeleccion[i].get('Fitness')):
                peor_fitness = listaSeleccion[i].get('Fitness')
                valor_equis = listaSeleccion[i].get('Valor de x')
                valor_ye = listaSeleccion[i].get('Valor de y')
            if(minimo_fitness > listaSeleccion[i].get('Fitness')):
                minimo_fitness = listaSeleccion[i].get('Fitness')
       
        prob = listaSeleccion[i].get('Fitness') / sumaFitness
        expCount = listaSeleccion[i].get('Fitness')/ promedioFitness
    
        listaSeleccion[i].update({'Prb i':prob})
        listaSeleccion[i].update({'Conteo esperado': expCount})
        probAcumulada += listaSeleccion[i].get('Prob i')
    
        listaSeleccion[i].update({'Prob acumulada': probAcumulada})
    
    mejores = {'Generacion': contador_gens, 'Mejor':peor_fitness, 'Peor': minimo_fitness, 'Promedio': promedioFitness},
    mejoresFit.extend(mejores)
    print("GENERARCION: ",contador_gens," FENOTIPO: ",valor_equis," FENOTIPO Y: ",valor_ye, "MEJOR: ",peorFitness,"MINIMO ",minimo_fitness,"SUM FIT: ",sumaFitness," PROMEDIO: ", promedioFitness)
    print("--------------------------------\n------------------")
    equis=0
    for i in range(len(listaSeleccion)):
        if(listaSeleccion[i].get('Conteo actual') != 0):
            for j in range(listaSeleccion[i].get('Conteo actual')):
                listaCruza[equis].update({'Mating pool':listaSeleccion[i].get('Poblacion Inicial')})
                listaFitness[equis].update({'Padre': listaSeleccion[i].get('Poblacion Inicial'), 'Fitness padre': listaSeleccion[i].get('Fitness')})
                equis+=1
                #print(equis)
    print(" --------------------------------------------------------- ")

    
    
def Cruza():
    cadena1=''
    cadena2=''
    auxcadena1=''
    auxcadena2=''
    aux_pares=[]
    aux_impares=[]
    dats=[]
    for b in range(0, len(listaCruza), 2):
        tamanio=len(listaCruza[b].get('Mating pool'))
        tamanio2=len(listaCruza[b+1].get('Mating pool'))
        corte=random.randint(1,cadena_bits)
        cadena1=listaCruza[b].get('Mating pool')[0:corte]
        cadena2=listaCruza[b+1].get('Mating pool')[0:corte]
        auxcadena1=listaCruza[b].get('Mating pool')[corte:tamanio]
        auxcadena2=listaCruza[b+1].get('Mating pool')[corte:tamanio2]
        cadena1 = cadena1 + auxcadena2
        cadena2 = cadena2 + auxcadena1

        listaCruza[b].update({'Despues de cruza': cadena1, 'Punto de cruza': corte})
        listaCruza[b+1].update({'Despues de cruza': cadena2, 'Punto de cruza': corte})
        listaMutacion[b].update({'Cruzado': cadena1})
        listaMutacion[b+1].update({'Cruzado': cadena2})
        
    for i in range(len(listaCruza)):
        cadenita = listaCruza[i].get('Despues de cruza')
        valorDecimal = BinarioDecimal(cadenita)
        listaCruza[i].update({'Valor': valorDecimal})
        deltaX = DeltaX(maximo,minimo,error)
        valorX = valorDecimal+(i*deltaX)
        deltaY = DeltaY(maximo,minimo,error)
        valorY = valorDecimal+(i*deltaY)
        fitness = CalcularFitness(valorX,valorY)
        listaCruza[i].update({'Fitness':fitness})
        
    

        
        
def Mutuacion(maximo,minimo,generacion,error):
    auxMutados = []
    original = ''
    mutado = ''
    for x in range(0,len(listaMutacion),2):
        original = ''
        mutado = ''
        mut = bool(random.getrandbits(1))
        mut2 = bool(random.getrandbits(1))
        original = listaMutacion[x].get('Cruzado')
        if mut:
            for i in original:
                if bool(random.getrandbits(1)):
                    if i == '1':
                        mutado += '0'
                    else:
                        mutado += '1'
                else:
                    mutado+=i
            listaMutacion[x].update({'Mutado':mutado})
        else:
            listaMutacion[x].update({'Mutado':original})
        
        mutado = ''
        original = listaMutacion[x+1].get('Cruzado')
        if mut2:
            for j in original:
                if bool(random.getrandbits(1)):
                    if j == '1':
                        mutado += '0'
                    else:
                        mutado += '1'
                else:
                    mutado+=j
            listaMutacion[x+1].update({'Mutado':mutado})
        else:
            listaMutacion[x+1].update({'Mutado':original})
    
    for x in range(len(listaMutacion)):
        cadena = listaMutacion[x].get('Mutado')
        individuoDecimal = BinarioDecimal(cadena)
        deltaX = DeltaX(maximo,minimo,error)
        valorX = individuoDecimal+(x*deltaX)
        deltaY = DeltaY(maximo,minimo,error)
        valorY = individuoDecimal+(x*deltaY)
        listaMutacion[x].update({'Valor de X':valorX})
        listaMutacion[x].update({'Valor de Y':valorY})
        fitness = CalcularFitness(valorX,valorY)
        listaMutacion[x].update({'Fitness':fitness})
        listaFitness[x].update({'Hijo':cadena,'Fitness hijo':fitness})
        if listaFitness[x].get('Fitness hijo') > listaFitness[x].get('Fitness padre'):
            listaFitness[x].update({'Mejor fitness': listaFitness[x].get('Fitness hijo'), 'Cadena de bits': listaFitness[x].get('Hijo')})
        else:
            listaFitness[x].update({'Mejor fitness': listaFitness[x].get('Fitness padre'), 'Cadena de bits': listaFitness[x].get('Padre')})
    
    auxMutados = listaMutacion
    auxMutados = sorted(auxMutados, key=lambda x: x['Fitness'], reverse=True)
    ActualizarDatos(auxMutados,generacion)
    
def ActualizarDatos(auxMutados,generaciones):
    global contadorControl
    for x in range(2):
        if contadorControl < maximoPoblacion:
            contadorControl+=1
            tablaSeleccion = { 'Indice' : contadorControl-1, 'Poblacion Inicial': auxMutados[x].get('Mutado'), 'Valor de x': 0, 'Valor de y': 0, 'Fitness': 0, 'Prob i': 0, 'Prob acumulada': 0, 'Conteo esperado': 0, 'Conteo actual': 0 },
            tablaCruza = {'Indice' : contadorControl-1, 'Mating pool': auxMutados[x].get('Mutado'), 'Punto de cruza' : 0, 'Despues de cruza': 0, 'Valor' : 0, 'Fitness' : 0,},
            tablaMutacion = {'Indice' : contadorControl-1, 'Cruzado': 0,  'Mutado': 0, 'Valor de X' : 0, 'Fitness' : 0},
            tablaFitness = { 'Padre':0, 'Fitness padre':0, 'Hijo':0, 'Fitness hijo':0, 'Mejor fitness':0, 'Cadena de bits':0 }

            listaSeleccion.extend(tablaSeleccion)
            listaCruza.extend(tablaCruza)
            listaMutacion.extend(tablaMutacion)
            listaFitness.append(tablaFitness)
        else:
            ControlPoblacion(contadorControl)

def ControlPoblacion(contadorControl):
  
    for x in range(contadorControl):
        if(listaFitness[x].get('Fitness hijo') >  listaFitness[x].get('Fitness padre')):
            listaSeleccion[x].update({'Poblacion Inicial':listaFitness[x].get('Hijo') })
        else:
            listaSeleccion[x].update({'Poblacion Inicial':listaFitness[x].get('Padre') })
        listaSeleccion[x].update({'Valor de x':0, 'Fitness': 0, 'Prob i': 0, 'Prob acumulada': 0, 'Conteo esperado': 0, 'Conteo actual': 0})

def Empezar(tamañoPoblacion, poblacionMax,generaciones, cadenaBits, minimo, maximo,error):
    
    global contador_gens
    global maximoPoblacion
    maximoPoblacion = poblacionMax
    GenerarPoblacion(tamañoPoblacion,cadenaBits)
    for i in range(generaciones):
        contador_gens+=1
        print("generacion no. ",contador_gens,"\n")
        seleccion(tamañoPoblacion, cadenaBits, minimo, maximo,error)
        Cruza()
        Mutuacion(maximo,minimo,generaciones,error)
        
def Clasificar(generaciones):
    for i in range(generaciones):
        mejores_gen.append(mejoresFit[i].get('Mejor'))
        peores_gen.append(mejoresFit[i].get('Peor'))
        promedio_gen.append(mejoresFit[i].get('Promedio'))
                
def GenerarGrafica(x,y,z):
    plt.plot(x, label = "Mejor Caso")   # Dibuja el gráfico
    plt.xlabel("Generaciones")   # Inserta el título del eje X
    plt.ylabel("Evolucion del Fitness")   # Inserta el título del eje Y
    plt.ioff()   # Desactiva modo interactivo de dibujo
    plt.ion()   # Activa modo interactivo de dibujo
    plt.plot(y, label = "Peor Caso")   # Dibuja datos de lista2 sin borrar datos de lista1
    plt.ioff()   # Desactiva modo interactivo
    plt.ion()   # Activa modo interactivo de dibujo
    plt.plot(z, label = "Caso promedio")   # Dibuja datos de lista2 sin borrar datos de lista1
    plt.ioff()   # Desactiva modo interactivo
    # plt.plot(lista3)   # No dibuja datos de lista3
    plt.legend()
    plt.show()   # Fuerza dibujo de datos de lista3
    
    
def verListaGen():
    for i in range(len(listaSeleccion)):
        print(listaSeleccion[i])
        
def verListCruza():
    for i in range(len(listaCruza)):
        print(listaCruza[i])
    
def verListMutacion():
    for i in range(len(listaMutacion)):
        print(listaMutacion[i])
        
def verListaMejores():
    for i in range(len(mejoresFit)):
        print(mejoresFit[i])
        
def verListaFitness():
    for i in range(len(listaFitness)):
        print(listaFitness[i])

if __name__ == "__main__":
    minimo = float (input("Valor minimo de x: "))
    maximo = float (input("Valor maximo de x: "))
    error = float (input ("Valor de error: "))
    tamaño_poblacion = int (input("Tamaño de la poblacion: "))
    maximo_poblacion = int (input("Tamaño maximo de la poblacion: "))
    generaciones = int (input("Numero de generaciones: "))
    cadena_bits = int (input("Tamaño de la cadena de bits: "))
    

    Empezar( tamaño_poblacion, maximo_poblacion, generaciones, cadena_bits,minimo, maximo,error)
    verListaMejores()
    Clasificar(generaciones)
    GenerarGrafica(mejores_gen, peores_gen, promedio_gen)


'''
formula a usar delta = (b-a)/n luego P(i) = a+i*delta
donde P(i) es el valor que va a tomar X y Y
'''