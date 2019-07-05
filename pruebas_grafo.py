#!/usr/bin/python
from grafo import Grafo

def grafo_vacio():
    print("PRUEBAS GRAFO VACIO\n")
    grafo = Grafo()
    print("Vertices: " + str(grafo.ver_vertices()))
    print("Cantidad:",  grafo.cantidad())

def pruebas_adyacentes():
    print("\n\nPRUEBAS GRAFO ADYACENTES\n")
    grafo = Grafo()
    grafo.add("Lucia")
    grafo.add_edge("Ernesto", "Alejo")
    grafo.add_edge ("Alejo", "Martin")
    grafo.add_edge("Martin", "Ernesto")
    vertices = grafo.ver_vertices()
    print("Vertices:", vertices)
    for i in vertices:
        print(i + " ", end='')
    print("Cantidad: " + str(grafo.cantidad()))
    print("Adyacentes de Ernesto: " + str(grafo.adyacentes("Ernesto")))
    print("Adyacentes de Alejo: " + str(grafo.adyacentes("Alejo")))
    print("Adyacentes de Martin: " + str(grafo.adyacentes("Martin")))
    grafo.add_edge("Ernesto", "Martin")
    grafo.add_edge("Ernesto", "Lucia")
    print(grafo.adyacente_aleatorio("Ernesto"))
    print(grafo.v_aleatorio())

    
def main(*args, **kwarks):
    grafo_vacio()
    pruebas_adyacentes()
    return 0

if __name__ == '__main__':
    main()