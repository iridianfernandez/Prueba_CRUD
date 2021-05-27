# Prueba_CRUD

en tabla_colores es donde tengo prácticamente todo el código para no utilizar la importación de clases, 
lo único que falta es ligar la tabla de crear con el botón


Estoy utilizando:
	-Visual Studio Code
	-MySQL workbench
	-PHPMyAdmin
	-python3
	-PyQt5
	
	
En PyQt5CRUDmysql tengo 4 carpetas:

	Controllers: tengo los controladores de las venatanas UI del crud,  para no tenerlo todo en un sólo archivo.
    	en CreatePersonController defino las funciones que me van a servir para crear un nuevo usuario apoyándome de la  interfaz gŕafica "Crear.py" (Ubicada en Views)
	En PrincipalController me encargo de definir las funciones que ejecutarán los botones en la ventana principal, en mi caso llamada: "crud" la cual se encuentra ubicada en Views.
	
	En la carpeta "Database" me encargo de hacer la conexión entre mi programa y la base de datos previamente creada, definiendo un puerdo, un usuario y una contraseña. 
	
	En Models tengo la clase AddPerson que sirve para recolectar los datos de las personas que se van agregando así como también para recuperar sus datos de la tabla. 
	
	En Views tengo las tablas de forma gráfica del crud y para agregar los datos de las personas, así como también tengo las mismas tablar en código para poder unirlos con los demás códigos de las demás carpetas utilizando: "from nombreCarpeta import nombreClase"




