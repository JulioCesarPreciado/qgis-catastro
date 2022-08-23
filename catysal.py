# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'catysal.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from .funcBaseDatos import fnConexionServidor, fnConexionCerrar, fnConexionServidorPg, fnConexionCerrarPg

def llenadatos(self):
             catastral = self.mLineEdit_2.text()
             print("catastral",catastral)
             print(self.mLineEdit.text())
             gConnMySql = fnConexionServidor()
             if (gConnMySql):
                print("conecta")
                cur = gConnMySql.cursor()
                print(catastral)
                ban_conecta=0
                cur.execute( "select catastro.id_catastro,catastro.catastral,catastro.propie,catastro.calle,catastro.exterior,catastro.interior,catastro.area_terr_titulo,catastro.area_const,catastro.val_terr,catastro.val_const,catastro.val_fiscal,catastro.tasa,saldos.id_catastro,saldos.impuesto,saldos.recargos,saldos.multa,saldos.gastos,saldos.gastos_ejecucion,saldos.baldio,saldos.saldo_total FROM catastro inner join saldos on catastro.id_catastro = saldos.id_catastro WHERE catastro.catastral = '" + catastral + "'")
                for row in cur.fetchall() :
                    ban_conecta=1
                    print("entra")
                    print(row[0])
                    print(row[1])
                    self.mLineEdit.setText(str(row[0]))
                    self.mLineEdit_3.setText(row[2])
                    if row[3] and row[4] and row[5]:
                        self.mLineEdit_4.setText(row[3]+" "+row[4]+" "+row[5])

                    self.mLineEdit_5.setText(str(row[6]))
                    self.mLineEdit_6.setText(str(row[7]))
                    self.mLineEdit_7.setText(str(row[8]))
                    self.mLineEdit_8.setText(str(row[9]))
                    self.mLineEdit_9.setText(str(row[10]))
                    self.mLineEdit_10.setText(str(row[11]))
                    self.mLineEdit_11.setText(str(row[12]))
                    self.mLineEdit_12.setText(str(row[1]))
                    self.mLineEdit_13.setText(str(row[13]))
                    self.mLineEdit_14.setText(str(row[14]))
                    self.mLineEdit_15.setText(str(row[15]))
                    self.mLineEdit_16.setText(str(row[16]))
                    self.mLineEdit_17.setText(str(row[17]))
                    self.mLineEdit_18.setText(str(row[18]))
                    self.mLineEdit_19.setText(str(row[19]))
                if ban_conecta==0:
                    self.label_text.setText(" Clave no vinculada")
                    self.label_text.setStyleSheet('background-color: darksalmon')

             

