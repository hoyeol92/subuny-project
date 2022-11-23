
from flask import Flask
from flask import render_template
from flask import request
from flaskserver import CRUD
import pymysql


num1=""
app=Flask(__name__)

@app.route('/')

def index():
    return render_template("index1.html")


def data():
    if request.method=='GET':
        num1=request.args['num1']
        return num1

if __name__=='__main__':
    app.run(host='192.168.30.113',port=5021)
    db = CRUD()
    db.insertDB(schema="public",table='yw_table',colum='id',data=num1)
    print(db.readDB(schema='public',table='yw_table',colum='id'))
    db.updateDB(schema='public',table='yw_table',colum='id', value='와우',condition='유동적변경')
    db.deleteDB(schema='public',table='yw_table',condition ="id != 'd'")