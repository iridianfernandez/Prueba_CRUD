from os import stat_result

class AddPerson():
	def __init__(self,conn):
		self.conn =conn
		with self.conn.cursor() as cursor:
		 
			sql = """CREATE TABLE IF NOT EXISTS person
						(idd VARCHAR(45) NOT NULL,
						nombre VARCHAR(45) NOT NULL,
						apellido VARCHAR(45) NOT NULL,
						edad VARCHAR(45) NOT NULL,
						ocupacion VARCHAR(45) NOT NULL,
						telefono VARCHAR (45) NOT NULL,
						direccion VARCHAR(45) NOT NULL,
						fechaNac VARCHAR(45) NOT NULL,
						estCivil VARCHAR(45) NOT NULL,
						observaciones VARCHAR(45) NOT NULL"""
			cursor.execute(sql)
			self.conn.commit()

#	def getPersons(self):
#		with self.cursor() as cursor:
#			sql = """SELECT * FROM person"""
#			cursor.execute(sql)
#			result = cursor.fetchall()
#			return result
	
#	def getPerson(self, idd):
#		with self.cursor() as cursor:
#			sql = """SELECT * FROM person WHERE idd = %s"""
#			cursor.execute(sql,idd)
#			result = cursor.fetchone()
#			if result:
#				return result
	
#	def updatePerson(self,idd,nombre,apellido,edad,ocupacion,telefono,domicilio,fechaNac,estCivil,observaciones):
#		with self.cursor() as cursor:
#			sql = """UPDATE person SET nombre = %s, apellido = %s, edad = %s, ocupacion = %s, telefono = %s, domicilio  = %s,fechaNac = %s,EstCivil=%s, observaciones= %s WHERE idd = %s """
#			cursor.execute(sql,(nombre,apellido,edad,ocupacion,idd,telefono,domicilio,fechaNac,estCivil,observaciones))
#			self.commit()

#	def deletePerson(self,idd):
#	with self.cursor() as cursor:
#			sql = """DELETE FROM person WHERE idd = %s"""
#			cursor.execute(sql, idd)
#			self.commit()
	
#	def insertPerson(self,idd,nombre,apellido,edad,ocupacion,telefono,domicilio,fechaNac,estCivil,observaciones):
#		with self.cursor() as cursor:
#			sql = """INSERT INTO person (idd,nombre,apellido,edad,ocupacion,telefono,domicilio,fechaNac,estCivil,observaciones) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
#			cursor.execute(sql, (idd,nombre,apellido,edad,ocupacion,telefono,domicilio,fechaNac,estCivil,observaciones))
#			self.commit()