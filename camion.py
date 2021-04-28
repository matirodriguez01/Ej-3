class Camion:
    __id = 0
    __nombre = ''
    __patente = ''
    __marca = ''
    __tara = 0

    def __init__(self, idd, nom, pat, mar, tar):
        self.__id = idd
        self.__nombre = nom
        self.__patente = pat
        self.__marca = mar
        self.__tara = tar

    def getid(self):
        return self.__id

    def gettara(self):
        return self.__tara

    def getnombre(self):
        return self.__nombre

    def getpatente(self):
        return self.__patente

    def getmarca(self):
        return self.__marca

