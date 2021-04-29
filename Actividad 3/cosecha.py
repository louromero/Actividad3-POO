from administrarCamion import AministrarC

class Cosecha:
    __lista = []
    def __init__(self):
        for i in range(20):
            self.__lista.append([])
            for _ in range(45):
                self.__lista[i].append(0)
        self.cargar()


    def cargar(self):
        archivo = open("ingreso.txt")
        Tcargas = archivo.readlines()
        cargas = []
        for x in Tcargas:
            cargas.append(x.split(','))
        for x in cargas:
            id = int(x[0])-1
            dias = int(x[1])-1
            total = int(x[2]) - AministrarC().getTara(id)
            self.__lista[id][dias] += total
        archivo.close()

    def listarPorDia(self,dia):
        print("\tPatente\tConductor\t\t\tCantidad de kilos")
        for x in AministrarC.getLista():
            if(self.__lista[x.getId()-1][dia-1] > 0):
                print("\t{}\t{}\t\t\t{}".format(x.getPatente(),x.getNombreCond(),self.__lista[x.getId()-1][dia-1]))

    def getKilos(self,id):
        acum = 0
        for x in self.__lista[id-1]:
            acum += x
        return  acum




