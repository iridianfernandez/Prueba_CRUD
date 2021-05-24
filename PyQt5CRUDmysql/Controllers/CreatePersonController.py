import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Models.addPerson import AddPerson
from Database.Connection import connection

class CreatePersonController():
    def __init__(self, crear_persona):
        self.AddPerson = AddPerson(connection())
        self.crear_persona = crear_persona
    
    def createPerson(self,idd,nombre,apellido,edad,ocupacion,telefono,direccion,fechaNac,estCivil,observaciones,Create_data):
        if idd and nombre and apellido and edad and ocupacion and telefono and direccion and fechaNac and estCivil:
            self.AddPerson.insertPerson(idd,nombre,apellido,edad,ocupacion,telefono,direccion,fechaNac,estCivil,observaciones)
            Create_data.hide()
