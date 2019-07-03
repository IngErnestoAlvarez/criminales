class Grafo(object):

    def __init__(self):
        self.vertices = {}
        self.cantidad = 0

    def ver_vertices(self):
        return self.vertices.keys()
    
    def cantidad(self):
        return self.cantidad
    
    def add(self, nombre):
        self.vertices[nombre] = set()
        self.cantidad += 1

    def add_edge(self, v, u):
        if(v not in self.vertices):
            self.add(v)
        if(u not in self.vertices):
            self.add(u)
        self.vertices[v].add(u)

    def adyacentes(self, v):
        return self.vertices[v]