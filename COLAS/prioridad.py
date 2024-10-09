class Tarea:
    def __init__(self, id, tiempo_ejecucion, prioridad):
        self.id = id
        self.tiempo_ejecucion = tiempo_ejecucion
        self.prioridad = prioridad

class Colas:
    def __init__(self):
        self.tareas = []

    def enqueue(self, tarea):
        self.tareas.append(tarea)
        self.tareas.sort(key=lambda x: x.prioridad, reverse=True)

    def dequeue(self):
        if not self.is_empty():
            return self.tareas.pop(0)
        return None

    def is_empty(self):
        return len(self.tareas) == 0

    def size(self):
        return len(self.tareas)

class Prioridades:
    def __init__(self):
        self.ready_queue = Colas()
        self.completed_queue = Colas()

    def agg_tarea(self, tarea):
        self.ready_queue.enqueue(tarea)

    def schedule(self):
        while not self.ready_queue.is_empty():
            tarea = self.ready_queue.dequeue()
            print(f"ejecutando tarea {tarea.id} en un tiempo de {tarea.tiempo_ejecucion} y de prioridad {tarea.prioridad}")
            print(f"Tarea {tarea.id} completada")
            self.completed_queue.enqueue(tarea)

    def print_tareas_completadas(self):
        print("tareas completadas:")
        while not self.completed_queue.is_empty():
            tarea = self.completed_queue.dequeue()
            print(f"Tarea {tarea.id} ejecutada en {tarea.tiempo_ejecucion}s, y de prioridad {tarea.prioridad}")

tarea1 = Tarea(1, 5, 4)
tarea2 = Tarea(2, 3, 2)
tarea3 = Tarea(3, 2, 1)
tarea4 = Tarea(4, 7, 5)

planificador = Prioridades()

planificador.agg_tarea(tarea1)
planificador.agg_tarea(tarea2)
planificador.agg_tarea(tarea3)
planificador.agg_tarea(tarea4)

planificador.schedule()

planificador.print_tareas_completadas()