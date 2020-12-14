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

import config as cf
from DISClib.ADT import list as lt
from App import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def compareTaxisIds (taxiA, taxiB):
    if int(taxiA['taxi_id']) == int(taxiB['taxi_id']):
        return 0
    elif int(taxiA['taxi_id']) > int(taxiB['taxi_id']):
        return 1
    return -1

def loadCSVfile(file,cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst

def loadTaxi(tipo_archivo):
    if tipo_archivo == "small":
        lst = loadCSVfile("Docs\taxi-trips-wrvz-psew-subset-small.csv",compareTaxisIds)
        return lst     
    elif tipo_archivo == "medium":
        lst = loadCSVfile("Docs\taxi-trips-wrvz-psew-subset-medium.csv",compareTaxisIds)
        return lst 
    elif tipo_archivo == "large":
        lst = loadCSVfile("Docs\taxi-trips-wrvz-psew-subset-large.csv",compareTaxisIds)
        return lst 

    
# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def cantidad_taxis(lst):
    retorno = model.cantidad_de_taxis(lst)
    return retorno 
def companias_taxis(lst):
    retorno = model.companias_con_un_taxi(lst)
    return retorno 
def orden_companias(lst,cantidad_companias):
    retorno = model.orden_companias(lst,cantidad_companias)
    return retorno 
def orden_companias_servicio(lst,cantidad_companias):
    retorno = model.orden_companias_servicio(lst,cantidad_companias)
    return retorno 

