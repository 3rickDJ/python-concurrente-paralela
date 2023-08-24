class Nodo:
    def __init__(self, carga=None, siguiente=None):
        self.carga = carga
        self.siguiente = siguiente

    def __str__(self):
        return str(self.carga)

if __name__ == '__main__':
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    print(nodo1)
    print(nodo1.siguiente)
    print(nodo1.siguiente.siguiente)
