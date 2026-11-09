
# Jeremy Arévalo
# PROBLEMA 3: SISTEMA DE GESTION DE POLINOMIOS
# Implementacion mediante listas enlazadas simples

# Nodo que almacena un termino del polinomio
class Nodo:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None


# Clase para gestionar los polinomios
class Polinomio:
    def __init__(self):
        self.cabeza = None

    # Insertar terminos ordenados por exponente
    def insertar(self, coeficiente, exponente):
        if coeficiente == 0:
            return

        nuevo = Nodo(coeficiente, exponente)

        if self.cabeza is None or self.cabeza.exponente < exponente:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return

        actual = self.cabeza
        anterior = None

        while actual is not None and actual.exponente > exponente:
            anterior = actual
            actual = actual.siguiente

        # Si el exponente ya existe, sumar coeficientes
        if actual is not None and actual.exponente == exponente:
            actual.coeficiente += coeficiente

            if actual.coeficiente == 0:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
        else:
            nuevo.siguiente = actual
            anterior.siguiente = nuevo

    # Mostrar el polinomio en formato matematico
    def mostrar(self):
        actual = self.cabeza
        resultado = ""

        while actual is not None:
            coef = actual.coeficiente
            exp = actual.exponente

            if resultado != "":
                resultado += " - " if coef < 0 else " + "
            elif coef < 0:
                resultado += "-"

            valor = abs(coef)

            if exp == 0:
                resultado += str(valor)
            else:
                if valor != 1:
                    resultado += str(valor)

                resultado += "x"

                if exp != 1:
                    resultado += "^" + str(exp)

            actual = actual.siguiente

        print(resultado if resultado else "0")

    # Sumar dos polinomios
    def sumar(self, otro):
        resultado = Polinomio()

        actual = self.cabeza
        while actual is not None:
            resultado.insertar(actual.coeficiente, actual.exponente)
            actual = actual.siguiente

        actual = otro.cabeza
        while actual is not None:
            resultado.insertar(actual.coeficiente, actual.exponente)
            actual = actual.siguiente

        return resultado

    # Restar dos polinomios
    def restar(self, otro):
        resultado = Polinomio()

        actual = self.cabeza
        while actual is not None:
            resultado.insertar(actual.coeficiente, actual.exponente)
            actual = actual.siguiente

        actual = otro.cabeza
        while actual is not None:
            resultado.insertar(-actual.coeficiente, actual.exponente)
            actual = actual.siguiente

        return resultado

    # Multiplicar dos polinomios
    def multiplicar(self, otro):
        resultado = Polinomio()

        actual1 = self.cabeza

        while actual1 is not None:
            actual2 = otro.cabeza

            while actual2 is not None:
                coef = actual1.coeficiente * actual2.coeficiente
                exp = actual1.exponente + actual2.exponente

                resultado.insertar(coef, exp)
                actual2 = actual2.siguiente

            actual1 = actual1.siguiente

        return resultado

    # Evaluar el polinomio para un valor de x
    def evaluar(self, x):
        resultado = 0
        actual = self.cabeza

        while actual is not None:
            resultado += actual.coeficiente * (x ** actual.exponente)
            actual = actual.siguiente

        return resultado

    # Derivar el polinomio
    def derivar(self):
        resultado = Polinomio()
        actual = self.cabeza

        while actual is not None:
            if actual.exponente > 0:
                coef = actual.coeficiente * actual.exponente
                exp = actual.exponente - 1
                resultado.insertar(coef, exp)

            actual = actual.siguiente

        return resultado

    # Integrar el polinomio (sin constante de integracion)
    def integrar(self):
        resultado = Polinomio()
        actual = self.cabeza

        while actual is not None:
            coef = actual.coeficiente / (actual.exponente + 1)
            exp = actual.exponente + 1

            resultado.insertar(coef, exp)
            actual = actual.siguiente

        return resultado


# CREACION DE TRES POLINOMIOS DIFERENTES

p1 = Polinomio()
p1.insertar(3, 4)
p1.insertar(-2, 2)
p1.insertar(5, 0)

p2 = Polinomio()
p2.insertar(2, 3)
p2.insertar(4, 2)
p2.insertar(-3, 0)

p3 = Polinomio()
p3.insertar(5, 3)
p3.insertar(-2, 1)
p3.insertar(7, 0)


# DEMOSTRACION DE LAS OPERACIONES

print("===== SISTEMA DE GESTION DE POLINOMIOS =====")

print("\nPOLINOMIO 1:")
p1.mostrar()

print("\nPOLINOMIO 2:")
p2.mostrar()

print("\nPOLINOMIO 3:")
p3.mostrar()


# Suma
print("\n1. SUMA DE POLINOMIOS")
p1.sumar(p2).mostrar()
p2.sumar(p3).mostrar()


# Resta
print("\n2. RESTA DE POLINOMIOS")

print("P1 - P2:")
p1.restar(p2).mostrar()

print("P2 - P1:")
p2.restar(p1).mostrar()


# Multiplicacion
print("\n3. MULTIPLICACION DE POLINOMIOS")
p1.multiplicar(p2).mostrar()
p2.multiplicar(p3).mostrar()

# Evaluacion
print("\n4. EVALUACION PARA x = 2")
print("P1 =", p1.evaluar(2))
print("P2 =", p2.evaluar(2))
print("P3 =", p3.evaluar(2))

# Derivacion
print("\n5. DERIVADA DE POLINOMIOS")
p1.derivar().mostrar()
p2.derivar().mostrar()
p3.derivar().mostrar()

# Integracion
print("\n6. INTEGRACION DE POLINOMIOS")
p1.integrar().mostrar()
p2.integrar().mostrar()
p3.integrar().mostrar()
