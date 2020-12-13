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
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Sorting import shellsort as sh 
from DISClib.Utils import error as error
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

# Funciones para agregar informacion al grafo

# ==============================
# Funciones de consulta
# ==============================
def cantidad_de_taxis(lst):
    total = lt.size(lst)
    return total 
def companias_con_un_taxi(lst):
    dict_companias = {}
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        taxi = it.next(iterator)
        if taxi['company'] not in dict_companias:
            dict_companias[taxi['company']] = 1 
        else: 
            dict_companias[taxi['company']] += 1 
    lst_companies = lt.newList(datastructure='SINGLE_LINKED',cmpfunction=None)
    lt.addFirst(lst_companies,dict_companias.keys())
    companies = lt.size(lst_companies)
    return companies
def orden_companias(lst,cantidad_companias):
    dict_companias = {}
    iterator = it.newIterator(lst)
    lista_resultado = lt.newList('SINGLE_LINKED',None)
    while it.hasNext(iterator):
        taxi = it.next(iterator)
        if taxi['company'] not in dict_companias:
            dict_companias[taxi['company']] = 1 
        else: 
            dict_companias[taxi['company']] += 1 
    lst_companies = lt.newList(datastructure='SINGLE_LINKED',cmpfunction=None)
    lt.addFirst(lst_companies,dict_companias.values())
    sh.shellSort(lst_companies,cmp_values)
    contador = 1
    while contador <= cantidad_companias:
        lt.addFirst(lista_resultado,lt.getElement(lst_companies,contador))
        contador += 1 
    return lista_resultado
def orden_companias_servicio(lst,cantidad_companias):
    respuesta = orden_companias(lst,cantidad_companias)
    return respuesta     
    

    

# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================

def cmp_values(element_1,element_2):
    if element_1 > element_2:
        return True 
    else:
        return False