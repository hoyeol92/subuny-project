import pymysql as ps

table = [#'tb_sensor_o2_hr','tb_sensor_temp','tb_sensor_humid',
         'tb_sensor_ecg','tb_sensor_emg']
column = [#['data_ir','data_hr','data_o2'],['data_temp'],['data_humid'],
          ['data_ecg'],['data_emg']]
sensor=[#['1','2','3'],['4'],['5'],['6'],['7']
        ['1'],['2']]
def insert_db(tb,col,data):
    conn = ps.connect(host='project-db-stu2.ddns.net', user='flex', passwd='1234', db='flex', port=3307)
    curs = conn.cursor()
    sql = f"insert into {tb}({col}) values ('{data}')"
    curs.execute(sql)
    conn.commit()
    curs.close()
    conn.close()
    
def insert_db2(tb,col1,col2,col3,data1,data2,data3):
    conn = ps.connect(host='project-db-stu2.ddns.net', user='flex', passwd='1234', db='flex', port=3307)
    curs = conn.cursor()
    sql = f"insert into {tb}({col1},{col2},{col3}) values ('{data1}','{data2}','{data3}')"
    curs.execute(sql)
    conn.commit()
    curs.close()
    conn.close()
    
def select_db():
    conn = ps.connect(host='project-db-stu2.ddns.net', user='flex', passwd='1234', db='flex', port=3307)
    curs = conn.cursor()
    sql = f"select * from tb_sensor_temp"
    curs.execute(sql)
    result = curs.fetchall()
    print(result)
    curs.close()
    conn.close()
    return result