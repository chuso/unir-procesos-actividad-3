"""
Módulo: calculadora.py
Descripción: Implementación de una calculadora con las cuatro operaciones
             aritméticas básicas (suma, resta, multiplicación, división).

Asignatura: Procesos en Ingeniería del Software
Actividad 3 grupal. Diseño de pruebas de software
"""


class Calculadora:
    """
    Clase Calculadora.

    Encapsula las cuatro operaciones aritméticas básicas como métodos
    de instancia. Cada método recibe dos operandos numéricos (int o float)
    y devuelve el resultado de la operación correspondiente.

    La clase no almacena estado entre llamadas: cada operación es pura
    y depende exclusivamente de sus argumentos. Esto facilita las pruebas
    unitarias (cada prueba es independiente).
    """

    def sumar(self, a: float, b: float) -> float:
        """
        Devuelve la suma de dos números.

        Parámetros
        ----------
        a : float
            Primer sumando.
        b : float
            Segundo sumando.

        Devuelve
        --------
        float
            Resultado de a + b.
        """
        return a + b

    def restar(self, a: float, b: float) -> float:
        """
        Devuelve la resta de dos números (minuendo menos sustraendo).

        Parámetros
        ----------
        a : float
            Minuendo.
        b : float
            Sustraendo.

        Devuelve
        --------
        float
            Resultado de a - b.
        """
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        """
        Devuelve el producto de dos números.

        Parámetros
        ----------
        a : float
            Primer factor.
        b : float
            Segundo factor.

        Devuelve
        --------
        float
            Resultado de a * b.
        """
        return a * b

    def dividir(self, a: float, b: float) -> float:
        """
        Devuelve el cociente de dos números.

        Parámetros
        ----------
        a : float
            Dividendo.
        b : float
            Divisor. No puede ser 0.

        Devuelve
        --------
        float
            Resultado de a / b.

        Excepciones
        -----------
        ValueError
            Si el divisor (b) es 0. Se gestiona explícitamente para
            ofrecer un mensaje descriptivo en lugar de dejar que se
            propague la excepción nativa ZeroDivisionError.
        """
        if b == 0:
            raise ValueError("La división por cero no está definida.")
        return a / b


if __name__ == "__main__":
    # Pequeña demostración manual (no forma parte de las pruebas).
    calc = Calculadora()
    print("2 + 3 =", calc.sumar(2, 3))
    print("10 - 4 =", calc.restar(10, 4))
    print("6 * 7 =", calc.multiplicar(6, 7))
    print("15 / 4 =", calc.dividir(15, 4))
