import random
class Grafo(object):

    def __init__(self):
        self.vertices = {}
        self.cant = 0

    def ver_vertices(self):
        return self.vertices.keys()
    
    def cantidad(self):
        return self.cant
    
    def add(self, nombre):
        self.vertices[nombre] = set()
        self.cant += 1

    def add_edge(self, v, u):
        if(u not in self.vertices):
            self.add(u)
        if(v not in self.vertices):
            self.add(v)
        self.vertices[v].add(u)

    def adyacentes(self, v):
        if self.cant == 0:
            return None
        if v not in self.vertices:
            return None
        return self.vertices[v]
    
    def adyacente_aleatorio(self, v):
        if self.cant == 0:
            return None
        if v not in self.vertices:
            return None
        if len(self.vertices[v]) == 0:
            return None
        return random.choice(tuple(self.vertices[v]))
    
    def v_aleatorio(self):
        if self.cant == 0:
            return None
        return random.choice(tuple(self.vertices.keys()))