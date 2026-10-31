"""Prueba unitaria de la función de ejemplo."""

import unittest

from bootstrap import sumar


class SumarTest(unittest.TestCase):
    def test_suma_dos_enteros(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_suma_dos_ceros(self):
        self.assertEqual(sumar(0, 0), 0)

    def test_suma_cero_y_positivo(self):
        self.assertEqual(sumar(0, 5), 5)

    def test_suma_positivo_y_cero(self):
        self.assertEqual(sumar(5, 0), 5)

    def test_suma_dos_negativos(self):
        self.assertEqual(sumar(-2, -3), -5)

    def test_suma_negativo_y_positivo(self):
        self.assertEqual(sumar(-2, 3), 1)

    def test_suma_positivo_y_negativo(self):
        self.assertEqual(sumar(3, -2), 1)

    def test_suma_enteros_grandes(self):
        self.assertEqual(sumar(10**12, 10**12), 2 * 10**12)
