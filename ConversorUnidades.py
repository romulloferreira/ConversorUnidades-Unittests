# coding=utf-8
# Desenvolvimento Romullo Ferreira
# ConversorUnidades.py

__author__ = 'Desenvolvimento Romullo Ferreira'


class ConversorUnidades():

    # Define métodos Getter e Setter
    def celsiusParaFahrenheit(temperatura):
        return (temperatura * 1.8 + 32)

    def fahrenheitParaCelsius(temperatura):
        return ((temperatura - 32) / 1.8)
