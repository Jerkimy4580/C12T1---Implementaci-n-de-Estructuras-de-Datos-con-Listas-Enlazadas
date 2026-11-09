
# Jeremy Arévalo
# PROBLEMA 4: HOJA DE CALCULO DISPERSA
# Implementacion mediante dos listas enlazadas

# Nodo que representa una celda con informacion
class NodoCelda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.derecha = None
        self.abajo = None


# Nodo que representa una fila
class NodoFila:
    def __init__(self, numero):
        self.numero = numero
        self.primera = None
        self.siguiente = None


# Nodo que representa una columna
class NodoColumna:
    def __init__(self, numero):
        self.numero = numero
        self.primera = None
        self.ultima = None
        self.siguiente = None


# Clase principal de la hoja de calculo
class HojaCalculo:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.lista_filas = None
        self.lista_columnas = None
        self.cantidad_celdas = 0

    # Buscar una fila
    def buscar_fila(self, numero):
        actual = self.lista_filas

        while actual is not None:
            if actual.numero == numero:
                return actual
            actual = actual.siguiente

        return None

    # Crear una fila si no existe
    def crear_fila(self, numero):
        nueva = NodoFila(numero)

        if self.lista_filas is None or numero < self.lista_filas.numero:
            nueva.siguiente = self.lista_filas
            self.lista_filas = nueva
            return nueva

        actual = self.lista_filas

        while actual.siguiente is not None and actual.siguiente.numero < numero:
            actual = actual.siguiente

        nueva.siguiente = actual.siguiente
        actual.siguiente = nueva

        return nueva

    # Reconstruir los enlaces de las columnas
    def reconstruir_columnas(self):
        self.lista_columnas = None
        fila = self.lista_filas

        while fila is not None:
            celda = fila.primera

            while celda is not None:
                celda.abajo = None
                celda = celda.derecha

            fila = fila.siguiente

        fila = self.lista_filas

        while fila is not None:
            celda = fila.primera

            while celda is not None:
                actual = self.lista_columnas
                anterior = None

                while actual is not None and actual.numero < celda.columna:
                    anterior = actual
                    actual = actual.siguiente

                if actual is None or actual.numero != celda.columna:
                    nueva = NodoColumna(celda.columna)

                    if anterior is None:
                        nueva.siguiente = self.lista_columnas
                        self.lista_columnas = nueva
                    else:
                        nueva.siguiente = actual
                        anterior.siguiente = nueva

                    actual = nueva

                if actual.primera is None:
                    actual.primera = celda
                else:
                    actual.ultima.abajo = celda

                actual.ultima = celda
                celda = celda.derecha

            fila = fila.siguiente

    # Insertar o actualizar una celda
    def insertar(self, fila, columna, valor):
        if not (1 <= fila <= self.filas and
                1 <= columna <= self.columnas):
            print("Coordenadas no validas.")
            return

        encabezado = self.buscar_fila(fila)

        if encabezado is None:
            encabezado = self.crear_fila(fila)

        actual = encabezado.primera
        anterior = None

        while actual is not None and actual.columna < columna:
            anterior = actual
            actual = actual.derecha

        # Actualizar si la celda ya existe
        if actual is not None and actual.columna == columna:
            if valor == 0:
                self.eliminar(fila, columna)
            else:
                actual.valor = valor
                print("Celda actualizada correctamente.")
            return

        # No almacenar valores vacios
        if valor == 0:
            return

        nueva = NodoCelda(fila, columna, valor)
        nueva.derecha = actual

        if anterior is None:
            encabezado.primera = nueva
        else:
            anterior.derecha = nueva

        self.cantidad_celdas += 1
        self.reconstruir_columnas()
        print("Celda insertada correctamente.")

    # Eliminar una celda
    def eliminar(self, fila, columna):
        encabezado = self.buscar_fila(fila)

        if encabezado is None:
            print("La celda no existe.")
            return

        actual = encabezado.primera
        anterior = None

        while actual is not None and actual.columna < columna:
            anterior = actual
            actual = actual.derecha

        if actual is None or actual.columna != columna:
            print("La celda no existe.")
            return

        if anterior is None:
            encabezado.primera = actual.derecha
        else:
            anterior.derecha = actual.derecha

        self.cantidad_celdas -= 1

        # Eliminar fila si queda vacia
        if encabezado.primera is None:
            self.eliminar_encabezado_fila(fila)

        self.reconstruir_columnas()
        print("Celda eliminada correctamente.")

    # Eliminar el encabezado de una fila vacia
    def eliminar_encabezado_fila(self, numero):
        actual = self.lista_filas
        anterior = None

        while actual is not None and actual.numero != numero:
            anterior = actual
            actual = actual.siguiente

        if actual is not None:
            if anterior is None:
                self.lista_filas = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente

    # Obtener el valor de una celda
    def obtener(self, fila, columna):
        encabezado = self.buscar_fila(fila)

        if encabezado is None:
            return 0

        actual = encabezado.primera

        while actual is not None and actual.columna < columna:
            actual = actual.derecha

        if actual is not None and actual.columna == columna:
            return actual.valor

        return 0

    # Sumar y promediar un rango de celdas
    def calcular_rango(self, fila_inicio, columna_inicio,
                       fila_fin, columna_fin):

        if not (1 <= fila_inicio <= fila_fin <= self.filas and
                1 <= columna_inicio <= columna_fin <= self.columnas):
            print("Rango no valido.")
            return

        suma = 0
        cantidad = 0
        fila = self.lista_filas

        while fila is not None:
            if fila_inicio <= fila.numero <= fila_fin:
                celda = fila.primera

                while celda is not None:
                    if columna_inicio <= celda.columna <= columna_fin:
                        suma += celda.valor
                        cantidad += 1

                    celda = celda.derecha

            fila = fila.siguiente

        promedio = suma / cantidad if cantidad > 0 else 0

        print("Suma del rango:", suma)
        print("Promedio de celdas con datos:", promedio)

    # Insertar una fila completa
    def insertar_fila(self, posicion):
        if posicion < 1 or posicion > self.filas + 1:
            print("Posicion no valida.")
            return

        fila = self.lista_filas

        while fila is not None:
            if fila.numero >= posicion:
                fila.numero += 1
            fila = fila.siguiente

        self.filas += 1
        self.reconstruir_columnas()
        print("Fila insertada correctamente.")

    # Eliminar una fila completa
    def eliminar_fila(self, posicion):
        if posicion < 1 or posicion > self.filas:
            print("Posicion no valida.")
            return

        actual = self.lista_filas
        anterior = None

        while actual is not None and actual.numero != posicion:
            anterior = actual
            actual = actual.siguiente

        if actual is not None:
            celda = actual.primera

            while celda is not None:
                self.cantidad_celdas -= 1
                celda = celda.derecha

            if anterior is None:
                self.lista_filas = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente

        fila = self.lista_filas

        while fila is not None:
            if fila.numero > posicion:
                fila.numero -= 1
            fila = fila.siguiente

        self.filas -= 1
        self.reconstruir_columnas()
        print("Fila eliminada correctamente.")

    # Insertar una columna completa
    def insertar_columna(self, posicion):
        if posicion < 1 or posicion > self.columnas + 1:
            print("Posicion no valida.")
            return

        fila = self.lista_filas

        while fila is not None:
            celda = fila.primera

            while celda is not None:
                if celda.columna >= posicion:
                    celda.columna += 1

                celda = celda.derecha

            fila = fila.siguiente

        self.columnas += 1
        self.reconstruir_columnas()
        print("Columna insertada correctamente.")

    # Eliminar una columna completa
    def eliminar_columna(self, posicion):
        if posicion < 1 or posicion > self.columnas:
            print("Posicion no valida.")
            return

        fila = self.lista_filas

        while fila is not None:
            actual = fila.primera
            anterior = None

            while actual is not None:
                siguiente = actual.derecha

                if actual.columna == posicion:
                    if anterior is None:
                        fila.primera = siguiente
                    else:
                        anterior.derecha = siguiente

                    self.cantidad_celdas -= 1

                else:
                    if actual.columna > posicion:
                        actual.columna -= 1

                    anterior = actual

                actual = siguiente

            fila = fila.siguiente

        # Eliminar filas que quedaron vacias
        actual = self.lista_filas
        anterior = None

        while actual is not None:
            if actual.primera is None:
                if anterior is None:
                    self.lista_filas = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
            else:
                anterior = actual

            actual = actual.siguiente

        self.columnas -= 1
        self.reconstruir_columnas()
        print("Columna eliminada correctamente.")

    # Mostrar la hoja en forma tabular
    def mostrar(self):
        print("\n--- HOJA DE CALCULO ---")

        print("    ", end="")

        for columna in range(1, self.columnas + 1):
            print(f"{columna:>8}", end="")

        print()

        for fila in range(1, self.filas + 1):
            print(f"{fila:>4}", end="")

            for columna in range(1, self.columnas + 1):
                valor = self.obtener(fila, columna)
                print(f"{valor:>8g}", end="")

            print()

    # Contar las celdas almacenadas
    def contar_celdas(self):
        return self.cantidad_celdas

    # Guardar la hoja en un archivo
    def guardar(self, archivo):
        with open(archivo, "w", encoding="utf-8") as documento:
            documento.write(f"{self.filas},{self.columnas}\n")

            fila = self.lista_filas

            while fila is not None:
                celda = fila.primera

                while celda is not None:
                    documento.write(
                        f"{celda.fila},{celda.columna},{celda.valor}\n"
                    )
                    celda = celda.derecha

                fila = fila.siguiente

        print("Hoja guardada correctamente.")

    # Cargar la hoja desde un archivo
    def cargar(self, archivo):
        with open(archivo, "r", encoding="utf-8") as documento:
            dimensiones = documento.readline().strip().split(",")

            self.filas = int(dimensiones[0])
            self.columnas = int(dimensiones[1])
            self.lista_filas = None
            self.lista_columnas = None
            self.cantidad_celdas = 0

            for linea in documento:
                datos = linea.strip().split(",")

                if len(datos) == 3:
                    fila = int(datos[0])
                    columna = int(datos[1])
                    valor = float(datos[2])

                    self.insertar(fila, columna, valor)

        print("Hoja cargada correctamente.")


