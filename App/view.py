"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Cargar información de buses de singapur")
    print("2- Consultar cantidad de taxis")
    print("3- Consultar compañias con al menos un taxi")
    print("4- Consultar el orden (mayor a menor) de la cantidad de taxis en las compañias")
    print("5- Consultar el numero de compañias que más servicios prestaron")
    print("0- Salir")
    print("*******************************************")

def optionOne():
    print("\n Cargando información de los taxis ")
    tipo_archivo = input(str("Ingrese qué archivo quiere cargar (small,medium o large)"))
    cont = controller.loadTaxi(tipo_archivo)
    print("Los archivos han sido cargados correctamente")
    return cont 

def optionTwo():
    print("El numero total de taxis es: "+str(controller.cantidad_taxis(cont)))



"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        cont = optionOne()
    elif int(inputs[0]) == 2:
        optionTwo()
    elif int(inputs[0]) == 3:
        controller.companias_taxis(cont)
    elif int(inputs[0]) == 4:
        cantidad_companias = input(str("Ingrese el numero de compañias que desea ver: "))
        controller.orden_companias(cont,cantidad_companias)
    elif int(inputs[0]) == 5:
        cantidad_companias = input(str("Ingrese el numero de compañias que desea ver: "))
        controller.orden_companias_servicio(cont,cantidad_companias)
    else:
        sys.exit(0)
sys.exit(0)

    


    
