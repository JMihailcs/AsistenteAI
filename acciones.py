import webbrowser
import subprocess
import urllib.parse
import os
import contextlib
from voz import hablar

def ejecutar_comando(accion, aplicacion, parametro=""):
    """Ejecuta una acción según lo que diga el modelo."""
    if accion == "buscar" and aplicacion== "youtube":
        query = urllib.parse.quote(parametro)
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        hablar(f"Buscando {parametro} en YouTube")
    elif accion == "abrir_google":
        webbrowser.open("https://www.google.com")
        hablar("Abriendo Google")
    elif accion == "abrir_programa":
        subprocess.Popen(parametro)  # Ejemplo: "gedit", "calc"
        hablar(f"Abriendo {parametro}")
    else:
        hablar("No entendí lo que quieres hacer.")

@contextlib.contextmanager
def silenciar_alsa():
    """Context manager para silenciar errores de ALSA temporalmente"""
    # Guardar configuración original
    old_stderr = os.dup(2)
    
    # Redirigir stderr a /dev/null
    with open(os.devnull, 'w') as devnull:
        os.dup2(devnull.fileno(), 2)
    
    try:
        yield
    finally:
        # Restaurar stderr
        os.dup2(old_stderr, 2)
        os.close(old_stderr)
