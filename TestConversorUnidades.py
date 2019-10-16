# coding=utf-8
# Desenvolvimento Romullo
# ConversorUnidadesTeste.py

from unittest import TestCase
from ConversorUnidades import ConversorUnidades

__author__ = 'Desenvolvimento Romullo'


class ConversorUnidadesTeste(TestCase):
            # Define Métodos de Testes

            def testCelsiusParaFahrenheit(self):
                # Testa método
                self.assertEqual(32.0, ConversorUnidades.celsiusParaFahrenheit(0))

            def testFahrenheitParaCelsius(self):
                # Testa método
                self.assertEqual(-17.77777777777778, ConversorUnidades.fahrenheitParaCelsius(0))





