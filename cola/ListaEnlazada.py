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
    print(cabeza, end=', ')

def eliminaSegundo(lista):
    if lista == None: return
    primero = lista
    segundo = lista.siguiente
    # Haz que el primer Nodo apunte al tercero
    primero.siguiente = segundo.siguiente
    # separar el segundo nodo del resto de la lista
    segundo.siguiente = None
    return segundo

def imprimeAlRevesBonito(lista):
    print("[", end='')
    if lista != None:
        cabeza = lista
        cola = lista.siguiente
        imprimeAlReves(cola)
        print(cabeza, end='')
    print(']')

if __name__ == '__main__':
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    imprimeLista(nodo1)
    imprimeAlRevesBonito(nodo1)
