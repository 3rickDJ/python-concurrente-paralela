class Nodo:
    def __init__(self, carga=None, siguiente=None):
        self.carga = carga
        self.siguiente = siguiente

    def __str__(self):
        return str(self.carga)

    def imprimeAlReves(self):
        if self.siguiente != None:
            cola = self.siguiente
            cola.imprimeAlReves()
        print(self.carga, end=' ')

