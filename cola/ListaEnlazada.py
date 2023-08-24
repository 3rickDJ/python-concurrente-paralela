class Nodo:
    def __init__(self, carga=None, siguiente=None):
        self.carga = carga
        self.siguiente = siguiente

    def __str__(self):
        return str(self.carga)

def imprimeLista(nodo):
    print("[", end='')
    while nodo:
        if nodo.siguiente == None:
            print(nodo, end='')
        else:
            print(nodo, end=', ');
        nodo = nodo.siguiente
    print(']')

def imprimeAlReves(lista):
    if lista == None: return
    cabeza = lista
    cola = lista.siguiente
    imprimeAlReves(cola)
    print(cabeza, end=' ')

if __name__ == '__main__':
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    imprimeLista(nodo1)
    imprimeAlReves(nodo1)
