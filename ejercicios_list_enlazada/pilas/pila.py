class Pila:
    def __init__(self, n=None):
        self.items = []
        self.n = n  

    def esta_vacia(self):
        return len(self.items) == 0

    def esta_llena(self):
        if self.n is None:
            return False  
        return len(self.items) >= self.n

    def push(self, item):
        if self.esta_llena():
            print("La pila está llena")#no puse limite en la pila, entonces nunca va a estar llena 
        else:
            self.items.append(item)

    def pop(self):
        if self.esta_vacia():
            print("La pila está vacía")
            return None
        return self.items.pop()

    def top(self):
        if self.esta_vacia():
            print("La pila está vacía")
            return None
        return self.items[len(self.items) - 1]

def mostrar_menu():
    print("¿Qué quiere hacer?")
    print("1. Push")
    print("2. Pop")
    print("3. Top")
    print("4.isEmpty")
    print("Ingrese cualquier otro número para salir")

def pedir_opcion():
    opcion = int(input("Ingrese la opción: "))
    return opcion

def push(pila):
    elemento = input("Ingrese el elemento a apilar: ")
    pila.push(elemento)

def pop(pila):
    elemento = pila.pop()
    if elemento:
        print("Se ha desapilado:", elemento)

def top(pila):
    top = pila.top()
    if top:
        print("La cima de la pila es:", top)

def verificar_esta_vacia(pila):
    if pila.esta_vacia():
        print("La pila está vacía.")
    else:
        print("La pila no está vacía.")
def creador_pila():
    pila = Pila()
        
    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == 1:
            push(pila)
        elif opcion == 2:
            pop(pila)
        elif opcion == 3:
            top(pila)
        elif opcion == 4:
            verificar_esta_vacia(pila)
        else:
            break

if __name__ == "__main__":
    creador_pila()
