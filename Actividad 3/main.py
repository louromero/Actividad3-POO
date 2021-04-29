from cosecha import Cosecha
from camion import  Camion
from administrarCamion import AministrarC

if __name__ == '__main__':

    cosecha = Cosecha()

    print("<<< MENU DE OPCIONES >>>")

    while True:

        print("\n1- Dado el número de identificador de un camión mostrar, la cantidad total de kilos descargados.")
        print("2- Mostrar listado del dia.")
        print("0- para terminar")

        op = int(input(":"))

        if(op == 0):
            break

        if op == 1:
            op = int(input("identificador: "))
            print("La cantidad de kilos descargados es: {}".format(cosecha.getKilos(op)))

        if op == 2:
            dia = int(input("Ingrese dia: "))
            cosecha.listarPorDia(dia,)


