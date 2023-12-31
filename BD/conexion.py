import mysql.connector
from mysql.connector import Error

#Data Access Object, realiza consultas.
class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306, #puerto cambiado vs windows.
                user='root',
                password='',
                db='correo_yuri' #nombre bd con Mayus
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarTrabajador(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('SELECT `rut`, `nombre_completo`, `sexo`, `cargo` FROM `trabajador`;')  #Nombre tabla con Mayus.
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
    def registrarTrabajador(self, trabajador):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO trabajador (rut, nombre_completo, sexo, cargo, direccion, telefono, fecha_ingreso, id_area,id_departamento) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}','{8}')"
                cursor.execute(sql.format(trabajador[0],trabajador[1],trabajador[2],trabajador[3],trabajador[4], trabajador[5],trabajador[6],trabajador[7],trabajador[8]))
                self.conexion.commit()
                print("¡Trabajador registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    def registrarContacto(self, contacto):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sql = "INSERT INTO contacto_emergencia (rut_contacto, nombre_completo,relacion,telefono,rut) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')"
                    cursor.execute(sql.format(contacto[0],contacto[1],contacto[2],contacto[3],contacto[4]))
                    self.conexion.commit()
                    print("¡Trabajador registrado!\n")
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))
    def registrarCarga(self, carga):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO carga_familiar(rut_carga, nombre_completo, parentesco, rut) VALUES ('{0}','{1}','{2}','{3}')"
                cursor.execute(sql.format(carga[0], carga[1], carga[2], carga[3]))
                self.conexion.commit()
                print("¡Contacto registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarTrabajador(self, trabajador):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE trabajado SET Titulo = '{1}', Genero = '{2}', Descripcion = '{3}', Duracion = '{4}' WHERE Id = '{0}'"
                cursor.execute(sql.format(trabajador[0], trabajador[1], trabajador[2],trabajador[3],trabajador[4],trabajador[5],trabajador[6]))
                self.conexion.commit()
                print("¡Contacto actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
    def eliminarTrabajador(self, rut):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM trabajador WHERE rut = '{0}'"
                cursor.execute(sql.format(rut))
                self.conexion.commit()
                print("¡Contacto eliminado!\n")
            except Error as error: #ejemplo de uso de rollback
                print("Fallo al intentar eliminar dato rollback: {}".format(error))
                # revirtiendo los cambios
                self.conexion.rollback()
            finally:
                # closing database connection.
                if self.conexion.is_connected():
                    cursor.close()
                    #conn.close()
                    #print("connection is closed")
            """except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))"""
            
    def listararea(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('SELECT * FROM area;')  #Nombre tabla con Mayus.
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def listarDepartamento(self):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    cursor.execute('SELECT * FROM departamento;')  #Nombre tabla con Mayus.
                    resultados = cursor.fetchall()
                    return resultados
                except Error as ex:
                    print("Error al intentar la conexión: {0}".format(ex))


    def listarsexo(self, sexo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = 'SELECT * FROM trabajador WHERE sexo = %s'
                cursor.execute(sql, (sexo,))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    def listarCargo(self,cargo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = 'SELECT * FROM trabajador WHERE cargo = %s'
                cursor.execute(sql, (cargo,))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    def listarArea(self,area):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = 'SELECT * FROM trabajador WHERE id_area= %s'
                cursor.execute(sql, (area,))
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))



