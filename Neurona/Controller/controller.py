from PySide2.QtWidgets import QWidget,QApplication
from Views.FormData import Ui_Form
from PySide2.QtCore import Qt

from os import name
import numpy as np 
import math
from matplotlib import colors
import matplotlib.pyplot as plt


class Neurona(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.vectorY = []
        self.matriz = []
        self.Grafica1 = []
        self.Grafica2 = []
        self.Grafica3 = []
        self.pushButtonValor.clicked.connect(self.start)
        
       
        
    def ValoresTxT(self):
        file = open("C:/Users/matam/OneDrive/Escritorio/IA/Neurona/doc/matriz.txt")
        vectorY = []
        matriz = []
        #vias se agrega como parte del algoritmo :c
        for linea in file:
            datos = linea.replace("X =","").replace("Y =","").replace("[","").replace("]","")
            vectorAux = datos.split(";")
            for x in range(len(vectorAux)):
                vectorAuxiliar = vectorAux[x].split(",")
                if len(vectorAuxiliar) >2:
                    datosMatriz = [int(vectorAuxiliar[0]),int(vectorAuxiliar[1]),int(vectorAuxiliar[2])]
                    matriz.append(datosMatriz)
                else:
                    vectorY.append(int(vectorAuxiliar[0]))
        self.vectorY = np.array(vectorY)
        self.matriz = np.array(matriz)
        file.close()
    
    def Peso(self):
        tamMatriz = self.matriz
        w = [np.random.uniform(-1,1) for i in range(tamMatriz.shape[1])]
        return w
    
    def U(self,w1):
        X = self.matriz
        w = w1
        u = np.dot(X,w)
        return u
    
    def Ufinal(self,w1):
        X = self.matriz
        w = w1
        u = np.dot(X,w)
        return u
    
    def Yc(self,w1):
        u = self.U(w1)
        yc = []
        for x in range(len(u)):
            if u[x] <= 0:
                yc.append(0)
            elif u[x] > 0:
                yc.append(1)
        return yc
    
    def YcComprobar(self,u1):
        u = u1
        yc = []
        for x in range(len(u)):
            if u[x] <= 0:
                yc.append(0)
            elif u[x] > 0:
                yc.append(1)
        return yc
    
    def E(self,w1):
        yc = self.Yc(w1)
        y = self.vectorY.T
        e = yc - y
        return e
    
    def Norma(self,w1):
        e = self.E(w1)
        norma = np.linalg.norm(e)
        return norma
    
    def NuevoW(self,lamda,epsilon,id):
        ward = []
        w = self.Peso()
        bandera = False
        while(bandera == False):  
            e = self.E(w)
            norma = self.Norma(w)
            X = self.matriz
            lamdas = lamda
            Xe = np.dot(e,X)
            lamdaXe = np.dot(lamdas,Xe)
            w = w - lamdaXe
            ward = w
            if id == 1:
                self.Grafica1.append(norma)
            elif id == 2:
                self.Grafica2.append(norma)
            elif id == 3:
                self.Grafica3.append(norma)
            if norma < epsilon:
                bandera = True
            else:
                bandera = False
            
        
        self.Graficar()
        
        otroU = self.Ufinal(ward)
        ycotro = self.YcComprobar(otroU)
        print(ycotro,'comprobar\n------------------------')
        print('Peso final: ',ward,' \n-------------------------------')
       
    def Graficar(self):
        plt.plot(self.Grafica1,color='blue')
        plt.plot(self.Grafica2,color='red')
        plt.plot(self.Grafica3,color='orange')
        plt.show()
    
            
    def start(self):
        error1 = float(self.lineEditErro1.text())
        error2 = float(self.lineEditErro2.text())
        error3 = float(self.lineEditErro3.text())
        lamda = float(self.lineEditLambda.text())
        modulo = Neurona()
        modulo.ValoresTxT()
        modulo.NuevoW(lamda,error1,1)
        modulo = Neurona()
        modulo.ValoresTxT()
        modulo.NuevoW(lamda,error2,2)
        modulo = Neurona()
        modulo.ValoresTxT()
        modulo.NuevoW(lamda,error3,3)
