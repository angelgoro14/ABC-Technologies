# Importación de librerias
import pylogix                         # Libreria comunicación con PLC AB
import pymysql                         # Libreria comunicación con MYSQL
import time                            # Libreria para espacios de tiempo
import mysql.connector                 # Libreria comunicacion MYSQL
import datetime                        # Libreria datos de tiempo
from pylogix import PLC
from mysql.connector import Error

# Imprimir todas las tags del PLC
with PLC("192.168.1.30") as comm:      # Ingresar la dirección IP del PLC
    tags = comm.GetTagList()           # Obtener las tags
    for t in tags.Value:
        print('\033[1m', "Nombre:", '\033[0m', t.TagName, '\033[1m', "\t\tTipo:", '\033[0m', t.DataType)

# CREAR BASE DE DATOS MYSQL
# Verificación de conexión y creación de Base de datos
try:                                                 # Conexión a la base de datos
    db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Contr@ctor14+', db = 'plc_table')  
    if db.is_connected():                            # Verificación de la conexión a la base de datos con credenciales
        cursor = db.cursor()
        # Query 1 - Crear Tabla
        query_1 = "CREATE TABLE plc_abc(ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, NAME VARCHAR(45) NOT NULL, VALUE INT NOT NULL, NUMBERID INT NOT NULL, TIME TIMESTAMP(6) NOT NULL)"
        cursor.execute(query_1)                      # Ejecutar la Query
        db.commit()                                  # Confirmar la instrucción

except Error as ex:                                  # Verificación de errores
    print('Error durante la ejecución', ex)

# Función que agrega registros en MYSQL
def mysql_add(name, value, numberid, time):      # Query 2
    query_1 = "INSERT INTO plc_abc (NAME, VALUE, NUMBERID, TIME) VALUES ('{0}','{1}','{2}','{3}')".format(name, value, numberid, time)
    cursor.execute(query_1)                      # Ejecutar la Query
    db.commit()                                  # Confirmar la instrucción

# Función que actualiza registros en MYSQL
def mysql_upd(numberid, time, val):              # Query 3
    if numberid == 3:
        pass
    else:
    query_2 = "UPDATE plc_abc SET NUMBERID = '{0}', TIME = '{1}' WHERE VALUE='{2}'".format(numberid, time, val)
    cursor.execute(query_2)                      # Ejecutar la Query
    db.commit()                                  # Confirmar la instrucción

# Función que lleva el conteo repetitivo
def conteo(b, vector, conteo):
    index = vector.index(b)     # Obtener la posicion que ocupa el valor "b" en el vector "vector"
    if conteo[index] == 1:      # Ubicarse en el vector "conteo" sobre la posición obtenida anteriormente
        conteo[index] = 2       # Si la posicion es 1, actualizar a 2
    else:
        conteo[index] = 3       # Cualquier otro valor, actualizar a 3
    return conteo[index]

# Principal comunicación con PLC
b_v = []          # Vector para almacenar valores de variable B
b_i = []          # Vector para almacenar conteo de variable B
b_1 = 0           # Valor inicial para recursividad

with PLC("192.168.1.30") as ab:                            # Dirección IP del PLC
    while True:                                            # Ciclo Infinito
        b = ab.Read('Program:MainProgram.B')               # leer la variable B del PLC
        x = datetime.datetime.now()                        # Datos del tiempo                                       
        if b.Value == b_1:
            pass
        else:
            if b.Value in b_v:                                 # Si ya se tiene el valor de B
                a = conteo(b.Value, b_v, b_i)                  # Aplicar función de "conteo"
                mysql_upd(a, x, b.Value)                       # Aplicar función de "mysql_upd"

            else:                                              # Si no se tiene el valor de B
                b_v.append(b.Value)                            # Guardar el valor de la variable B en el vector
                b_i.append(1)                                  # Aumentar el vector de conteo con '1'
                mysql_add(b.TagName, b.Value, 1, x)            # Aplicar función de "mysql_add"
            b_1 = b.Value