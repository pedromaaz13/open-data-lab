"""pytest: añade src/ al path para importar los módulos del proyecto."""
import os, sys
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)
