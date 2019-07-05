import funciones
import sys
from grafo import Grafo
import csv

COMANDOS = {
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
    for salida, llegada in lineas:
        grafo.add_edge(salida, llegada)
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
    importantes = funciones.beetweeness(grafo, cant)
    for i in importantes[:-1]:
        print(i + ',' + " ", end='')
    print(importantes[-1])


def persecucion(grafo, delincuentes, k):
    lista_del = delincuentes.split(',')
    camino = funciones.camino_varios_v(grafo, lista_del, k)
    for i in camino[-1]:
        print(i + " " + "->" + " ",end='')
    print(camino[-1])


def comunidades(grafo, n):
    comunidades = funciones.label_propagation(grafo, n)
    i = 1
    for comunidad in comunidades:
        if len(comunidades[comunidad]) >= n:
            print("Comunidad " + i + ': ', end='')
            for vertice in comunidades[comunidad][:-1]:
                print(vertice + ", ", end='')
            print(comunidades[comunidad][-1])
            i += 1
    

def divulgar(grafo, delincuente, n):
    vertices = funciones.bfs_rango(grafo, delincuente, n)
    for v in vertices[:-1]:
        print(v + ", ", end='')
    print(vertices[-1])

def divulgar_ciclo(grafo, delincuente, n):
    lista = funciones.ciclo(grafo,delincuente,n)
    if lista == None:
        print("No se encontro recorrido")
        return
    for i in lista[-1]:
        print(i + " " + "->" + " ",end='')
    print(lista[-1])
    return


def cfc(grafo):
    arreglo_cfc = funciones.tarjan(grafo)
    contador = 1
    for cfc in arreglo_cfc:
        print("CFC " + str(contador) + ':', end=' ')
        for v in cfc[:-1]:
            print(v + ",", end=' ')
        print(cfc[-1])
        contador += 1

def aplicar_comandos(grafo):
    while True:
        comando = input()
        comando_s, *args = comando.split(sep=' ')
        if comando_s not in COMANDOS:
            print("Comando equivocado")
            return
        if len(args) == 0:
            COMANDOS[comando_s](grafo)
        elif len(args) == 1:
            COMANDOS[comando_s](grafo, args[0])
        elif len(args) == 2:
            COMANDOS[comando_s](grafo, args[0], args[1])
        else:
            print("Cantidad de paramentros invalida")

def main(*args):
    with open(sys.args[1],"r") as archivo:
        if (not validar_parametros(args, archivo)):
            return False
        grafo = cargar_grafo(archivo)
        aplicar_comandos(grafo)
    return 0