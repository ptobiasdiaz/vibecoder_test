"""Prueba unitaria de la función de ejemplo."""

import unittest

from bootstrap import sumar


class SumarTest(unittest.TestCase):
    def test_suma_dos_enteros(self):
        self.assertEqual(sumar(2, 3), 5)
