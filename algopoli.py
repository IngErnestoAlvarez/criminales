#!/usr/bin/python3
import funciones
import sys
from grafo import Grafo
import csv


def validar_parametros(*args):
    if len(sys.argv) != 2:
        print("La cantidad de parametros es invalido") 
        return False
    return True

def cargar_grafo(archivo):
    lineas = csv.reader(archivo, delimiter='\t')
    grafo = Grafo()
    for salida, llegada in lineas:
        grafo.add_edge(salida, llegada)
    return grafo
    
def minseguimientos(grafo, origen, destino):
    lista = funciones.camino_minimo(grafo, origen, destino)
    if lista == None:
        print("Seguimiento imposible")
        return
    for i in lista[:-1]:
        print(i + " " + "->" + " ",end='')
    print(lista[-1])

def mas_imp(grafo, cant):
    cant = int(cant)
    importantes = funciones.beetweeness(grafo, cant)
    for i in importantes[:-1]:
        print(i + ',' + " ", end='')
    print(importantes[-1])


def persecucion(grafo, delincuentes, k):
    k = int(k)
    lista_del = delincuentes.split(',')
    camino = funciones.camino_varios_v(grafo, lista_del, k)
    for i in camino[:-1]:
        print(i + " " + "->" + " ",end='')
    print(camino[-1])


def comunidades(grafo, n):
    n = int(n)
    comunidades = funciones.label_propagation(grafo)
    for i, comunidad in enumerate(comunidades, start=1):
        if len(comunidades[comunidad]) >= n:
            print("Comunidad " + str(i) + ': ', end='')
            for vertice in comunidades[comunidad][:-1]:
                print(vertice + ", ", end='')
            print(comunidades[comunidad][-1])
    

def divulgar(grafo, delincuente, n):
    n = int(n)
    vertices = funciones.bfs_rango(grafo, delincuente, n)
    for v in vertices[:-1]:
        print(v + ", ", end='')
    print(vertices[-1])

def divulgar_ciclo(grafo, delincuente, n):
    n = int(n)
    lista = funciones.ciclo(grafo,delincuente,n)
    if len(lista) == 0:
        print("No se encontro recorrido")
        return
    for i in lista[:-1]:
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
        if comando_s == "cfc":
            if len(args) > 0:
                print ("cantidad de parametros invalida")
                continue
            COMANDOS[comando_s](grafo)
        elif comando_s == "comunidades" or comando_s == "mas_imp":
            if len(args) != 1:
                print ("cantidad de parametros invalida")
                continue
            COMANDOS[comando_s](grafo, args[0])
        else:
            if len(args) != 2:
                print ("cantidad de parametros invalida")
                continue
            COMANDOS[comando_s](grafo, args[0], args[1])
        break


COMANDOS = {
    "min_seguimientos":minseguimientos,
    "mas_imp":mas_imp,
    "persecucion":persecucion,
    "comunidades":comunidades,
    "divulgar":divulgar,
    "divulgar_ciclo":divulgar_ciclo,
    "cfc":cfc
}

def main():
    with open(sys.argv[1],"r") as archivo:
        if (not validar_parametros(archivo)):
            return False
        grafo = cargar_grafo(archivo)
        aplicar_comandos(grafo)
    return 0

if __name__ == '__main__':
    main()
    