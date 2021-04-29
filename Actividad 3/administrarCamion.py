from camion import Camion
class AministrarC:
    lista = []
    archivo = open("camion.txt",'r')
    for x in archivo.readlines():
        camion = x.split(',')
        lista.append(Camion(camion[0],camion[1],camion[2],camion[3],camion[4]))

    @classmethod
    def getLista(cls):
        return AministrarC.lista

    @classmethod
    def getCamion(cls,id):
        return AministrarC.lista[id-1]

    @classmethod
    def getConductor(cls,id):
        return AministrarC.lista[id-1].getNombreCond


    @classmethod
    def getPatente(cls,id):
       return AministrarC.lista[id-1].getPatente()

    @classmethod
    def getMarca(cls, id):
        return AministrarC.lista[id - 1].getMarca()

    @classmethod
    def getTara(cls, id):
        return AministrarC.lista[id - 1].getTara()














        pass

