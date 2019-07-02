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
    print("Seguimiento imposible.")
    return None

def camino(v, padre):
    lista = []
    lista.append(v)
    j = padre[v]
    while j != None:
        lista.insert(0, j)
        j = padre[j]
    return lista
    #No habria que imprimir el resultado?

#para componentes no conexas usar un for y esto adentro.
def bfs(grafo,vertice_origen,visitados = None):
    visitados = {}
    padre = {}
    dist = {}
    cola = deque([])
    cola.append(vertice_origen)
    visitados[vertice_origen] = True
    dist[vertice_origen] = 0
    padre[vertice_origen] = None
    while(len(cola) != 0):
        v = cola.popleft()
        for w in v.adyacentes()
            if w not in visitados:
                visitados[w] = True
                dist[w] = dist[v] + 1
                padre[w] = v
                cola.append(w)
    return (padre,dist)
#Esto se tiene que hacer muchas veces, y de ahi sacar los vertices por los cuales se paso
#odio python y mi vida.
def RandomWalks(grafo, n):
    x = 0;
    cola = deque([])
    veces = {}
    while(x != n)
        v = grafo.obtener_vertice_aleatorio()
        cola.append(v)
        while(len(cola) != 0 or x != n)
              for w in v.adyacentes(): ##Tiene que ser uno random
                cola.append(w)
                veces[w] += 1;
                x +=1
    ordenar(veces)
    return veces


##Este es exacto, necesitamos el aproximado (random walks) xq' para grafos grandes
##este tarda mucho
def PageRank_o_BTC(cant):
    cent = {}
    distancias = {}
    for v in grafo: cent[v] = 0
    for v in grafo:
        padre,distancias = bfs(grafo,v)
        distancias.add(distancia[v])
        cent_aux = {}
        for w in grafo: cent_aux[w] = 0
        vertices_ordenados = ordenar_vertices(grafo,distancias)
        for w in vertices_ordenados:
            cent_aux[w] = cent_aux[w] + cent_aux[w] + 1 #cent_aux[padre[w]] += 1 + cent_aux[w]
        for w in grafo:
            if w == v continue
            cent[w] += cent_aux[w]
    return cent

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

