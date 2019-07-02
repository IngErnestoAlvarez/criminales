class Vertice(object):

    def __init__(self, nombre):
        self.nombre = nombre
        self.llegada = set()
        self.salida = set()

    def obtener_nombre(self):
        return self.nombre
    
    def add_llegada(self, vertice):
        self.llegada.add(vertice)

    def add_salida(self, vertice):
        self.salida.add(vertice)
    
    def adyacentes(self):
        return self.salida

    def llegadas(self):
        return self.llegada

class Grafo(object):

    def __init__(self):
        self.vertices = set()
        self.cantidad = 0

    def obtener_vertices(self):
        return self.vertices
    
    def cantidad(self):
        return self.cantidad
    
    def dad(self, nombre):
        v = Vertice(nombre)
        self.vertices.add(v)
        self.cantidad += 1
        return True

    def add_edge(self, v, u):
        if(v not in self.vertices or u not in self.vertices):
            return False
        v.add_salida(u)
        u.add_llegada(v)
        return True

    def remove_edge(self, v, u):
        if(v not in self.vertices or u not in self.vertices):
            return False
        if(v not in u.llegada or u not in v.salida):
            return False
        v.salida.remove(u)
        u.llegada.remove(v)
        return True

    def remove_vertice(self, v):
        if(v not in self.vertices): 
            return False
        for x in v.llegada:
            x.salida.remove(v)
        for y in v.salida:
            y.llegada.remove(v)
        self.vertices.discard(v)
        self.cantidad -= 1
        return True