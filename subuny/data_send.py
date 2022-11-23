from flask import Flask, request
import db
app = Flask(__name__)
@app.route('/insert', methods=['GET'])
def insert():
    if request.method == 'GET':
        for i,j,k in zip(db.table,db.column,db.sensor):
            print(i)
            print(j)
            print(k)
            
            if len(j) == 3:
                    data1 = request.args['data1']
                    data2 = request.args['data2']
                    data3 = request.args['data3']
                    data=[data1,data2,data3]
                    print(data)
                    db.insert_db2(i,j[0],j[1],j[2],data1,data2,data3)
                    
            else :
                    
                    data = request.args[f'data{k[0]}']
                    print(data)
                    db.insert_db(i,j[0],data)
    return '', 204
                    
                    
@app.route('/select')
def select():
    result = db.select_db()
    print(result)
    return '데이터 출력 성공'
if __name__ == '__main__':
    # app.run(host='192.168.101.197', port=5026)
    app.run(host='0.0.0.0', port=5026)