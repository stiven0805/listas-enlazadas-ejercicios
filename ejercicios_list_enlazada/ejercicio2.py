""" Diseña e implementa un sistema de gestión de tareas utilizando listas enlazadas. Cada tarea tendrá las siguientes propiedades:

Descripción: Una breve descripción de la tarea.
Prioridad: Un valor numérico que indica la prioridad de la tarea (por ejemplo, 1 para alta prioridad, 3 para baja prioridad).
Fecha de Vencimiento: La fecha límite para completar la tarea.
El sistema debe permitir realizar las siguientes operaciones:

Agregar una tarea: El usuario puede ingresar los detalles de una nueva tarea y añadirla a la lista.
Eliminar una tarea: El usuario puede eliminar una tarea de la lista, ya sea por su descripción o por su posición en la lista.
Mostrar todas las tareas: El sistema muestra todas las tareas en la lista, ordenadas por prioridad (de mayor a menor) y, en caso de empate, por fecha de vencimiento (de más próxima a más lejana).
Buscar una tarea: El usuario puede buscar una tarea por su descripción y el sistema muestra los detalles de la tarea si la encuentra.
Marcar una tarea como completada: El usuario puede marcar una tarea como completada, y esta se elimina de la lista."""


class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.siguiente = None
        self.completada = False

class ListaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, tarea):
        if self.cabeza is None:
            self.cabeza = tarea
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = tarea

    def eliminar_tarea(self, descripcion):
        if self.cabeza is None:
            return

        if self.cabeza.descripcion == descripcion:
            self.cabeza = self.cabeza.siguiente
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.descripcion == descripcion:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

    def mostrar_tareas(self):
        if self.cabeza is None:
            print("no hay tareas en la lista.")
            return

        tareas = []
        actual = self.cabeza
        while actual is not None:
            if not actual.completada:
                tareas.append(actual)
            actual = actual.siguiente

        tareas.sort(key=lambda x: (-x.prioridad, x.fecha_vencimiento))

        for tarea in tareas:
            print(f"Descripción: {tarea.descripcion}")
            print(f"Prioridad: {tarea.prioridad}")
            print(f"Fecha de Vencimiento: {tarea.fecha_vencimiento}")
            print("-" * 50)

    def buscar_tarea(self, descripcion):
        actual = self.cabeza
        while actual is not None:
            if actual.descripcion == descripcion:
                print(f"descripción: {actual.descripcion}")
                print(f"prioridad: {actual.prioridad}")
                print(f"fecha de vencimiento: {actual.fecha_vencimiento}")
                return
            actual = actual.siguiente
        print("tarea no encontrada")

    def marcar_completada(self, descripcion):
        actual = self.cabeza
        while actual is not None:
            if actual.descripcion == descripcion:
                actual.completada = True
                print("esta tarea ya fue cumplida")
                return
            actual = actual.siguiente
        print("tarea no encontrada.")

lista_tareas = ListaTareas()

lista_tareas.agregar_tarea(Tarea("hacer calculos", 2, "2024-08-10"))
lista_tareas.agregar_tarea(Tarea("Pagar facturas", 1, "2024-07-05"))
lista_tareas.agregar_tarea(Tarea("hacer informe", 3, "2024-09-15"))

lista_tareas.mostrar_tareas()

lista_tareas.buscar_tarea("Pagar facturas")

lista_tareas.marcar_completada("Pagar facturas")

lista_tareas.mostrar_tareas()
