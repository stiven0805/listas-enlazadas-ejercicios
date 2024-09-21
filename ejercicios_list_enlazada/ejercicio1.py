"""Diseñe e implemente un sistema para el control de un sistema de un parque Zoologico 

Crear una clase animal con los métodos y atributos básicos. en uno de los atributos, debes indicar la edad y el tipo de animal (Águila, pantera, vaca, ...)
Crear una lista enlazada que permita agregar animales al listado, donde al momento de agregar un nuevo animal a la lista, esta no debe repetirse
Para mostrar los animales que contiene la lista enlazada, debes realizarla usando dos métodos
Una función recursiva
Un bucle"""



class Animal:
    def __init__(self, especie:str, edad:int)->str|int:
        self.especie = especie
        self.edad = edad

    def __str__(self):
        return f"El animal es un {self.especie} y tiene {self.edad} años de edad"
class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, animal:str):
        if not self.existe(animal):
            nuevo_nodo = Nodo(animal)
            if self.cabeza is None:
                self.cabeza = nuevo_nodo

            else:
                actual =self.cabeza
                while actual.siguiente is not None:
                    actual = actual.siguiente
                actual.siguiente = nuevo_nodo
               
    def existe(self, animal:str):
        actual =self.cabeza
        while actual is not None:
            if actual.animal.especie == animal.especie:
                return True
            actual = actual.siguiente
        return False

    def imprimir(self):
        actual =self.cabeza
        while actual is not None:
            print(actual.animal)
            actual = actual.siguiente
        
            
gorilla = Animal("gorilla", 5)
caballo = Animal("caballo", 8)
tigre = Animal("tigre", 7)
leon = Animal("León", 10)


zoo=ListaEnlazada()

zoo.agregar(gorilla)
zoo.agregar(caballo)
zoo.agregar(tigre)
zoo.agregar(leon)
zoo.agregar(caballo)  

zoo.imprimir()

    