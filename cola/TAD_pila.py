class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        return self.elementos.pop()

    def isEmpty(self):
        return self.elementos == []

if __name__ == '__main__':
    s = Pila()
    s.push(1)
    s.push("hola")
    s.push(3)
    s.push("🐥")
    s.push([])
    while not s.isEmpty():
        print(s.pop(), end=' ')
    print()

