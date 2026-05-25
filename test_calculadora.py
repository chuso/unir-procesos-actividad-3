"""
Módulo: test_calculadora.py
Descripción: Pruebas unitarias para la clase Calculadora utilizando la
             librería estándar unittest de Python.

Asignatura: Procesos en Ingeniería del Software
Actividad 3 grupal. Diseño de pruebas de software

Diseño de las pruebas
---------------------
Cada operación dispone, como mínimo, de los tres casos exigidos en el
enunciado (positivos, negativos y cero) más casos adicionales para cubrir
particiones de equivalencia relevantes y, en el caso de la división, la
gestión del error por divisor nulo.

Convenciones aplicadas
----------------------
- Nombrado de los métodos de prueba con el patrón
  test_<operacion>_<escenario>_<resultadoEsperado>
  (siguiendo el ejemplo de la diapositiva 10 del Tema 7).
- Estructura Arrange / Act / Assert dentro de cada método.
- Comparaciones de igualdad entre flotantes mediante assertAlmostEqual
  para evitar falsos negativos por imprecisión binaria.

Ejecución
---------
Desde el directorio del proyecto:
    python -m unittest test_calculadora.py -v
"""

import unittest

from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    """Conjunto de pruebas unitarias para la clase Calculadora."""

    def setUp(self) -> None:
        """
        setUp se ejecuta antes de cada prueba.
        Crea una nueva instancia de Calculadora para garantizar el
        aislamiento entre pruebas (no se comparte estado).
        """
        self.calc = Calculadora()

    # ------------------------------------------------------------------
    # Pruebas de la operación SUMA
    # ------------------------------------------------------------------

    def test_sumar_dos_positivos_devuelve_suma(self) -> None:
        """Suma de dos enteros positivos: 5 + 3 = 8."""
        # Arrange
        a, b = 5, 3
        # Act
        resultado = self.calc.sumar(a, b)
        # Assert
        self.assertEqual(resultado, 8)

    def test_sumar_dos_negativos_devuelve_suma_negativa(self) -> None:
        """Suma de dos enteros negativos: -2 + -7 = -9."""
        resultado = self.calc.sumar(-2, -7)
        self.assertEqual(resultado, -9)

    def test_sumar_numero_y_cero_devuelve_el_numero(self) -> None:
        """Elemento neutro de la suma: 4 + 0 = 4."""
        resultado = self.calc.sumar(4, 0)
        self.assertEqual(resultado, 4)

    def test_sumar_positivo_y_negativo_devuelve_resta(self) -> None:
        """Caso adicional: signos opuestos. 10 + (-4) = 6."""
        resultado = self.calc.sumar(10, -4)
        self.assertEqual(resultado, 6)

    def test_sumar_decimales_devuelve_suma_correcta(self) -> None:
        """Caso adicional: operandos en coma flotante. 1.5 + 2.25 = 3.75."""
        resultado = self.calc.sumar(1.5, 2.25)
        self.assertAlmostEqual(resultado, 3.75, places=7)

    # ------------------------------------------------------------------
    # Pruebas de la operación RESTA
    # ------------------------------------------------------------------

    def test_restar_dos_positivos_devuelve_resta(self) -> None:
        """Resta de dos enteros positivos: 10 - 4 = 6."""
        resultado = self.calc.restar(10, 4)
        self.assertEqual(resultado, 6)

    def test_restar_dos_negativos_devuelve_resta(self) -> None:
        """Resta de dos enteros negativos: -5 - (-3) = -2."""
        resultado = self.calc.restar(-5, -3)
        self.assertEqual(resultado, -2)

    def test_restar_numero_menos_cero_devuelve_el_numero(self) -> None:
        """Elemento neutro de la resta por la derecha: 7 - 0 = 7."""
        resultado = self.calc.restar(7, 0)
        self.assertEqual(resultado, 7)

    def test_restar_cero_menos_numero_devuelve_opuesto(self) -> None:
        """Cero menos un número devuelve el opuesto: 0 - 5 = -5."""
        resultado = self.calc.restar(0, 5)
        self.assertEqual(resultado, -5)

    def test_restar_resultado_negativo(self) -> None:
        """Caso adicional: minuendo menor que sustraendo. 3 - 8 = -5."""
        resultado = self.calc.restar(3, 8)
        self.assertEqual(resultado, -5)

    # ------------------------------------------------------------------
    # Pruebas de la operación MULTIPLICACIÓN
    # ------------------------------------------------------------------

    def test_multiplicar_dos_positivos_devuelve_producto(self) -> None:
        """Producto de dos positivos: 4 * 5 = 20."""
        resultado = self.calc.multiplicar(4, 5)
        self.assertEqual(resultado, 20)

    def test_multiplicar_dos_negativos_devuelve_positivo(self) -> None:
        """Producto de dos negativos: -3 * -4 = 12."""
        resultado = self.calc.multiplicar(-3, -4)
        self.assertEqual(resultado, 12)

    def test_multiplicar_por_cero_devuelve_cero(self) -> None:
        """Elemento absorbente: 7 * 0 = 0."""
        resultado = self.calc.multiplicar(7, 0)
        self.assertEqual(resultado, 0)

    def test_multiplicar_positivo_por_negativo_devuelve_negativo(self) -> None:
        """Caso adicional: signos opuestos. 6 * (-3) = -18."""
        resultado = self.calc.multiplicar(6, -3)
        self.assertEqual(resultado, -18)

    def test_multiplicar_por_uno_devuelve_el_numero(self) -> None:
        """Elemento neutro: 9 * 1 = 9."""
        resultado = self.calc.multiplicar(9, 1)
        self.assertEqual(resultado, 9)

    # ------------------------------------------------------------------
    # Pruebas de la operación DIVISIÓN
    # ------------------------------------------------------------------

    def test_dividir_dos_positivos_devuelve_cociente(self) -> None:
        """División exacta de positivos: 10 / 2 = 5."""
        resultado = self.calc.dividir(10, 2)
        self.assertEqual(resultado, 5)

    def test_dividir_dos_negativos_devuelve_positivo(self) -> None:
        """División de dos negativos: -10 / -2 = 5."""
        resultado = self.calc.dividir(-10, -2)
        self.assertEqual(resultado, 5)

    def test_dividir_cero_entre_numero_devuelve_cero(self) -> None:
        """Dividendo cero: 0 / 5 = 0."""
        resultado = self.calc.dividir(0, 5)
        self.assertEqual(resultado, 0)

    def test_dividir_resultado_decimal(self) -> None:
        """División no exacta: 7 / 2 = 3.5."""
        resultado = self.calc.dividir(7, 2)
        self.assertAlmostEqual(resultado, 3.5, places=7)

    def test_dividir_por_cero_lanza_value_error(self) -> None:
        """
        Gestión de errores: la división por cero debe lanzar ValueError
        con un mensaje descriptivo. Se utiliza assertRaises como gestor
        de contexto para capturar y verificar la excepción.
        """
        # Arrange
        a, b = 5, 0
        # Act + Assert
        with self.assertRaises(ValueError) as contexto:
            self.calc.dividir(a, b)
        # Verificación del mensaje (refuerza la calidad de la prueba)
        self.assertIn("cero", str(contexto.exception).lower())

    def test_dividir_cero_entre_cero_lanza_value_error(self) -> None:
        """
        Caso límite: 0 / 0 también debe lanzar ValueError, ya que la
        operación tampoco está matemáticamente definida.
        """
        with self.assertRaises(ValueError):
            self.calc.dividir(0, 0)


if __name__ == "__main__":
    # Permite ejecutar el archivo directamente con:  python test_calculadora.py
    unittest.main(verbosity=2)
