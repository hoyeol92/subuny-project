import pymysql

class Databases():
    def __init__(self):
        self.db =pymysql.connect(host='localhost', dbname='notingbetter',user='chungwon',password='1234',port=5432)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.execute("ROLLBACK")
        self.cursor.commit()