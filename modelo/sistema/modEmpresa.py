# -----------------------------------------------------------------
# Clase mEmpresa
# Modelo para manejar información de la tabla empresa
# -----------------------------------------------------------------

# Importa la libreria globales
import entidades.entGlobales         as eg
import entidades.sistema.entEmpresa  as ee
import funciones.funcBaseDatos       as fbd

# Constantes para las Columnas de la Tabla de usuarios
INT_COL_EMPRESA_NOMBRE    = 0
INT_COL_EMPRESA_DIRECCION = 1
INT_COL_EMPRESA_TELEFONO  = 2
INT_COL_EMPRESA_RFC       = 3
INT_COL_EMPRESA_SERIAL    = 4
INT_COL_EMPRESA_LOGO      = 5

# Definición de la Clase
class mEmpresa:

    # Función para obtener información de la Empresa
    def fnEmpresaGet(self):

        # Crea el objeto de Entidad Empresa
        oEmpresa = ee.eEmpresa()

        # Prepara el Query para Consulta
        sQuery =  " SELECT * FROM empresa "

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount>0):

                # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Coloca los datos en el objeto
                oEmpresa.setStrEmpresaNombre(registro[INT_COL_EMPRESA_NOMBRE])
                oEmpresa.setStrEmpresaDireccion(registro[INT_COL_EMPRESA_DIRECCION])
                oEmpresa.setStrEmpresaTelefono(registro[INT_COL_EMPRESA_TELEFONO])
                oEmpresa.setStrEmpresaRfc(registro[INT_COL_EMPRESA_RFC])
                oEmpresa.setStrEmpresaSerial(registro[INT_COL_EMPRESA_SERIAL])
                oEmpresa.setStrEmpresaLogo(registro[INT_COL_EMPRESA_LOGO])
                
        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Objeto
        return oEmpresa

    # Función para obtener establecer los valores de la Empresa
    def fnEmpresaSet(self, oEmpresa):

        # Prepara el Query para realizar el Update
        sQuery =  " UPDATE empresa SET "
        sQuery += " strEmpresaNombre     = '"+str(oEmpresa.getStrEmpresaNombre())+"',"
        sQuery += " strEmpresaDireccion  = '"+str(oEmpresa.getStrEmpresaDireccion())+"',"
        sQuery += " strEmpresaTelefono   = '"+str(oEmpresa.getStrEmpresaTelefono())+"',"
        sQuery += " strEmpresaRfc        = '"+str(oEmpresa.getStrEmpresaRfc())+"',"
        sQuery += " strEmpresaSerial     = '"+str(oEmpresa.getStrEmpresaSerial())+"',"
        sQuery += " strEmpresaLogo       = '"+str(oEmpresa.getStrEmpresaLogo())+"'"

        # Ejecuta y Retorna
        return fbd.fnExecuteUpdateSql(sQuery,True)

    # Función para obtener el Logo de la Empresa
    def fnEmpresaLogoGet(self):

        # Crea el valor a retornar
        sLogo=""

        # Prepara el Query para Consulta
        sQuery =  " SELECT strEmpresaLogo FROM empresa "

        # Intenta Ejecuta la Sentencia de
        if (fbd.fnExecuteSql(sQuery)):

            # Verifica que haya habido resultados
            if (eg.gCursor.rowcount>0):

                # Lee el Registro
                registro = eg.gCursor.fetchone()

                # Coloca los datos en el objeto
                sLogo = registro[0]
                
        
        # Cierra el Cursor
        eg.gCursor.close()
        
        # Retorna el Logo
        return sLogo


# Función main
if __name__ == "__main__":

    # Cargo la libreria
    from PyQt5 import QtWidgets

    # Importa la librería sys
    import sys

    # Crea el objeto de Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Conectando al Servidor
    print("Conectando al Servidor ...")
    fbd.fnConexionServidor()

    # Declarando un objeto del Modelo
    datEmpresa = mEmpresa()

    # Declarando un objeto de la entidad Empresa
    oEmpresa = ee.eEmpresa()

    # Ejecutando la Consulta de los datos
    oEmpresa = datEmpresa.fnEmpresaGet()

    # Desplegando los datos
    print("Nombre    :",oEmpresa.getStrEmpresaNombre())
    print("Direccion :",oEmpresa.getStrEmpresaDireccion())
    print("Telefono  :",oEmpresa.getStrEmpresaTelefono())
    print("Rfc       :",oEmpresa.getStrEmpresaRfc())
    print("Serial    :",oEmpresa.getStrEmpresaSerial())
    print("Logo      :",oEmpresa.getStrEmpresaLogo())

    # Desplegando el Logo
    print("La ruta del Logo:",datEmpresa.fnEmpresaLogoGet())

    # Ejecuto Modificaion
    print("Modificó:",datEmpresa.fnEmpresaSet(oEmpresa))
    
    # Cierra la Conexión
    print("Cerrando Conexión ...")
    fbd.fnConexionCerrar()
