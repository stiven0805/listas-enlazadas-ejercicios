class Tarea:
    def __init__(self, id, tiempo_ejecucion):
        self.id = id
        self.tiempo_ejecucion = tiempo_ejecucion

class Queue:
    def __init__(self):
        self.tareas = []

    def enqueue(self, tarea):
        self.tareas.append(tarea)

    def dequeue(self):
        if not self.is_empty():
            return self.tareas.pop(0)
        return None

    def is_empty(self):
        return len(self.tareas) == 0

    def size(self):
        return len(self.tareas)

class SJF:
    def __init__(self):
        self.ready_queue = Queue()
        self.completed_queue = Queue()

    def agg_tarea(self, tarea):
        self.ready_queue.enqueue(tarea)

    def schedule(self):
        while not self.ready_queue.is_empty():
            tarea = self.ready_queue.dequeue()
            print(f"ejecutando tarea {tarea.id} en un tiempo de {tarea.tiempo_ejecucion}s")
            print(f"Tarea {tarea.id} completada")
            self.completed_queue.enqueue(tarea)

    def print_tareas_completadas(self):
        print("tareas completadas:")
        while not self.completed_queue.is_empty():
            tarea = self.completed_queue.dequeue()
        print(f"tarea {tarea.id} con tiempo de ejecucion de {tarea.tiempo_ejecucion}s")

tarea1 = Tarea(1, 5)
tarea2 = Tarea(2, 3)
tarea3 = Tarea(3, 2)
tarea4 = Tarea(4, 7)

planificador = SJF()


planificador.agg_tarea(tarea1)
planificador.agg_tarea(tarea2)
planificador.agg_tarea(tarea3)
planificador.agg_tarea(tarea4)

planificador.schedule()

planificador.print_tareas_completadas()