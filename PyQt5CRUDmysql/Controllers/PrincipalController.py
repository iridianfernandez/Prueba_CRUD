import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Database.Connection import connection
from Models.addPerson import AddPerson

class PrincipalController():

    def __init__(self, crud):
        self.addPerson = AddPerson(connection())
        self.crud = crud
    
#    def listaPersonas(self):
        table = self.crud.table_datos
        personas = self.AddPerson.getPersons()
        table.setRowCount(0)
        for row_number, row_data in enumerate(personas):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def showPerson(self):
        table = self.CRUD.table_datos
        if table.currentItem() != None:
            id = table.currentItem().text()
            print(id)
            persona = self.AddPerson.getPerson(id)
            if persona:
                print(persona)
                msg = QMessageBox()
                msg.setWindowTitle(persona[1])
                msg.setText(persona[1])

                msg.setIcon(QMessageBox.Information)

                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText('ID: '+persona[0]+'\nNombre: '+persona[1]+'\nApellido: '+persona[2]+'\nEdad: '+persona[3]+'\nOcupacion: '+persona[4]+'\nTelefono: '+persona[5]+'\nDomicilio: '+persona[6]+'\nObservaciones: '+persona[7])

                x = msg.exec_()
    
    def updatePersons(self):
        table = self.CRUD.table_datos
        personas = []
        fila = []
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number,column_number) != None:
                    fila.append(table.item(row_number,column_number).text())
            if len(fila)>0:
                personas.append(fila)
            fila = []
        
        if len(personas)>0:
            for per in personas:
                self.AddPerson.updatePerson(per[0],per[1],per[2],per[3],per[4],per[5],per[6],per[7])
        
        self.listaPersonas()
    
    def deletePersons(self):
        table = self.CRUD.table_datos
        if table.currentItem() != None:
            id = table.currentItem().text()
            persona = self.AddPerson.getPerson(id)
            if persona:
                self.AddPerson.deletePerson(id)
        self.listaPersonas()
    
    def openCreate(self, Ui_Crear):
        self.CRUD.Form = QtWidgets.QWidget()
        self.CRUD.ui = Ui_Crear()
        self.CRUD.ui.setupUi(self.CRUD.Form)
        self.CRUD.Form.show()