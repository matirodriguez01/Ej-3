import csv

from camion import Camion

class Manejadorcamiones:

    def __init__(self):
        self.__listacamiones = []

    def crearlista(self):
        archivo = open('Camion.csv')
        reader = csv.reader(archivo, delimiter=',')
        i = 0
        for fila in reader:
            self.__listacamiones.append(Camion(fila[0], fila[1], fila[2], fila[3], fila[4]))
            i += 1
        archivo.close()

    def getcamion(self, iid):
        return self.__listacamiones[iid]

    def getlista(self):
        return self.__listacamiones