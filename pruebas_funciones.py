from grafo import Grafo
import funciones


def pruebas_camino_minimo():
    print("PRUEBAS CAMINO MINIMO\n")
    grafo = Grafo()
    grafo.add_edge(1,2)
    grafo.add_edge(2,3)
    grafo.add_edge(3,4)
    
    camino = funciones.camino_minimo(grafo, 1, 4)
    for v in camino[:-1]:
        print(v, "-> ", end='')
    print(camino[-1])
    camino2 = funciones.camino_minimo(grafo, 2, 4)
    for v in camino2[:-1]:
        print(v, "-> ", end='')
    print(camino2[-1])
    grafo.add_edge(2, 4)
    camino = funciones.camino_minimo(grafo, 1, 4)
    for v in camino[:-1]:
        print(v, "-> ", end='')
    print(camino[-1])
    camino2 = funciones.camino_minimo(grafo, 2, 4)
    for v in camino2[:-1]:
        print(v, "-> ", end='')
    print(camino2[-1])

    grafo.add(5)
    camino = funciones.camino_minimo(grafo, 1, 5)
    print(camino)

def pruebas_beetweeness():
    print("\n\nPRUEBA BEETWEENESS\n")
    grafo = Grafo()
    grafo.add_edge(1, "centro")
    grafo.add_edge(2, "centro")
    grafo.add_edge(3, "centro")
    grafo.add_edge(4, "centro")
    grafo.add_edge(5, "centro")
    grafo.add_edge(2, 5)

    importantes = funciones.beetweeness(grafo, 2)

    print(importantes[0])
    print(importantes[1])

def cfc(grafo):
    arreglo_cfc = funciones.tarjan(grafo)
    contador = 1
    for cfc in arreglo_cfc:
        print("CFC " + str(contador) + ':', end=' ')
        for v in cfc[:-1]:
            print(v + ",", end=' ')
        print(cfc[-1])
        contador += 1

def pruebas_tarjan():
    print("\n\nPRUEBAS COMPONENTES CONEXAS\n")
    grafo = Grafo()
    grafo.add_edge('A', 'B')
    grafo.add_edge('B', 'C')
    grafo.add_edge('C', 'A')
    grafo.add_edge('C', 'D')
    grafo.add_edge('B', 'E')
    grafo.add_edge('E', 'D')
    grafo.add_edge('D', 'F')
    grafo.add_edge('F', 'E')
    grafo.add('G')
    #! H e I tienen que ser una sola componente
    grafo.add_edge('H', 'I')
    cfc(grafo)

def persecucion(grafo, delincuentes, k):
    lista_del = delincuentes.split(',')
    camino = funciones.camino_varios_v(grafo, lista_del, k)
    for i in camino[:-1]:
        print(str(i) + " " + "->" + " ",end='')
    print(camino[-1])


def pruebas_camino_varios():
    print("\n\n PRUEBAS CAMINO VARIOS\n")
    grafo = Grafo()
    grafo.add_edge(1, 3)
    grafo.add_edge(1, 2)
    grafo.add_edge(2, 3)
    grafo.add_edge(2, 4)
    grafo.add_edge(4, 5)
    grafo.add_edge(5, 3)
    grafo.add_edge(2, 'y')
    grafo.add_edge(3, 'y')
    grafo.add_edge(4, 'y')
    grafo.add_edge(5, 'y')

    grafo.add_edge('enc1', 1)
    grafo.add_edge('enc2', 'enc1')

    lista = "enc1,enc2"
    persecucion(grafo, lista, 2)

def pruebas_ciclo():
    print("\n\n PRUEBAS CICLO DE LARGO n\n")
    grafo = Grafo()
    grafo.add_edge('A', 'B')
    grafo.add_edge('B', 'C')
    grafo.add_edge('C', 'A')
    grafo.add_edge('C', 'D')
    grafo.add_edge('B', 'E')
    grafo.add_edge('E', 'D')
    grafo.add_edge('D', 'F')
    grafo.add_edge('F', 'E')
    grafo.add('G')
    lista = funciones.ciclo(grafo,'B',3)
    print(lista)

def main():
    pruebas_camino_minimo()
    pruebas_beetweeness()
    pruebas_tarjan()
    pruebas_camino_varios()
    pruebas_ciclo()
    return 0

if __name__ == '__main__':
    main()
    