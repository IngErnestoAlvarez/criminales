import funciones
import sys
from grafo import Grafo
import csv

comandos = {
    "min_seguimientos":min_seguimientos,
    "mas_imp":mas_imp,
    "persecucion":persecucion,
    "comunidades":comunidades,
    "divulgar":divulgar,
    "divulgar_ciclo":divulgar_ciclo,
    "cfc":cfc
}
def validar_parametros(*args):
    if len(sys.args) != 2:
        print("La cantidad de parametros es invalido") 
        return False
    return True

def cargar_grafo(archivo):
    lineas = csv.reader(archivo, delimiter='\t')
    grafo = Grafo()
    for linea in lineas:
        grafo.add_edge(linea[0], linea[1])
    return grafo
    
def min_seguimientos(grafo, origen, destino):
    lista = funciones.camino_minimo(grafo, origen, destino)
    if lista == None:
        print("Seguimiento imposible")
        return
    for i in lista[:-1]:
        print(i + " " + "->" + " ",end='')
    print(lista[-1])

def mas_imp(grafo, cant):
    pass

def persecucion(grafo, delicuentes, k):
    pass

def comunidades(grafo, n):
    pass

def divulgar(grafo, delincuente, n):
    pass

def divulgar_ciclo(grafo, delincuente, n):
    lista = ciclo(grafo,delincuente,n)
    if lista == None:
        print("No se encontro recorrido")
        return
    for i in lista[-1]:
        print(i + " " + "->" + " ",end='')
    print(lista[-1])
    return


def cfc(grafo):
    pass

def main(*args):
    if (!validar_parametros(args)):
        return False
    archivo = open(sys.args[1],"r")
    if archivo == -1:
        return -1
    grafo = cargar_grafo(archivo)
    archivo.close()
    comando = input()
    comandos = comando.split(sep=' ')
    return 0