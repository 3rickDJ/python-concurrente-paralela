class Cola:
    def __init__(self):
        self.longitud = 0
        cabeza = None

    def estaVacia(self):
        return self.longitud == 0

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)
