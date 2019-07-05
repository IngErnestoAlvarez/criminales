from grafo import Grafo
import heapq
from collections import deque
from math import inf
import heapq
LARGO_RW = 10000
CANTIDAD_RW = 500
VECES_LABEL = 300

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
    return []

def camino(v, padre):
    lista = []
    lista.append(v)
    j = padre[v]
    while j != None:
        lista.insert(0, j)
        j = padre[j]
    return lista

def camino_varios_v(grafo, vertices, k):
    importantes = beetweeness(grafo, k)
    lista_final = camino_minimo(grafo, vertices[0], importantes[0])
    for i in importantes:
        for v in vertices:
            aux = camino_minimo(grafo, v, i)
            if len(lista_final) == 0:
                lista_final = aux
            elif len(aux) < len(lista_final):
                lista_final = aux
    return lista_final
#Esto se tiene que hacer muchas veces, y de ahi sacar los vertices por los cuales se paso
def randomWalk(grafo, v, largo, apariciones):
    if largo == LARGO_RW:
        return
    largo += 1
    apariciones[v] += 1
    w = grafo.adyacente_aleatorio(v)
    if not w:
        return
    randomWalk(grafo, grafo.adyacente_aleatorio(v), largo, apariciones)

def beetweeness(grafo, cant):
    apariciones = {}
    for v in grafo.ver_vertices():
        apariciones[v] = 0
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

#Para componentes no conexas usar un for y esto adentro.
def bfs(grafo,vertice_origen, visitados):
    cola = deque([])
    lista = []
    visitados.add(vertice_origen)
    lista.append(vertice_origen)
    cola.append(vertice_origen)
    while(len(cola) != 0):
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w) 
                lista.append(w)
                cola.append(w)
    return lista

def max_freq(actual, lista):
    freq = {}
    for n in lista:
        if n not in freq:
            freq[n] = 1
        else: 
            freq[n] += 1
    maximo = 0
    numero_comunidad = actual
    for l in freq:
        if freq[l] > maximo:
            maximo = freq[l]
            numero_comunidad = l
    return numero_comunidad

def cargar_label(grafo, entrada, label):
    for i, v in enumerate(grafo.ver_vertices()):
        label[v] = i
        for w in grafo.adyacentes(v):
            if w not in entrada:
                entrada[w] = set(v)
            else:
                entrada[w].add(v)


def propagation(grafo, entrada, label):
    for i in range(VECES_LABEL):
        v_rand = grafo.v_aleatorio()
        visitados = set()
        orden = bfs(grafo, v_rand, visitados)
        for v in grafo:
            orden = orden + bfs(grafo, v, visitados)
        for w in orden:
            lista = []
            for l in entrada[w]:
                lista.append(label[l])
            label[w] = max_freq(label[w], lista)

def label_propagation(grafo):
    entrada = {}
    label = {}
    cargar_label(grafo, entrada, label)
    propagation(grafo, entrada, label)

    comunidades = {}
    for vertice, comunidad in label:
        if(comunidad not in comunidades):
            comunidades[comunidad] = []
        comunidades[comunidad].append(vertice)

    return comunidades




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
                if(dist[x] > n):
                    return lista
                dist[x] = dist[w] +1
                lista.append(x)
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
        aux=padres[aux]
    final.append(vertice)
    final.insert(0,vertice)
    return final

def dfs(grafo, v, vertice_final, visitados, saltos, padres, n):
    if(saltos == n):
        if vertice_final == v:
            return True
        return False
    if vertice_final == v and saltos > 0:
        return False
    for w in grafo.adyacentes(v):
        if w not in visitados:
            padres[w] = v
            visitados.add(w)
            if dfs(grafo, w, vertice_final, visitados, saltos + 1, padres, n):
                return True
            else:
                visitados.remove(w)
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
            en_cfs.add(z)
            nueva_cfc.append(z)
        cfcs.append(nueva_cfc)