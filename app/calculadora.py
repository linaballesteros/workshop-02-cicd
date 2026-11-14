"""Operaciones aritméticas básicas usadas por la calculadora."""

# IMPORTANTE: reemplaza ??? con los nombres completos de los 3 integrantes,
# separados por " | " y en el mismo orden de la sección Integrantes del README.
# Ejemplo: "Ana María Pérez | Luis Andrés Gómez | Sara Restrepo Ríos"
AUTOR = "Lina Sofía Ballesteros | Quinnie Nastasja Villareal | Alejandro Ríos"


def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta de a menos b."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto de a por b."""
    return a * b


def dividir(a, b):
    """Devuelve el cociente de a entre b; lanza error si b es cero."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
