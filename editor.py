
# Jeremy Arévalo
# PROBLEMA 2: EDITOR DE TEXTO BASICO
# Implementacion mediante listas enlazadas simples

# Clase que representa cada linea del documento
class NodoLinea:
    def __init__(self, texto):
        self.texto = texto
        self.siguiente = None


# Clase principal del editor de texto
class EditorTexto:
    def __init__(self):
        self.cabeza = None
        self.cantidad = 0

    # Insertar una linea en cualquier posicion
    def insertar(self, posicion, texto):
        if posicion < 1 or posicion > self.cantidad + 1:
            print("Posicion no valida.")
            return

        nuevo = NodoLinea(texto)

        if posicion == 1:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza

            for i in range(posicion - 2):
                actual = actual.siguiente

            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

        self.cantidad += 1
        print("Linea insertada correctamente.")

    # Mostrar todas las lineas
    def mostrar(self):
        actual = self.cabeza
        numero = 1

        print("\n--- CONTENIDO DEL DOCUMENTO ---")

        if actual is None:
            print("Documento vacio.")
            return

        while actual is not None:
            print(str(numero) + ". " + actual.texto)
            actual = actual.siguiente
            numero += 1

    # Eliminar una linea especifica
    def eliminar(self, posicion):
        if posicion < 1 or posicion > self.cantidad:
            print("Posicion no valida.")
            return

        if posicion == 1:
            self.cabeza = self.cabeza.siguiente
        else:
            actual = self.cabeza

            for i in range(posicion - 2):
                actual = actual.siguiente

            actual.siguiente = actual.siguiente.siguiente

        self.cantidad -= 1
        print("Linea eliminada correctamente.")

    # Mover una linea a otra posicion
    def mover(self, origen, destino):
        if (origen < 1 or origen > self.cantidad or
                destino < 1 or destino > self.cantidad):
            print("Posiciones no validas.")
            return

        if origen == destino:
            print("La linea ya esta en esa posicion.")
            return

        actual = self.cabeza
        anterior = None

        # Buscar la linea que se desea mover
        for i in range(origen - 1):
            anterior = actual
            actual = actual.siguiente

        # Desconectar la linea de su posicion actual
        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

        texto = actual.texto

        # Insertar la linea en la nueva posicion
        nuevo = NodoLinea(texto)

        if destino == 1:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza

            for i in range(destino - 2):
                actual = actual.siguiente

            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

        print("Linea movida correctamente.")

    # Buscar texto en todas las lineas
    def buscar(self, texto):
        actual = self.cabeza
        posicion = 1
        encontrados = 0

        print("\n--- RESULTADOS DE BUSQUEDA ---")

        while actual is not None:
            if texto.lower() in actual.texto.lower():
                print("Encontrado en la linea", posicion, ":", actual.texto)
                encontrados += 1

            actual = actual.siguiente
            posicion += 1

        if encontrados == 0:
            print("No se encontro el texto.")

    # Reemplazar texto en una linea especifica
    def reemplazar(self, posicion, texto_anterior, texto_nuevo):
        if posicion < 1 or posicion > self.cantidad:
            print("Posicion no valida.")
            return

        actual = self.cabeza

        for i in range(posicion - 1):
            actual = actual.siguiente

        if texto_anterior not in actual.texto:
            print("El texto no existe en esa linea.")
            return

        actual.texto = actual.texto.replace(texto_anterior, texto_nuevo)
        print("Texto reemplazado correctamente.")

    # Guardar el documento en un archivo
    def guardar(self, archivo):
        with open(archivo, "w", encoding="utf-8") as documento:
            actual = self.cabeza

            while actual is not None:
                documento.write(actual.texto + "\n")
                actual = actual.siguiente

        print("Documento guardado correctamente.")

    # Cargar el documento desde un archivo
    def cargar(self, archivo):
        self.cabeza = None
        self.cantidad = 0

        with open(archivo, "r", encoding="utf-8") as documento:
            for linea in documento:
                self.insertar(self.cantidad + 1, linea.rstrip("\n"))

        print("Documento cargado correctamente.")


# DEMOSTRACION DEL EDITOR DE TEXTO
editor = EditorTexto()

# Insertar lineas
print("1. INSERTAR LINEAS")
editor.insertar(1, "Introduccion al documento")
editor.insertar(2, "Este es un editor de texto")
editor.insertar(3, "Programacion en Python")
editor.insertar(2, "Uso de listas enlazadas")
editor.mostrar()

# Buscar texto
print("\n2. BUSCAR TEXTO")
editor.buscar("Python")

# Reemplazar texto
print("\n3. REEMPLAZAR TEXTO")
editor.reemplazar(3, "editor", "programa")
editor.mostrar()

# Mover una linea
print("\n4. MOVER LINEA")
editor.mover(4, 1)
editor.mostrar()

# Eliminar una linea
print("\n5. ELIMINAR LINEA")
editor.eliminar(2)
editor.mostrar()

# Guardar documento
print("\n6. GUARDAR DOCUMENTO")
editor.guardar("documento.txt")

# Cargar documento
print("\n7. CARGAR DOCUMENTO")
nuevo_editor = EditorTexto()
nuevo_editor.cargar("documento.txt")
nuevo_editor.mostrar()
