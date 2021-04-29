
class Camion:
    __id = 0
    __nombreCond = ""
    __patente = 0
    __marca = 0
    __tara = 0

    def __init__(self,id,patente,nombreCond,marca,tara):
        self.__id = id
        self.__nombreCond = nombreCond
        self.__patente = patente
        self.__marca = marca
        self.__tara = tara

    def getId(self):
        return int(self.__id)

    def getNombreCond(self):
        return self.__nombreCond

    def getPatente(self):
        return self.__patente

    def getMarca(self):
        return self.__marca

    def getTara(self):
        return int(self.__tara)
