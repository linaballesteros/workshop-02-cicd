# Dockerfile
# Usa una imagen base oficial de Python. Elige una versión específica para consistencia.
FROM python:3.13-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el lockfile con versiones y hashes fijados para una build reproducible
COPY requirements.lock.txt .

# Instala solo las dependencias de ejecución (Flask y Gunicorn)
# --no-cache-dir reduce el tamaño de la imagen
# --only-binary :all: instala solo wheels y evita ejecutar scripts de setup
# --require-hashes fija versiones resueltas y verifica la integridad por hash
RUN pip install --no-cache-dir --only-binary :all: --require-hashes -r requirements.lock.txt

# Copia el código de la aplicación (solo la carpeta app)
COPY app/ ./app/

# Crea un usuario sin privilegios y ejecuta la aplicación como ese usuario
RUN useradd --create-home --uid 1000 appuser \
    && chown -R appuser:appuser /app
USER appuser

# Expón el puerto en el que Gunicorn servirá la aplicación
# Gunicorn por defecto usa 8000, así que usaremos ese.
EXPOSE 8000

# Comando para ejecutar la aplicación usando Gunicorn cuando el contenedor inicie
# 'app.app:app' significa: del archivo app.py dentro del paquete app, usa la instancia 'app' de Flask.
# 'workers=4' es un ejemplo, ajusta según sea necesario.
# 'bind 0.0.0.0:8000' hace que Gunicorn escuche en todas las interfaces de red en el puerto 8000.
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8000", "app.app:app"]