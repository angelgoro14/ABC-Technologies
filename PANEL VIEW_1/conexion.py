import mysql.connector
 
class Registro_datos():
    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost', database ='abc', user = 'root', password ='AnGeL14&%.#')

    def inserta_producto(self,id_1, nombre, valor, numberid, fecha):
        cur = self.conexion.cursor()
        sql='''INSERT INTO omron (ID, NOMBRE, VALOR, NUMBERID, FECHA) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(id_1, nombre, valor, numberid, fecha)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM omron " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, valor):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM omron WHERE VALOR = {}".format(valor)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def elimina_productos(self,valor):
        cur = self.conexion.cursor()
        sql='''DELETE FROM omron WHERE VALOR = {}'''.format(valor)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def actualiza_productos(self, id, nombre, valor, numberid, fecha):
        cur = self.conexion.cursor()
        sql = "UPDATE omron SET NOMBRE = '{}', VALOR = '{}', NUMBERID = '{}', FECHA = '{}' WHERE ID = '{}'".format(nombre, valor, numberid, fecha, id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a