class Ui_Catysal(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(535, 327)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 521, 311))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 30, 61, 16))
        self.label.setObjectName("label")
        self.mLineEdit = QgsFilterLineEdit(self.tab)
        self.mLineEdit.setGeometry(QtCore.QRect(80, 20, 121, 27))
        self.mLineEdit.setProperty("qgisRelation", "")
        self.mLineEdit.setObjectName("mLineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        
        self.mLineEdit.setAcceptDrops(False)
        self.mLineEdit.setReadOnly(True)
        
        self.label_2.setGeometry(QtCore.QRect(240, 30, 81, 20))
        self.label_2.setObjectName("label_2")
        self.mLineEdit_2 = QgsFilterLineEdit(self.tab)
        self.mLineEdit_2.setGeometry(QtCore.QRect(330, 20, 151, 27))
        self.mLineEdit_2.setProperty("qgisRelation", "")
        self.mLineEdit_2.setObjectName("mLineEdit_2")
        
        self.mLineEdit_2.setAcceptDrops(False)
        self.mLineEdit_2.setReadOnly(True)
        
        self.label_text = QtWidgets.QLabel(self.tab)
        self.label_text.setGeometry(QtCore.QRect(130, 50, 160, 16))
        self.label_text.setObjectName("label_text")

        self.mLineEdit_3 = QgsFilterLineEdit(self.tab)
        self.mLineEdit_3.setGeometry(QtCore.QRect(90, 70, 391, 27))
        self.mLineEdit_3.setText("")
        self.mLineEdit_3.setProperty("qgisRelation", "")
        self.mLineEdit_3.setObjectName("mLineEdit_3")
        
        self.mLineEdit_3.setAcceptDrops(False)
        self.mLineEdit_3.setReadOnly(True)
        
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 81, 20))
        self.label_4.setObjectName("label_4")
        self.mLineEdit_4 = QgsFilterLineEdit(self.tab)
        self.mLineEdit_4.setGeometry(QtCore.QRect(90, 110, 391, 27))
        self.mLineEdit_4.setText("")
        self.mLineEdit_4.setProperty("qgisRelation", "")
        self.mLineEdit_4.setObjectName("mLineEdit_4")
        
        self.mLineEdit_4.setAcceptDrops(False)
        self.mLineEdit_4.setReadOnly(True)
        
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 121, 20))
        self.label_5.setObjectName("label_5")
        self.mLineEdit_5 = QgsFilterLineEdit(self.tab)
        self.mLineEdit_5.setGeometry(QtCore.QRect(130, 150, 121, 27))
        self.mLineEdit_5.setProperty("qgisRelation", "")
        self.mLineEdit_5.setObjectName("mLineEdit_5")
        
        self.mLineEdit_5.setAcceptDrops(False)
        self.mLineEdit_5.setReadOnly(True)
        
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 111, 20))
        self.label_6.setObjectName("label_6")
        self.mLineEdit_6 = QgsFilterLineEdit(self.tab)
        self.mLineEdit_6.setGeometry(QtCore.QRect(130, 180, 121, 27))
        self.mLineEdit_6.setProperty("qgisRelation", "")
        self.mLineEdit_6.setObjectName("mLineEdit_6")
        
        self.mLineEdit_6.setAcceptDrops(False)
        self.mLineEdit_6.setReadOnly(True)
        
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 220, 65, 16))
        self.label_7.setObjectName("label_7")
        self.mLineEdit_7 = QgsFilterLineEdit(self.tab)
        self.mLineEdit_7.setGeometry(QtCore.QRect(130, 210, 121, 27))
        self.mLineEdit_7.setProperty("qgisRelation", "")
        self.mLineEdit_7.setObjectName("mLineEdit_7")
        
        self.mLineEdit_7.setAcceptDrops(False)
        self.mLineEdit_7.setReadOnly(True)
        
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(270, 160, 81, 20))
        self.label_8.setObjectName("label_8")
        self.mLineEdit_8 = QgsFilterLineEdit(self.tab)
        self.mLineEdit_8.setGeometry(QtCore.QRect(360, 150, 121, 27))
        self.mLineEdit_8.setProperty("qgisRelation", "")
        self.mLineEdit_8.setObjectName("mLineEdit_8")
        
        self.mLineEdit_8.setAcceptDrops(False)
        self.mLineEdit_8.setReadOnly(True)
        
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(270, 190, 91, 20))
        self.label_9.setObjectName("label_9")
        self.mLineEdit_9 = QgsFilterLineEdit(self.tab)
        self.mLineEdit_9.setGeometry(QtCore.QRect(360, 180, 121, 27))
        self.mLineEdit_9.setProperty("qgisRelation", "")
        self.mLineEdit_9.setObjectName("mLineEdit_9")
        
        self.mLineEdit_9.setAcceptDrops(False)
        self.mLineEdit_9.setReadOnly(True)
        
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(270, 220, 61, 16))
        self.label_10.setObjectName("label_10")
        self.mLineEdit_10 = QgsFilterLineEdit(self.tab)
        self.mLineEdit_10.setGeometry(QtCore.QRect(360, 210, 121, 27))
        self.mLineEdit_10.setProperty("qgisRelation", "")
        self.mLineEdit_10.setObjectName("mLineEdit_10")
        
        self.mLineEdit_10.setAcceptDrops(False)
        self.mLineEdit_10.setReadOnly(True)

        
        

        
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label_11.setObjectName("label_11")
        self.mLineEdit_11 = QgsFilterLineEdit(self.tab_2)
        self.mLineEdit_11.setGeometry(QtCore.QRect(90, 20, 121, 27))
        self.mLineEdit_11.setProperty("qgisRelation", "")
        self.mLineEdit_11.setObjectName("mLineEdit_11")
        
        self.mLineEdit_11.setAcceptDrops(False)
        self.mLineEdit_11.setReadOnly(True)
        
        self.mLineEdit_12 = QgsFilterLineEdit(self.tab_2)
        self.mLineEdit_12.setGeometry(QtCore.QRect(340, 20, 151, 27))
        self.mLineEdit_12.setProperty("qgisRelation", "")
        self.mLineEdit_12.setObjectName("mLineEdit_12")
        
        self.mLineEdit_12.setAcceptDrops(False)
        self.mLineEdit_12.setReadOnly(True)
        
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(250, 30, 81, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.label_13.setObjectName("label_13")
        self.mLineEdit_13 = QgsFilterLineEdit(self.tab_2)
        self.mLineEdit_13.setGeometry(QtCore.QRect(90, 70, 121, 27))
        self.mLineEdit_13.setProperty("qgisRelation", "")
        self.mLineEdit_13.setObjectName("mLineEdit_13")
        
        self.mLineEdit_13.setAcceptDrops(False)
        self.mLineEdit_13.setReadOnly(True)
        
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(260, 90, 61, 16))
        self.label_14.setObjectName("label_14")
        self.mLineEdit_14 = QgsFilterLineEdit(self.tab_2)
        self.mLineEdit_14.setGeometry(QtCore.QRect(340, 80, 121, 27))
        self.mLineEdit_14.setProperty("qgisRelation", "")
        self.mLineEdit_14.setObjectName("mLineEdit_14")
        
        self.mLineEdit_14.setAcceptDrops(False)
        self.mLineEdit_14.setReadOnly(True)
        
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(20, 140, 151, 16))
        self.label_15.setObjectName("label_15")
        self.mLineEdit_15 = QgsFilterLineEdit(self.tab_2)
        self.mLineEdit_15.setGeometry(QtCore.QRect(210, 130, 121, 27))
        self.mLineEdit_15.setProperty("qgisRelation", "")
        self.mLineEdit_15.setObjectName("mLineEdit_15")
        
        self.mLineEdit_15.setAcceptDrops(False)
        self.mLineEdit_15.setReadOnly(True)
        
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(20, 200, 61, 16))
        self.label_16.setObjectName("label_16")
        self.mLineEdit_16 = QgsFilterLineEdit(self.tab_2)
        self.mLineEdit_16.setGeometry(QtCore.QRect(90, 190, 121, 27))
        self.mLineEdit_16.setProperty("qgisRelation", "")
        self.mLineEdit_16.setObjectName("mLineEdit_16")
        
        self.mLineEdit_16.setAcceptDrops(False)
        self.mLineEdit_16.setReadOnly(True)
        
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(240, 200, 101, 16))
        self.label_17.setObjectName("label_17")
        self.mLineEdit_17 = QgsFilterLineEdit(self.tab_2)
        self.mLineEdit_17.setGeometry(QtCore.QRect(340, 190, 121, 27))
        self.mLineEdit_17.setProperty("qgisRelation", "")
        self.mLineEdit_17.setObjectName("mLineEdit_17")
        
        self.mLineEdit_17.setAcceptDrops(False)
        self.mLineEdit_17.setReadOnly(True)
        
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(20, 260, 121, 16))
        self.label_18.setObjectName("label_18")
        self.mLineEdit_18 = QgsFilterLineEdit(self.tab_2)
        self.mLineEdit_18.setGeometry(QtCore.QRect(160, 250, 121, 27))
        self.mLineEdit_18.setProperty("qgisRelation", "")
        self.mLineEdit_18.setObjectName("mLineEdit_18")
        
        self.mLineEdit_18.setAcceptDrops(False)
        self.mLineEdit_18.setReadOnly(True)
        
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(300, 260, 41, 16))
        self.label_19.setObjectName("label_19")
        self.mLineEdit_19 = QgsFilterLineEdit(self.tab_2)
        self.mLineEdit_19.setGeometry(QtCore.QRect(340, 250, 121, 27))
        self.mLineEdit_19.setProperty("qgisRelation", "")
        self.mLineEdit_19.setObjectName("mLineEdit_19")
        
        self.mLineEdit_19.setAcceptDrops(False)
        self.mLineEdit_19.setReadOnly(True)
        
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Información Catastral y Saldos"))
        self.label.setText(_translate("Dialog", "Id Catastro"))
        self.label_2.setText(_translate("Dialog", "Clave Catastral"))
        self.label_3.setText(_translate("Dialog", "Propietario"))
        self.label_4.setText(_translate("Dialog", "Ubicacion Legal"))
        self.label_5.setText(_translate("Dialog", "Area del Terreno(Título)"))
        self.label_6.setText(_translate("Dialog", "Area de Construccion"))
        self.label_7.setText(_translate("Dialog", "Valor Catastral"))
        self.label_8.setText(_translate("Dialog", "Valor de Terreno"))
        self.label_9.setText(_translate("Dialog", "Valor de Constr"))
        self.label_10.setText(_translate("Dialog", "Tasa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Catastro"))
        self.label_11.setText(_translate("Dialog", "Id Catastro"))
        self.label_12.setText(_translate("Dialog", "Clave Catastral"))
        self.label_13.setText(_translate("Dialog", "Impuesto"))
        self.label_14.setText(_translate("Dialog", "Recargos"))
        self.label_15.setText(_translate("Dialog", "Multa (Sanción Administrativa)"))
        self.label_16.setText(_translate("Dialog", "Gastos"))
        self.label_17.setText(_translate("Dialog", "Gastos de Ejecisión"))
        self.label_18.setText(_translate("Dialog", "Baldio (Baldio Total DP)"))
        self.label_19.setText(_translate("Dialog", "Saldo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Saldos"))
from qgsfilterlineedit import QgsFilterLineEdit


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Catysal()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
