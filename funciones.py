from grafo import Grafo
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
        for x in grafo.adyacentes(w):
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

#Para componentes no conexas usar un for y esto adentro.
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
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados[w] = True
                dist[w] = dist[v] + 1
                padre[w] = v
                cola.append(w)
    return (padre,dist)

#Esto se tiene que hacer muchas veces, y de ahi sacar los vertices por los cuales se paso
def RandomWalks(grafo, n):
    x = 0;
    cola = deque([])
    veces = {}
    while(x != n):
        v = grafo.obtener_vertice_aleatorio()
        cola.append(v)
        while(len(cola) != 0 or x != n):
            for w in grafo.adyacentes_random(v): ##Tiene que ser uno random
                cola.append(w)
                veces[w] += 1;
                x +=1
    ordenar(veces)
    return veces

def laber_propagation(grafo, n):
    label = {}
    i = 1
    comunidades = 0
    for v in grafo.ver_vertices(): 
        label[v] = i
        i += 1
    while comunidades < n:
        for w in grafo.ver_vertices():
            label[w] = max(label[grafo.adyacentes(w)])


def bfs_rango(grafo, vertice, n):
    if(n == 0):
        return [vertice]
    dist = {}
    lista = []
    cola = deque([])
    dist[vertice] = 0
    cola.append(vertice)
    while len(cola) > 0:
        w = cola.popleft()
        for x in grafo.adyacentes(w):
            if x not in dist:
                dist[x] = dist[w] +1
                if(dist[x] == n):
                    lista.append(x)
                if(dist[x] > n):
                    return lista
    return lista

def ciclo(grafo, vertice, n):
    visitados = {}
    padres = {}
    ciclo = []
    saltos = 0
    cola = deque([])
    visitados [vertice] = True
    padres[v] = None
    cola.append(vertice)
    while( len(cola) > 0 and saltos < n):
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                cola.append(w)
                visitados [w] = True
                padres[w] = v 
                saltos += 1
            if w == vertice and saltos == n:
                while padres [w] != None:
                    ciclo.insert(0,padres[w])
                    w = padres[w]
                    if padres[w] == None:
                        ciclo.append(vertice)
    if len(ciclo) == 0:
        return None
    return ciclo

def tarjan(grafo):
    S = []
    P = []
    orden = {}
    visitados = set()
    cfc = []
    en = set()
    for v in grafo.ver_vertices():
        if v not in visitados:
            orden[v] = 0
            dfs_cfc(grafo, v, visitados, orden, P, S, cfc, en)
    
    return cfc

def dfs_cfc(grafo, v, visitados, orden, p, s, cfcs, en_cfs):
    visitados.add(v)
    s.append(v)
    p.append(v)
    for w in grafo.adyacentes(v):
		if w not in visitados:
			orden[w] = orden[v] + 1
			dfs_cfc(grafo, w, visitados, orden, p, s, cfcs, en_cfs)
		elif w not in en_cfs:
			while orden[p[-1]] > orden[w]:
				p.pop()

    if p[-1] == v:
		p.pop()
		z = None
		nueva_cfc = []
		while z != v:
			z = s.pop()
			en_cfs.append(z)
			nueva_cfc.append(z)
		cfcs.append(nueva_cfc)