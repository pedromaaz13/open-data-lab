"""Configuración de pytest para el proyecto.

Añade src/ al sys.path para que los tests puedan importar los módulos del proyecto
(config, indicators, transform, ...) sin convertir las carpetas numeradas del
repositorio en paquetes Python.
"""
import os
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)
