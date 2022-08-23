# ------------------------------------------------------------------
# Módulo funcBaseDatos.py
# Constantes, Variables y Funciones para el Manejo de Bases de Datos
# ------------------------------------------------------------------

# Librería de mysql
# pip install mysql-conector
#import pymysql
import psycopg2
import pyodbc
from qgis.utils import iface
from qgis.PyQt.QtCore import *
from qgis.core import *



# Función para conectarse a mySql
def fnUri():
    uri = QgsDataSourceUri()
    uri.setConnection("192.168.254.202", "5432", "postgis", "postgres", "4@dm!nP0str35")
    return uri


def fnConexionServidor():
        #direccion_servidor = 'WIN-M7M66FBC314'
        #nombre_bd = 'catastro_geo'
        #nombre_usuario = 'pruebas'     
        #password = 'pruebas'
        direccion_servidor = '192.168.254.201'
        nombre_bd = 'catastro_geo'
        nombre_usuario = 'sa'     
        password = 'Ayuntamiento.LC1102-'
        try:
            conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=' +direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
            print("OK! conexión exitosa")
            return conexion
        except Exception as e:
            # Atrapar error
            print("Ocurrió un error al conectar a SQL Server: ", e)
            return False 
            ######################################3333333
        # try:
        
            # # Creamos una conexión e intentamos conectar
            # ConnMySql = pymysql.connect(host='localhost', user= 'root', passwd='taQ99Zm007', db='usuarios')
        

            # # Retorna verdadero
            # return ConnMySql

        # except pymysql.Error as err:  
            # iface.messageBar().pushMessage("errors3", "no corre!", level=Qgis.Success)
            # return False     

    

# Función para cerrar la Conexión
def fnConexionCerrar(conexion):

    # Grabando en el Log
    #fa.fnLogGraba("funcBaseDatos","fnConexionCerrar","Informativo","Cerrando la Conexión al Servidor")

    # Cierra la Conexión
    conexion.close()

    
# Función para conectarse a postgres
def fnConexionServidorPg():
    
    
        try:
        
            # Creamos una conexión e intentamos conectar
            gConnPostgreSql = psycopg2.connect(database='postgis', port='5432', user='postgres',host='192.168.254.202',password='4@dm!nP0str35')
        

            # Retorna verdadero
            return gConnPostgreSql

        except gConnPostgreSql.Error as err:  
            iface.messageBar().pushMessage("errors3", "no corre!", level=Qgis.Success)
            return False     

    

# Función para cerrar la Conexión posgres
def fnConexionCerrarPg(gConnPostgreSql):

    # Grabando en el Log
    #fa.fnLogGraba("funcBaseDatos","fnConexionCerrar","Informativo","Cerrando la Conexión al Servidor")

    # Cierra la Conexión
    gConnPostgreSql.close()

    


# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Test Conexion a BD
    