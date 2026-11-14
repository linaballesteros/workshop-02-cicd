"""Aplicación web Flask de una calculadora básica.

Expone una única ruta que muestra un formulario (GET) y calcula el
resultado de la operación seleccionada (POST).
"""

import os

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)
# Clave para firmar el token CSRF. En producción se define por variable de
# entorno; en desarrollo se genera una aleatoria por proceso.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", os.urandom(32).hex())
# Habilita la protección CSRF en todos los formularios POST.
csrf = CSRFProtect(app)


@app.route("/", methods=["GET", "POST"])
def index():
    """Muestra el formulario y calcula el resultado de la operación."""
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    app.run(port=5000, host="127.0.0.1")
