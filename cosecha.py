import csv

class Cosechas:

    def __init__(self):
        self.__listacosechas = []

    def inicializarlista(self):
        for i in range(20):
            self.__listacosechas.append([])
            for j in range(45):
                self.__listacosechas[i].append(int(0))

    def sumar(self, idd, dia, kg):
        self.__listacosechas[idd][dia] += kg

    def calcular(self, tara, peso):
        return int(peso) - int(tara)

    def archivocosechas(self, lista):
        archivo = open('Cosechas.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            idd = int(fila[0])-1
            dia = int(fila[1])-1
            peso = int(fila[2])
            tara = lista[idd].gettara()
            kg = self.calcular(tara, peso)
            self.sumar(idd, dia, kg)
        archivo.close()


    def getcosecha(self, idd, dia):
        return self.__listacosechas[idd][dia]

    def getlista(self):
        return self.__listacosechas



