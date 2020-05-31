import pymysql
from conexion import Conexion
from sqlalchemy import create_engine
from json import dumps
cx = Conexion()

class Usuario:
    idusuario = 0
    nomuser = ""
    clave = ""
    estado = ""
    def readAll(self):
        try:
            conexion=cx.conecta()
            cursor = conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('listar_usuario')
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            conexion.close()
    def delete(self):
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('delete_usuario',[self.idusuario])
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def agregarusuario(self):
        nomuser=self.nomuser
        clave=self.clave
        data=[nomuser,clave]
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("create_usuario",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def buscarusuario(self):
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('read_usuario',[self.idusuario,])
            rows=cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def modificarusuario(self):
        try:
            idu=self.idusuario
            nomuser=self.nomuser
            clave=self.clave
            data=[nomuser,clave,idu]
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("update_usuario",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()