# -------------------------------------------------------------------
# Módulo entGlobales.py
# Constantes y Variables Globales al Sistema
# -------------------------------------------------------------------

# Importamos librería
from typing import TextIO

# Variables de MySql no se pudieran manejar a través de la clase
gConnMySql        = 0        # Conexión a la Base de Datos
gCursor           = 0        # El Cursor par hacer Consultas

# Declaro la Clase
class eGlobales:

    # -------------------------------------------------------------------
    # Constantes
    # -------------------------------------------------------------------
   
    INICIALIZACION  = "inicializacion.xml" # Archivo de Inicialización
    
      
    # ------------------------------------------------------------------
    # Variables Globales
    # ------------------------------------------------------------------
    UsuarioIde      = "UnKnow" # Usuario del Sistema
    UsuarioNom      = "Unknow" # Nombre del Usuario
    

    # En el dialogo de Ventana
    BotonPresionado = -1

    
# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    
