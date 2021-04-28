from cosecha import Cosechas

from manejadorcamion import Manejadorcamiones


def cero():
    print('Hasta luego')
    input('Presione cualquier tecla para continuar...')


def uno():
    print('\n-OPCIÓN 1-\n')
    idd = int(input('Ingrese ID del camión buscado: '))
    if idd < 20 or idd < 0:
        sumador = 0
        for i in range(len(lista[idd])):
            sumador += i
        print('Cantidad de kilos descargados: ', sumador)
    else:
        print('El ID ingresado es inválido')
    input('\nPresione cualquier tecla para continuar...')


def dos():
    print('-OPCIÓN 2-')
    dia = int(input('Ingrese el día que desea buscar (1 a 45): '))
    print('\n\nPatente       Conductor    Cantidad de Kg')
    for i in range(len(mancamion.getlista())):
        print('%7s    %9s    %6d' % (mancamion.getcamion(i).getpatente(),
                                     mancamion.getcamion(i).getnombre(),
                                     int(cosecha.getcosecha(i, dia-1)) - int(mancamion.getcamion(i).gettara())))

    input('\nPresione cualquier tecla para continuar...')


switcher = {
    0: cero,
    1: uno,
    2: dos
}


def switch(opc):
    func = switcher.get(opc, lambda: print('\nOpción incorrecta'))
    func()


if __name__ == '__main__':
    cosecha = Cosechas()
    mancamion = Manejadorcamiones()
    mancamion.crearlista()
    lista = mancamion.getlista()
    cosecha.inicializarlista()
    cosecha.archivocosechas(lista)

    band = False
    while not band:
        print('-----MENU-----')
        print('1- Buscar camión por ID y mostrar kilos descargados')
        print('2- Buscar información de un día')
        print('0- Salir')
        op = int(input('\nIngrese una opción: '))
        switch(op)
        band = int(op) == 0
