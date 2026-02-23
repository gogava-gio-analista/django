from django.db import models
import oracledb
# Create your models here.
class Departamento:
    def __init__(self):
        self.id = 0
        self.nombre = ''
        self.localidad = ''

class ServiceDepartamentos:
    def __init__(self):
        self.connection = oracledb.connect(user='system',
                                           password='ORACLE',
                                           dsn = 'localhost/freepdb1')

    def getDepartamentos(self):
        sql = 'select * from dept'
        cursor = self.connection.cursor()
        cursor.execute(sql)
        listaDepartamentos = []
        for row in cursor:
            dept = Departamento()
            dept.id = row[0]
            dept.nombre = row[1]
            dept.localidad = row[2]
            listaDepartamentos.append(dept)
        cursor.close()
        return listaDepartamentos
    
    def insertarDepartamento(self, id, nombre, loc):
        cursor = self.connection.cursor()
        sql = 'insert into dept values (:id, :nom, :loc)'
        cursor.execute(sql, (id, nombre, loc,))
        self.connection.commit()
        cursor.close()

    def updatedept(self, id, nombre, loc):
        cursor = self.connection.cursor()
        sql = 'update dept set nombre=:nom, loc=:loc where id=:id'
        cursor.execute(sql, (nombre, loc, id,))
        self.connection.commit()
        cursor.close()

    def buscardept(self,id):
        sql = 'select * from dept where dept_no=:id'
        cursor = self.connection.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        dept = Departamento()
        dept.id = row[0]
        dept.nombre = row[1]
        dept.localidad = row[2]
        cursor.close()
        return dept 