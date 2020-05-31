import pymysql
class Conexion:
    def __init__(self):
        self._HOST = "bggfrshj1fhn1qnw0dtk-mysql.services.clever-cloud.com"
        self._USER = "uzkpobgdqkjbqxsa"
        self._PASS = "7Risj2IafnwimbREYZnD"
        self._BD = "bggfrshj1fhn1qnw0dtk"
    def conecta(self):
        bd = pymysql.connect(self._HOST, self._USER, self._PASS, self._BD, port=3306)
        print("Conexion Exitosa...!")
        return bd
cx = Conexion()
print(cx.conecta())