# DEMOSTRACION DEL SISTEMA

hoja = HojaCalculo(5, 5)

print("===== HOJA DE CALCULO DISPERSA =====")

# 1. Insertar datos
print("\n1. INSERTAR CELDAS")
hoja.insertar(1, 1, 10)
hoja.insertar(1, 3, 20)
hoja.insertar(2, 2, 30)
hoja.insertar(3, 1, 40)
hoja.insertar(4, 4, 50)
hoja.insertar(5, 5, 60)
hoja.mostrar()

# 2. Actualizar una celda
print("\n2. ACTUALIZAR CELDA")
hoja.insertar(1, 1, 100)
hoja.mostrar()

# 3. Obtener un valor
print("\n3. OBTENER CELDA")
print("Valor de la celda (2,2):", hoja.obtener(2, 2))
print("Valor de la celda (2,3):", hoja.obtener(2, 3))

# 4. Sumar y promediar un rango
print("\n4. CALCULAR RANGO")
hoja.calcular_rango(1, 1, 3, 3)

# 5. Eliminar una celda
print("\n5. ELIMINAR CELDA")
hoja.eliminar(3, 1)
hoja.mostrar()

# 6. Insertar y eliminar filas
print("\n6. GESTION DE FILAS")
hoja.insertar_fila(2)
hoja.mostrar()
hoja.eliminar_fila(2)
hoja.mostrar()

# 7. Insertar y eliminar columnas
print("\n7. GESTION DE COLUMNAS")
hoja.insertar_columna(2)
hoja.mostrar()
hoja.eliminar_columna(2)
hoja.mostrar()

# 8. Comparacion de memoria
print("\n8. EFICIENCIA DE ALMACENAMIENTO")
total = hoja.filas * hoja.columnas
ocupadas = hoja.contar_celdas()

print("Celdas de una matriz completa:", total)
print("Celdas almacenadas en la lista:", ocupadas)
print("Celdas vacias no almacenadas:", total - ocupadas)

if total > 0:
    ahorro = (1 - ocupadas / total) * 100
    print("Reduccion de celdas almacenadas:", round(ahorro, 2), "%")

# 9. Guardar y cargar
print("\n9. GUARDAR Y CARGAR ARCHIVO")
hoja.guardar("hoja_calculo.txt")

nueva_hoja = HojaCalculo(1, 1)
nueva_hoja.cargar("hoja_calculo.txt")
nueva_hoja.mostrar()
