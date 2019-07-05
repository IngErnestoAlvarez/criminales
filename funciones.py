from grafo import Grafo
import heapq
from collections import deque
from math import inf
import heapq
LARGO_RW = 10000
CANTIDAD_RW = 500

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
def bfs(grafo,vertice_origen,visitados = {}):
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

def camino_varios_v(grafo, vertices, k):
    importantes = beetweeness(grafo, k)
    lista_final = camino_minimo(importantes[0], vertices[0])
    for i in importantes:
        for v in vertices:
            aux = camino_minimo(grafo, v, i)
            if len(aux) < len(lista_final):
                lista_final = aux
    return lista_final
#Esto se tiene que hacer muchas veces, y de ahi sacar los vertices por los cuales se paso
def randomWalk(grafo, v, largo, apariciones):
    if largo == LARGO_RW:
        return
    largo += 1
    apariciones[v] += 1
    randomWalk(grafo, grafo.adyacente_aleatorio(v), largo, apariciones)

def beetweeness(grafo, cant):
    apariciones = {}
    for i in range(CANTIDAD_RW):
        randomWalk(grafo, grafo.v_aleatorio(), 0, apariciones)
    maximo = []
    for i in apariciones:
        if len(maximo) < cant:
            heapq.heappush(maximo, (apariciones[i], i))
        else:
            if maximo[0][0] < apariciones[i]:
                heapq.heappop(maximo)
                heapq.heappush(maximo, (apariciones[i], i))
    final = []
    for i in range(cant):
        vertice = heapq.heappop(maximo)
        final.insert(0, vertice[1])
    return final

def label_propagation(grafo, n):
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
    visitados = set()
    padres = {}
    padres [vertice] = None
    if not dfs(grafo, vertice, vertice, visitados, 0, padres, n):
        return []
    aux = padres[vertice]
    final = []
    while(vertice != aux):
        final.insert(0,aux)
        aux=padres[vertice]
    final.append(vertice)
    final.insert(0,vertice)
    return final

def dfs(grafo, v, vertice_final, visitados, saltos, padres, n):
    if(saltos == n):
        if vertice_final == v:
            return True
        return False
    if vertice_final == v:
        return False
    for w in grafo.adyacentes(v):
        if w not in visitados:
            padres[w] = v
            if dfs(grafo, w, vertice_final, visitados + set([w]), saltos + 1, padres, n):
                return True
    return False
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