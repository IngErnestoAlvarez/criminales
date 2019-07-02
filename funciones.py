from grafo import Grafo
from grafo import Vertice
from collections import deque
from math import inf
import heapq

def camino_minimo(grafo,u,v):
    padre = {}
    cola = deque([])
    padre[u] = None
    cola.append(u)
    while len(cola) > 0:
        w = cola.popleft()
        for x in w.adyacentes:
            if x not in padre:
                padre[x] = w
                cola.append(x)
            if x == v:
                return camino(v, padre)
    return None

def camino(v, padre):
    lista = []
    lista.append(v)
    j = padre[v]
    while j != None:
        lista.insert(0, j)
        j = padre[j]
    return lista

def PageRank_o_BTC(cant):
    pass


def camino_importante(v_vertices, k):
    pass

def laber_propagation(n):
    pass

def bfs_rango(vertice, n):
    if(n == 0):
        return [vertice]
    dist = {}
    lista = []
    cola = deque([])
    dist[vertice] = 0
    cola.append(vertice)
    while len(cola) > 0:
        w = cola.popleft()
        for x in w.adyacentes:
            if x not in dist:
                dist[x] = dist[w] +1
                if(dist[x] == n):
                    lista.append(x)
                if(dist[x] > n):
                    return lista
    return lista

def ciclo(vertice, n):
    pass

def cfc():
    pass

