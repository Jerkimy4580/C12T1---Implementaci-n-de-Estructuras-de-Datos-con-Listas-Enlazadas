
# Jeremy Arévalo
# TEMA 6: LISTAS ENLAZADAS, PILAS Y COLAS
# PROBLEMA 1: SISTEMA DE GESTIÓN DE PROCESOS

# Clase que representa cada proceso (nodo).
class NodoProceso:
    def __init__(self, id, nombre, estado, creacion, cpu):
        self.id = id
        self.nombre = nombre
        self.estado = estado
        self.creacion = creacion
        self.cpu = cpu
        self.siguiente = None


# Clase que administra la lista enlazada.
class ListaProcesos:
    def __init__(self):
        self.cabeza = None

    # Agregar un proceso al final.
    def agregar(self, id, nombre, estado, creacion, cpu):
        nuevo = NodoProceso(id, nombre, estado, creacion, cpu)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

    # Cambiar el estado de un proceso.
    def cambiar_estado(self, id, estado):
        actual = self.cabeza

        while actual is not None:
            if actual.id == id:
                actual.estado = estado
                return True

            actual = actual.siguiente

        return False

    # Eliminar todos los procesos terminados.
    def eliminar_terminados(self):
        while self.cabeza is not None and self.cabeza.estado == "terminado":
            self.cabeza = self.cabeza.siguiente

        actual = self.cabeza

        while actual is not None and actual.siguiente is not None:
            if actual.siguiente.estado == "terminado":
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente

    # Mover un proceso al principio de la lista.
    def mover_al_inicio(self, id):
        if self.cabeza is None:
            return False

        if self.cabeza.id == id:
            return True

        anterior = self.cabeza
        actual = self.cabeza.siguiente

        while actual is not None:
            if actual.id == id:
                anterior.siguiente = actual.siguiente
                actual.siguiente = self.cabeza
                self.cabeza = actual
                return True

            anterior = actual
            actual = actual.siguiente

        return False

    # Mostrar todos los procesos.
    def mostrar(self):
        actual = self.cabeza

        print("\n--- LISTA DE PROCESOS ---")

        while actual is not None:
            print("ID:", actual.id,
                  "| Nombre:", actual.nombre,
                  "| Estado:", actual.estado,
                  "| Creación:", actual.creacion,
                  "| CPU:", actual.cpu)

            actual = actual.siguiente

    # Calcular el tiempo promedio de espera.
    def promedio_espera(self):
        actual = self.cabeza
        reloj = 0
        total = 0
        cantidad = 0

        # Simulación de planificación FCFS.
        while actual is not None:
            inicio = max(reloj, actual.creacion)
            espera = inicio - actual.creacion

            total += espera
            cantidad += 1
            reloj = inicio + actual.cpu

            actual = actual.siguiente

        if cantidad > 0:
            return total / cantidad

        return 0


# PROGRAMA PRINCIPAL

procesos = ListaProcesos()

print("=== SISTEMA DE GESTIÓN DE PROCESOS ===")

# Registrar 10 procesos.
procesos.agregar("P001", "Navegador", "listo", 0, 5)
procesos.agregar("P002", "Editor", "listo", 1, 3)
procesos.agregar("P003", "Antivirus", "bloqueado", 2, 4)
procesos.agregar("P004", "Explorador", "listo", 3, 2)
procesos.agregar("P005", "Musica", "en ejecución", 4, 6)
procesos.agregar("P006", "Calculadora", "listo", 5, 2)
procesos.agregar("P007", "Actualizacion", "bloqueado", 6, 5)
procesos.agregar("P008", "Terminal", "listo", 7, 3)
procesos.agregar("P009", "Correo", "listo", 8, 4)
procesos.agregar("P010", "Sistema", "listo", 9, 2)

# Mostrar los procesos registrados.
print("\n1. Procesos registrados:")
procesos.mostrar()

# Cambiar el estado de un proceso.
print("\n2. Cambiar estado de P003:")
procesos.cambiar_estado("P003", "listo")
procesos.mostrar()

# Dar prioridad a un proceso.
print("\n3. Mover P008 al principio:")
procesos.mover_al_inicio("P008")
procesos.mostrar()

# Calcular el promedio de espera.
print("\n4. Tiempo promedio de espera:")
print(round(procesos.promedio_espera(), 2), "unidades de tiempo")

# Marcar procesos como terminados.
print("\n5. Eliminar procesos terminados:")
procesos.cambiar_estado("P002", "terminado")
procesos.cambiar_estado("P005", "terminado")
procesos.eliminar_terminados()

# Mostrar la lista final.
print("\n6. Lista final:")
procesos.mostrar()

print("\n=== FIN DEL PROGRAMA ===")
